from golf.models import Golfer, Tournament


def test__golfer_play_round():
    golfer = Golfer(name="Happy Gilmore", mean=70, std_dev=2)
    score = golfer.play_round()
    assert score is not None
    assert score >= 0
    assert score <= 140

def test__golfer_play_tournament():
    golfer = Golfer(name="Happy Gilmore", mean=70, std_dev=2)
    score = golfer.play_tournament()
    assert score is not None
    assert score >= 0
    assert score <= 280


def test__tournament_run():
    golfer1 = Golfer(name="Happy Gilmore", mean=70, std_dev=2)
    golfer2 = Golfer(name="Shooter McGavin", mean=70, std_dev=2)
    tournament = Tournament(golfers=[golfer1, golfer2])
    scores = tournament.run()
    assert scores is not None
    assert len(scores) == 2