from golf.data_loader import load_golfer_performance_data
from golf.simulator import run_simulation
from tabulate import tabulate


NUM_SIMULATIONS = 1000
NUM_ROUNDS_PER_TOURNAMENT = 4
DATA_FILE = "data/golfer_performance_data.json"

def main():

    golfer_data = load_golfer_performance_data(DATA_FILE)

    result = run_simulation(golfer_performance_data=golfer_data, num_tournaments=NUM_SIMULATIONS)

    win_data = [[golfer, f"{fraction*100:.1f}%"] for golfer, fraction in result["win_fractions"].items()]
    top5_data = [[golfer, f"{fraction*100:.1f}%"] for golfer, fraction in result["top5_fractions"].items()]

    print("\nWin Fractions:")
    print(tabulate(win_data, headers=["Golfer", "Win %"], tablefmt="grid"))

    print("\nTop 5 Fractions:")
    print(tabulate(top5_data, headers=["Golfer", "Top 5 %"], tablefmt="grid"))

if __name__ == "__main__":
    main()