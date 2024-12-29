import numpy as np
from tensorflow.keras.models import load_model

def detect_anomalies(input_data, model_path, threshold):
    """Detect anomalies based on reconstruction error."""
    model = load_model(model_path)
    reconstructions = model.predict(input_data)
    errors = np.mean(np.square(input_data - reconstructions), axis=1)
    anomalies = errors > threshold
    return anomalies, errors

if __name__ == "__main__":
    test_data = np.load("test_data.npy")
    anomalies, errors = detect_anomalies(test_data, "autoencoder_model.h5", threshold=0.05)
    print(f"Anomalies detected: {np.sum(anomalies)}")

