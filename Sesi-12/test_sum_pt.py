from sum import sum_self_made

def test_sum():
    assert sum_self_made([1, 2, 3]) == 6, "Should be 6"

def test_sum2():
    assert sum_self_made((1, 2, 3)) == 6, "Should be 6"