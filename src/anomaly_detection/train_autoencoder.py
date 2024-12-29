import numpy as np
from autoencoder import build_autoencoder

def train_autoencoder(train_data, model_path):
    """Train the autoencoder on normal data and save the model."""
    autoencoder = build_autoencoder(input_dim=train_data.shape[1])
    autoencoder.fit(train_data, train_data, epochs=50, batch_size=32, validation_split=0.2)
    autoencoder.save(model_path)
    print(f"Autoencoder model saved to {model_path}")

if __name__ == "__main__":
    train_data = np.load("train_data.npy")
    train_autoencoder(train_data, "autoencoder_model.h5")

