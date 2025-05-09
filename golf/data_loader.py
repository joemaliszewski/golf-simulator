import json
from typing import Dict, Any


def load_golfer_performance_data(file_path: str) -> Dict[str, Dict[str, float]]:
    """Load golfer scores from JSON file and return a dictionary of golfer statistics."""
    try:
        with open(file_path, 'r') as f:
            golfer_data = json.load(f)
    except FileNotFoundError as e:
        raise Exception(f"Could not find golfer scores file: {str(e)}")
    except json.JSONDecodeError as e:
        raise Exception(f"Invalid JSON format in golfer scores file: {str(e)}")

    golfer_performance_data = {}
    for golfer in golfer_data:
        golfer_performance_data[golfer['Golfer']] = {
            'mean': golfer['Mean'],
            'std': golfer['Standard deviation']
        }
    return golfer_performance_data