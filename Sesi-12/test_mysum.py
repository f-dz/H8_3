from my_sum import sum

def test_my_sum():
    assert round(sum([0.1, 0.2, 0.3]), 2) == 0.60, "Should be 0.6"