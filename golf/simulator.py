from golf.models import Golfer, Tournament
from golf.stats import StatsCalculator


def run_simulation(golfer_performance_data: dict, num_tournaments: int) -> dict:

    golfers = []
    for golfer_name, score in golfer_performance_data.items():
        golfers.append(Golfer(name=golfer_name, mean=score["mean"], std_dev=score["std"]))

    all_simulated_stats = []
    for i in range(num_tournaments):
        tournament = Tournament(golfers=golfers, seed=i)
        scores = tournament.run()

        stats_calculator = StatsCalculator(tournament_scores=scores)
        stats = stats_calculator.calculate_stats()
        all_simulated_stats.append(stats)

    average_stats = {}
    for stat_type in all_simulated_stats[0].stats.keys():
        average_stats[stat_type] = {}
        for golfer in golfer_performance_data.keys():
            average_stats[stat_type][golfer] = sum(
                stat.stats[stat_type][golfer] for stat in all_simulated_stats
            ) / num_tournaments
        
        average_stats[stat_type] = dict(sorted(
            average_stats[stat_type].items(),
            key=lambda x: x[1],
            reverse=True
        ))

    return average_stats



    


    


        
    
