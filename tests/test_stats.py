from golf.models import GolferTournamentScore
from golf.stats import StatsCalculator
def test_stats_calculator():

    tournament_scores = [
        GolferTournamentScore(golfer_name="Rory McIlroy", total_score=288),
        GolferTournamentScore(golfer_name="Jordan Spieth", total_score=289),
        GolferTournamentScore(golfer_name="Sergio Garcia", total_score=290),
        GolferTournamentScore(golfer_name="Tiger Woods", total_score=291),
        GolferTournamentScore(golfer_name="Kenny Perry", total_score=292),
    ]

    stats_calculator = StatsCalculator(tournament_scores=tournament_scores)
    stats = stats_calculator.calculate_stats()

    assert stats.stats["win_fractions"] == {
        "Rory McIlroy": 1.0,
        "Jordan Spieth": 0.0,
        "Sergio Garcia": 0.0,
        "Tiger Woods": 0.0,
        "Kenny Perry": 0.0
    }

def test_calculate_win_fractions_no_ties():
    # Table 1 example - no ties
    tournament_scores = [
        GolferTournamentScore(golfer_name="Rory McIlroy", total_score=288),
        GolferTournamentScore(golfer_name="Jordan Spieth", total_score=289),
        GolferTournamentScore(golfer_name="Sergio Garcia", total_score=290),
        GolferTournamentScore(golfer_name="Tiger Woods", total_score=291),
        GolferTournamentScore(golfer_name="Kenny Perry", total_score=292),
        GolferTournamentScore(golfer_name="John Cook", total_score=293),
        GolferTournamentScore(golfer_name="Jaco Van Zyl", total_score=294),
        GolferTournamentScore(golfer_name="Justin Rose", total_score=295)
    ]

    stats_calculator = StatsCalculator(tournament_scores=tournament_scores)
    win_fractions = stats_calculator._calculate_win_fractions()

    assert win_fractions == {
        "Rory McIlroy": 1.0,
        "Jordan Spieth": 0.0,
        "Sergio Garcia": 0.0,
        "Tiger Woods": 0.0,
        "Kenny Perry": 0.0,
        "John Cook": 0.0,
        "Jaco Van Zyl": 0.0,
        "Justin Rose": 0.0
    }


def test_calculate_win_fractions_with_ties():
    # Table 2 example - with ties
    tournament_scores = [
        GolferTournamentScore(golfer_name="Rory McIlroy", total_score=288),
        GolferTournamentScore(golfer_name="Jordan Spieth", total_score=288),
        GolferTournamentScore(golfer_name="Sergio Garcia", total_score=290),
        GolferTournamentScore(golfer_name="Tiger Woods", total_score=291),
        GolferTournamentScore(golfer_name="Kenny Perry", total_score=291),
        GolferTournamentScore(golfer_name="John Cook", total_score=291),
        GolferTournamentScore(golfer_name="Jaco Van Zyl", total_score=294),
        GolferTournamentScore(golfer_name="Justin Rose", total_score=295)
    ]
    
    expected = {
        "Rory McIlroy": 0.5,
        "Jordan Spieth": 0.5,
        "Sergio Garcia": 0.0,
        "Tiger Woods": 0.0,
        "Kenny Perry": 0.0,
        "John Cook": 0.0,
        "Jaco Van Zyl": 0.0,
        "Justin Rose": 0.0
    }
    
    stats_calculator = StatsCalculator(tournament_scores=tournament_scores)
    win_fractions = stats_calculator._calculate_win_fractions()
    assert win_fractions == expected


def test_calculate_top5_fractions_no_ties():
    # Table 1 example - no ties
    tournament_scores = [
        GolferTournamentScore(golfer_name="Rory McIlroy", total_score=288),
        GolferTournamentScore(golfer_name="Jordan Spieth", total_score=289),
        GolferTournamentScore(golfer_name="Sergio Garcia", total_score=290),
        GolferTournamentScore(golfer_name="Tiger Woods", total_score=291),
        GolferTournamentScore(golfer_name="Kenny Perry", total_score=292),
        GolferTournamentScore(golfer_name="John Cook", total_score=293),
        GolferTournamentScore(golfer_name="Jaco Van Zyl", total_score=294),
        GolferTournamentScore(golfer_name="Justin Rose", total_score=295)
    ]
    
    expected = {
        "Rory McIlroy": 1.0,
        "Jordan Spieth": 1.0,
        "Sergio Garcia": 1.0,
        "Tiger Woods": 1.0,
        "Kenny Perry": 1.0,
        "John Cook": 0.0,
        "Jaco Van Zyl": 0.0,
        "Justin Rose": 0.0
    }
    
    stats_calculator = StatsCalculator(tournament_scores=tournament_scores)
    top5_fractions = stats_calculator._calculate_top5_fractions()
    assert top5_fractions == expected

def test_calculate_top5_fractions_with_ties():
    # Table 2 example - with ties
    tournament_scores = [
        GolferTournamentScore(golfer_name="Rory McIlroy", total_score=288),
        GolferTournamentScore(golfer_name="Jordan Spieth", total_score=288),
        GolferTournamentScore(golfer_name="Sergio Garcia", total_score=290),
        GolferTournamentScore(golfer_name="Tiger Woods", total_score=291),
        GolferTournamentScore(golfer_name="Kenny Perry", total_score=291),
        GolferTournamentScore(golfer_name="John Cook", total_score=291),
        GolferTournamentScore(golfer_name="Jaco Van Zyl", total_score=294),
        GolferTournamentScore(golfer_name="Justin Rose", total_score=295)
    ]
    
    expected = {
        "Rory McIlroy": 1.0,
        "Jordan Spieth": 1.0,
        "Sergio Garcia": 1.0,
        "Tiger Woods": 2/3,
        "Kenny Perry": 2/3,
        "John Cook": 2/3,
        "Jaco Van Zyl": 0.0,
        "Justin Rose": 0.0
    }
    
    stats_calculator = StatsCalculator(tournament_scores=tournament_scores)
    top5_fractions = stats_calculator._calculate_top5_fractions()
    assert top5_fractions == expected

