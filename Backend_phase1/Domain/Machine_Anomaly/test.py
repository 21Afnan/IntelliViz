import os
import joblib
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt

# CONFIG
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_CSV = os.path.join(BASE_DIR, "ai4i2020.csv")  
MODEL_PATH = os.path.join(BASE_DIR, "lstm_classifier.pth")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.save")
CM_PATH = os.path.join(BASE_DIR, "confusion_matrix_test.png")
BATCH_SIZE = 64

FEATURES = [
    "Type",
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
]

# DATASET
class TestDataset(Dataset):
    def __init__(self, csv_path, scaler):
        df = pd.read_csv(csv_path)
        df["Type"] = df["Type"].map({"L":0,"M":1,"H":2}).astype(float)
        self.labels = df["Machine failure"].values
        data = df[FEATURES].values.astype(float)
        self.data = scaler.transform(data).astype(np.float32)
        
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return torch.tensor(self.data[idx]), torch.tensor(self.labels[idx], dtype=torch.float32)

# MODEL
class LSTMClassifier(nn.Module):
    def __init__(self, input_size, hidden_size=64):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size,1)
        self.sigmoid = nn.Sigmoid()
    def forward(self,x):
        x = x.unsqueeze(1)
        _, (h, _) = self.lstm(x)
        out = self.fc(h[-1])
        return self.sigmoid(out).squeeze()

# MAIN
def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    scaler = joblib.load(SCALER_PATH)
    print("Scaler loaded.")
    
    test_ds = TestDataset(TEST_CSV, scaler)
    test_loader = DataLoader(test_ds, batch_size=BATCH_SIZE, shuffle=False)
    
    model = LSTMClassifier(input_size=len(FEATURES)).to(device)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
    model.eval()
    print("Model loaded.")
    
    criterion = nn.BCELoss()
    all_preds = []
    all_labels = []
    losses = []
    
    with torch.no_grad():
        for X, y in test_loader:
            X, y = X.to(device), y.to(device)
            out = model(X)
            loss = criterion(out, y)
            losses.append(loss.item()*X.size(0))
            all_preds.extend((out.cpu().numpy()>0.5).astype(int))
            all_labels.extend(y.cpu().numpy().astype(int))
    
    avg_loss = np.sum(losses)/len(test_ds)
    print(f"\nAverage Test Loss: {avg_loss:.4f}")
    
    cm = confusion_matrix(all_labels, all_preds)
    print("\nConfusion Matrix:")
    print(cm)
    
    print("\nClassification Report:")
    print(classification_report(all_labels, all_preds, digits=4))
    
    overall_acc = np.mean(np.array(all_preds)==np.array(all_labels))*100
    print(f"\nOverall Test Accuracy: {overall_acc:.2f}%")
    
    # Save confusion matrix plot
    plt.figure(figsize=(4,4))
    plt.imshow(cm, cmap="Blues")
    plt.title("Confusion Matrix (Test)")
    plt.xticks([0,1], ["Pred 0","Pred 1"])
    plt.yticks([0,1], ["True 0","True 1"])
    for (i,j), v in np.ndenumerate(cm):
        plt.text(j,i,str(v), ha="center", va="center")
    plt.tight_layout()
    plt.savefig(CM_PATH)
    print("Confusion matrix saved.")

if __name__=="__main__":
    main()