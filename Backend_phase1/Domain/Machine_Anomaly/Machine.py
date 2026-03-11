import os
import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader, random_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt

# ========================
# CONFIG
# ========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "ai4i2020.csv")
BATCH_SIZE = 64
HIDDEN_SIZE = 64
EPOCHS = 20
LR = 0.001
VAL_SPLIT = 0.2
SEED = 42

MODEL_PATH = os.path.join(BASE_DIR, "lstm_classifier.pth")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.save")
LOSS_PLOT_PATH = os.path.join(BASE_DIR, "loss_plot.png")
CM_PATH = os.path.join(BASE_DIR, "confusion_matrix.png")

FEATURES = [
    "Type",
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
]

# ========================
# DATASET
# ========================
class AI4IDataset(Dataset):
    def __init__(self, csv_path):
        df = pd.read_csv(csv_path)
        df["Type"] = df["Type"].map({"L":0,"M":1,"H":2}).astype(float)
        self.labels = df["Machine failure"].values.astype(np.float32)
        data = df[FEATURES].values.astype(float)
        self.scaler = MinMaxScaler()
        self.data = self.scaler.fit_transform(data).astype(np.float32)
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return torch.tensor(self.data[idx]), torch.tensor(self.labels[idx], dtype=torch.float32)

# ========================
# MODEL
# ========================
class LSTMClassifier(nn.Module):
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        x = x.unsqueeze(1)  # add seq_len dim
        _, (h, _) = self.lstm(x)
        out = self.fc(h[-1])
        return out.squeeze()  # logits

# ========================
# TRAINING
# ========================
def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # --- Dataset ---
    dataset = AI4IDataset(CSV_PATH)
    joblib.dump(dataset.scaler, SCALER_PATH)
    print("Scaler saved.")

    # --- Calculate pos_weight for BCEWithLogitsLoss ---
    labels = dataset.labels
    normal = np.sum(labels == 0)
    anomaly = np.sum(labels == 1)
    pos_weight = torch.tensor([normal / anomaly]).to(device)
    print(f"Normal: {normal}, Anomaly: {anomaly}, Pos_weight: {pos_weight.item():.2f}")

    # --- Split dataset ---
    val_size = int(len(dataset) * VAL_SPLIT)
    train_size = len(dataset) - val_size
    train_ds, val_ds = random_split(dataset, [train_size, val_size], generator=torch.Generator().manual_seed(SEED))
    train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE, shuffle=False)

    # --- Model, Loss, Optimizer ---
    model = LSTMClassifier(input_size=len(FEATURES), hidden_size=HIDDEN_SIZE).to(device)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)

    train_losses = []
    val_losses = []

    for epoch in range(EPOCHS):
        # --- Training ---
        model.train()
        epoch_loss = 0
        for X, y in train_loader:
            X, y = X.to(device), y.to(device)
            optimizer.zero_grad()
            out = model(X)
            loss = criterion(out, y)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item() * X.size(0)
        train_loss = epoch_loss / len(train_loader.dataset)
        train_losses.append(train_loss)

        # --- Validation ---
        model.eval()
        val_loss_total = 0
        val_preds = []
        val_labels = []
        with torch.no_grad():
            for X, y in val_loader:
                X, y = X.to(device), y.to(device)
                out = model(X)
                loss = criterion(out, y)
                val_loss_total += loss.item() * X.size(0)
                probs = torch.sigmoid(out)
                val_preds.extend((probs.cpu().numpy() > 0.5).astype(int))
                val_labels.extend(y.cpu().numpy().astype(int))
        val_loss = val_loss_total / len(val_loader.dataset)
        val_losses.append(val_loss)

        val_acc = np.mean(np.array(val_preds) == np.array(val_labels)) * 100
        print(f"Epoch {epoch+1}/{EPOCHS} | Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f} | Val Acc: {val_acc:.2f}%")

    # --- Save model ---
    torch.save(model.state_dict(), MODEL_PATH)
    print("Model saved.")

    # --- Plot loss ---
    plt.figure(figsize=(8,5))
    plt.plot(train_losses, label="Train Loss", marker="o")
    plt.plot(val_losses, label="Val Loss", marker="o")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Training & Validation Loss")
    plt.legend()
    plt.grid(True)
    plt.savefig(LOSS_PLOT_PATH)
    print("Loss plot saved.")

    # --- Confusion Matrix & Report ---
    cm = confusion_matrix(val_labels, val_preds)
    print("\nConfusion Matrix:")
    print(cm)
    print("\nClassification Report:")
    print(classification_report(val_labels, val_preds, digits=4))
    overall_acc = np.mean(np.array(val_preds) == np.array(val_labels)) * 100
    print(f"\nOverall Accuracy: {overall_acc:.2f}%")

    # Save confusion matrix plot
    plt.figure(figsize=(4,4))
    plt.imshow(cm, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xticks([0,1], ["Pred 0","Pred 1"])
    plt.yticks([0,1], ["True 0","True 1"])
    for (i,j), v in np.ndenumerate(cm):
        plt.text(j,i,str(v), ha="center", va="center")
    plt.tight_layout()
    plt.savefig(CM_PATH)
    print("Confusion matrix saved.")

if __name__=="__main__":
    main()