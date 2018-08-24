from read_data import read_csv


def test_read_csv_as_sparse():
    data = read_csv.read_csv_as_sparse('../test_data/ratings.csv', 0, 1, 2)
    print(data)


def test_read_csv_as_sparse2():
    data = read_csv.read_csv_as_sparse('../test_data/test_ratings.csv', 0, 1, 2)
    print(data)


test_read_csv_as_sparse()
