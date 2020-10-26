from ch_1.flat import Flat


def test_flat():
    assert Flat.flat(Flat(), sample_list=[1, 2, [3]]) == [1, 2, 3]
    assert Flat.flat(Flat(), sample_list=[1, 2, [3], []]) == [1, 2, 3]
    assert Flat.flat(Flat(), sample_list=[1, 2, [3], [3, 4, 5]]) == [1, 2, 3, 3, 4, 5]
    assert Flat.flat(Flat(), sample_list=[1, 2, [3], [7, [9, 2, 5], 4, 3, 2]]) == [1, 2, 3, 7, 9, 2, 5, 4, 3, 2]
