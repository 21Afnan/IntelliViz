# ==============================
# LSTM Autoencoder for SWaT Dataset (PyTorch)
# ==============================

import torch
import torch.nn as nn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import Dataset, DataLoader

# ==============================
# DATASET CLASS
# ==============================
class SWaTDataset(Dataset):
    """
    Custom Dataset class for SWaT data with proper preprocessing:
    - Handles missing values
    - Drops non-numeric columns
    - Normalizes numeric features
    - Converts time-series into sequences for LSTM autoencoder
    """

    def __init__(self, file_path, window_size=10):
        self.window_size = window_size

        # Load CSV
        df = pd.read_csv(file_path)

        # Remove leading/trailing spaces from column names
        df.columns = df.columns.str.strip()

        # Drop Timestamp & Label columns if they exist
        df = df.drop(columns=[c for c in ['Timestamp', 'Normal/Attack'] if c in df.columns])

        # Fill NaN values (forward fill, then zero as fallback)
        df.fillna(method='ffill', inplace=True)
        df.fillna(0, inplace=True)

        # Drop non-numeric columns (if any remain)
        df = df.select_dtypes(include=[np.number])

        # Normalize numeric data
        self.scaler = MinMaxScaler()
        data = self.scaler.fit_transform(df.values)

        # Create sequences
        self.sequences = []
        for i in range(len(data) - window_size):
            self.sequences.append(data[i:i + window_size])
        self.sequences = np.array(self.sequences, dtype=np.float32)

    def __len__(self):
        """
        Returns the number of sequences in the dataset.
        PyTorch DataLoader uses this to know how many batches to generate.
        """
        return len(self.sequences)

    def __getitem__(self, idx):
        """
        Returns one sequence at index `idx` as a torch FloatTensor.
        PyTorch DataLoader uses this to fetch batch elements.
        """
        return torch.FloatTensor(self.sequences[idx])


# ==============================
# LSTM AUTOENCODER MODEL
# ==============================
class LSTMAutoencoder(nn.Module):
    """
    LSTM Autoencoder:
    Encoder -> Compress sequence
    Decoder -> Reconstruct sequence
    """

    def __init__(self, input_size, hidden_size):
        super(LSTMAutoencoder, self).__init__()
        self.encoder = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.decoder = nn.LSTM(hidden_size, input_size, batch_first=True)

    def forward(self, x):
        # Encode input sequence
        encoded, (hidden, cell) = self.encoder(x)

        # Decode sequence (using encoded output)
        decoded, _ = self.decoder(encoded)
        return decoded


# ==============================
# TRAINER CLASS
# ==============================
class Trainer:
    """
    Handles training of LSTM Autoencoder
    """

    def __init__(self, model, dataloader, device='cpu', lr=0.001, epochs=20, save_path='lstm_autoencoder.pth'):
        self.model = model.to(device)
        self.dataloader = dataloader
        self.device = device
        self.lr = lr
        self.epochs = epochs
        self.save_path = save_path

        self.criterion = nn.MSELoss()
        self.optimizer = torch.optim.Adam(model.parameters(), lr=lr)
        self.losses = []

    def train(self, print_batches=True):
        best_loss = float('inf')    
        for epoch in range(self.epochs):
            self.model.train()
            epoch_loss = 0
            total_batches = len(self.dataloader)

            for batch_idx, batch in enumerate(self.dataloader, start=1):
                batch = batch.to(self.device)

                # Zero gradients
                self.optimizer.zero_grad()

                # Forward pass
                output = self.model(batch)

                # Compute loss (reconstruction error)
                loss = self.criterion(output, batch)

                # Backprop
                loss.backward()
                self.optimizer.step()

                epoch_loss += loss.item() * batch.size(0)

                if print_batches:
                    print(f"Epoch [{epoch+1}/{self.epochs}], "
                          f"Batch [{batch_idx}/{total_batches}], "
                          f"Loss: {loss.item():.6f}")

            # Average epoch loss
            avg_loss = epoch_loss / len(self.dataloader.dataset)
            self.losses.append(avg_loss)

            print(f"✅ Epoch [{epoch+1}/{self.epochs}] completed, "
                  f"Avg Loss: {avg_loss:.6f}")

            # Save best model
            if avg_loss < best_loss:
                best_loss = avg_loss
                torch.save(self.model.state_dict(), self.save_path)
                print(f"🔹 Model saved with loss {best_loss:.6f}\n")    
    def plot_loss(self):
        plt.figure(figsize=(8,5))
        plt.plot(self.losses, marker='o')
        plt.title("Training Loss Curve")
        plt.xlabel("Epoch")
        plt.ylabel("Loss")
        plt.grid(True)
        plt.show()


# ==============================
# MAIN FUNCTION
# ==============================
def main():
    # Parameters
    FILE_PATH = "normal.csv"
    WINDOW_SIZE = 10
    BATCH_SIZE = 64
    HIDDEN_SIZE = 64
    EPOCHS = 3

    # Device
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print("Using device:", device)

    # Dataset
    dataset = SWaTDataset(FILE_PATH, window_size=WINDOW_SIZE)
     # ===== SAVE SCALER =====
    import joblib
    joblib.dump(dataset.scaler, "scaler.save")
    print("Scaler saved as 'scaler.save'")
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

    # Model
    sample = dataset[0]
    input_size = sample.shape[1]
    model = LSTMAutoencoder(input_size=input_size, hidden_size=HIDDEN_SIZE)

    # Trainer
    trainer = Trainer(model, dataloader, device=device, epochs=EPOCHS)

    # Train
    trainer.train()

    # Plot loss curve
    trainer.plot_loss()


if __name__ == "__main__":
    main()