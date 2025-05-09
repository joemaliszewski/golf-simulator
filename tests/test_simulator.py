from golf.models import Golfer
from golf.simulator import run_simulation

def test_simulator():

    golfer_data = {
        "Sergio Garcia": {
            "mean": 68.99802084636,
            "std": 2.8022106094
        },
        "Tiger Woods": {
            "mean": 69.35135041782,
            "std": 2.7891506279
        },
        "Kenny Perry": {
            "mean": 69.91471916678,
            "std": 2.779164583
        }
    }
    
    result = run_simulation(golfer_performance_data=golfer_data, num_tournaments=10)
    assert result is not None
    assert len(result["win_fractions"]) == 3
    assert len(result["top5_fractions"]) == 3

