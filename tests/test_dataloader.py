from golf.data_loader import load_golfer_performance_data

def test__load_golfer_performance_data():

    golfer_performance_data_FILE = 'data/golfer_performance_data.json'

    golfer_data = load_golfer_performance_data(golfer_performance_data_FILE)
    assert len(golfer_data) > 0
    assert isinstance(golfer_data, dict)
