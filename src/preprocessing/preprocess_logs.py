import json
from collections import Counter

def preprocess_logs(input_file, output_file):
    """Convert raw logs into normalized frequency vectors."""
    with open(input_file, 'r') as file:
        logs = json.load(file)

    frequency = Counter(log['system_call'] for log in logs)
    total_calls = sum(frequency.values())
    normalized = {call: count / total_calls for call, count in frequency.items()}

    with open(output_file, 'w') as file:
        json.dump(normalized, file)
    print(f"Preprocessed logs saved to {output_file}")

if __name__ == "__main__":
    preprocess_logs("raw_logs.json", "preprocessed_logs.json")

