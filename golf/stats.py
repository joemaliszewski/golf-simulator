from golf.models import GolferTournamentScore
from typing import List
from pydantic import BaseModel
# 

class TournamentStats(BaseModel):
    stats: dict[str, dict[str, float]]

class StatsCalculator():

    def __init__(self, tournament_scores: List[GolferTournamentScore]):
        self.tournament_scores = tournament_scores
        
        
    def _calculate_win_fractions(self) -> dict[str, float]:
        """Return win fractions for golfers based on lowest score and ties."""

        if not self.tournament_scores:
            return {}
        
        result = {score.golfer_name: 0.0 for score in self.tournament_scores}
        lowest_score = min(score.total_score for score in self.tournament_scores)
        winners = [score.golfer_name for score in self.tournament_scores if score.total_score == lowest_score]
        win_fraction = 1.0 / len(winners)
        for winner in winners:
            result[winner] = win_fraction
        return result
    
    def _calculate_top5_fractions(self) -> dict[str, float]:
        """Return top 5 fractions for golfers based on ties and available spots."""

        if not self.tournament_scores:
            return {}
        
        result = {score.golfer_name: 0.0 for score in self.tournament_scores}


        scores = sorted(set(score.total_score for score in self.tournament_scores))
        spaces_left = 5

        

        for score in scores:
            
            golfers_with_score = [ts for ts in self.tournament_scores if ts.total_score == score]
            total_golfers_with_score = len(golfers_with_score)

            if spaces_left == 0:
                return result

            if total_golfers_with_score <= spaces_left:
                for golfer in golfers_with_score:
                    result[golfer.golfer_name] = 1.0
                spaces_left -= total_golfers_with_score
            else:
                fraction = spaces_left / total_golfers_with_score
                for golfer in golfers_with_score:
                    result[golfer.golfer_name] = fraction
                return result

        return result
    
    def calculate_stats(self) -> TournamentStats:

        stats = {
            "win_fractions": self._calculate_win_fractions(),
            "top5_fractions": self._calculate_top5_fractions()
        }

        tournament_stats = TournamentStats(stats=stats)

        return tournament_stats

    

