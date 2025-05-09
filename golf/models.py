import random
from pydantic import BaseModel

class GolferTournamentScore(BaseModel):
    golfer_name: str
    total_score: float

class Golfer:
    def __init__(self, name: str, mean: float, std_dev: float):
        self.name = name
        self.mean = mean
        self.std_dev = std_dev
        self.results = []

    def play_round(self) -> float:
        return round(random.normalvariate(self.mean, self.std_dev)) 

    def play_tournament(self, num_rounds: int = 4) -> float:
        return sum(self.play_round() for _ in range(num_rounds))

class Tournament:
    def __init__(self, golfers: list[Golfer], num_rounds: int = 4, seed: int = None):
        self.golfers = golfers
        self.num_rounds = num_rounds
        if seed is not None:
            random.seed(seed)

    def run(self) -> list[GolferTournamentScore]:
        results = []
        for golfer in self.golfers:
            total_score = golfer.play_tournament(self.num_rounds)
            results.append(GolferTournamentScore(golfer_name=golfer.name, total_score=total_score))
        return results

