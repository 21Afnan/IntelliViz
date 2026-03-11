# ==============================
# test.py - LSTM Autoencoder Testing with Percentile Threshold
# ==============================

import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import Dataset, DataLoader
import joblib
import matplotlib.pyplot as plt

# ==============================
# DATASET CLASS (for test data)
# ==============================
class SWaTDatasetTest(Dataset):
    """
    Preprocess test data the same way as training:
    - Fill NaNs
    - Drop timestamp/label
    - Keep numeric only
    - Scale with saved scaler
    - Make sequences
    """
    def __init__(self, file_path, scaler, window_size=10):
        self.window_size = window_size

        # Load CSV
        self.df = pd.read_csv(file_path)
        self.df.columns = self.df.columns.str.strip()
        self.original_len = len(self.df)

        # Save original labels if present
        if 'Normal/Attack' in self.df.columns:
            self.labels = self.df['Normal/Attack'].values[self.window_size:]
        else:
            self.labels = None

        # Drop timestamp and label columns
        self.df = self.df.drop(columns=[c for c in ['Timestamp', 'Normal/Attack'] if c in self.df.columns])

        # Fill missing values
        self.df.fillna(method='ffill', inplace=True)
        self.df.fillna(0, inplace=True)

        # Keep only numeric columns
        self.df = self.df.select_dtypes(include=[np.number])

        # Scale using saved scaler
        data = scaler.transform(self.df.values)

        # Create sequences
        self.sequences = []
        for i in range(len(data) - window_size):
            self.sequences.append(data[i:i + window_size])
        self.sequences = np.array(self.sequences, dtype=np.float32)

    def __len__(self):
        return len(self.sequences)

    def __getitem__(self, idx):
        return torch.FloatTensor(self.sequences[idx])

# ==============================
# LSTM AUTOENCODER MODEL
# ==============================
class LSTMAutoencoder(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(LSTMAutoencoder, self).__init__()
        self.encoder = nn.LSTM(input_size, hidden_size, batch_first=True)
        self.decoder = nn.LSTM(hidden_size, input_size, batch_first=True)

    def forward(self, x):
        encoded, (hidden, cell) = self.encoder(x)
        decoded, _ = self.decoder(encoded)
        return decoded

# ==============================
# MAIN TEST FUNCTION
# ==============================
def main():
    FILE_PATH = "merged.csv"          # test data
    SCALER_PATH = "scaler.save"       # Saved scaler
    MODEL_PATH = "lstm_autoencoder.pth"  # Saved model weights
    WINDOW_SIZE = 10
    BATCH_SIZE = 64
    HIDDEN_SIZE = 64
    PERCENTILE = 95  # percentile for anomaly threshold
    DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

    # Load scaler
    scaler = joblib.load(SCALER_PATH)
    print(" Scaler loaded.")

    # Dataset & Dataloader
    dataset = SWaTDatasetTest(FILE_PATH, scaler, window_size=WINDOW_SIZE)
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=False)
    print(f" Test dataset loaded. {len(dataset)} sequences.")

    # Model
    input_size = dataset[0].shape[1]
    model = LSTMAutoencoder(input_size=input_size, hidden_size=HIDDEN_SIZE).to(DEVICE)
    model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
    model.eval()
    print(" Model loaded.")

    # Evaluate reconstruction errors
    criterion = nn.MSELoss(reduction='none')
    errors = []

    with torch.no_grad():
        for batch in dataloader:
            batch = batch.to(DEVICE)
            output = model(batch)
            batch_error = criterion(output, batch).mean(dim=(1,2)).cpu().numpy()
            errors.extend(batch_error)

    errors = np.array(errors)
    print(f" Testing completed. Mean reconstruction error: {errors.mean():.6f}")

    # -----------------------------
    # Detect anomalies using percentile
    # -----------------------------
    threshold = np.percentile(errors, PERCENTILE)
    print(f"Anomaly detection threshold ({PERCENTILE}th percentile): {threshold:.6f}")

    predictions = np.array(['Normal' if e <= threshold else 'Attack' for e in errors])

    # Save results to CSV
    result_df = pd.DataFrame({
        'Sequence_Index': np.arange(len(errors)),
        'Reconstruction_Error': errors,
        'Prediction': predictions
    })

    # Optional: include original labels if present
    if dataset.labels is not None:
        result_df['True_Label'] = dataset.labels

    result_df.to_csv("test_results_percentile.csv", index=False)
    print("✅ Test results saved to test_results_percentile.csv")

    # Optional: plot reconstruction errors
    plt.figure(figsize=(12,6))
    plt.plot(errors, marker='o', linestyle='', alpha=0.5, label='Reconstruction Error')
    plt.axhline(y=threshold, color='r', linestyle='--', label=f'{PERCENTILE}th Percentile Threshold')
    plt.title("Reconstruction Error for Test Sequences")
    plt.xlabel("Sequence index")
    plt.ylabel("MSE Error")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()