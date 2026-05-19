# Coverage Report

Total executable lines: 11
Covered lines: 11
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def maxProfit(prices):
2: ✓     if not prices:
3: ✓         return 0
4: ✓     min_price = prices[0]
5: ✓     max_profit = 0
6: ✓     for price in prices:
7: ✓         if price < min_price:
8: ✓             min_price = price
9: ✓         elif price - min_price > max_profit:
10: ✓             max_profit = price - min_price
11: ✓     return max_profit
```

## Complete Test File

```python
def maxProfit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = maxProfit([7, 1, 5, 3, 6, 4])
        assert result == 5, f"Test 1 failed: got {result}, expected {5}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = maxProfit([7, 6, 4, 3, 1])
        assert result == 0, f"Test 2 failed: got {result}, expected {0}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = maxProfit([2, 4, 1])
        assert result == 2, f"Test 3 failed: got {result}, expected {2}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = maxProfit([1, 2])
        assert result == 1, f"Test 4 failed: got {result}, expected {1}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = maxProfit([])
        assert result == 0, f"Test 5 failed: got {result}, expected {0}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = maxProfit([1, 1, 1, 1])
        assert result == 0, f"Test 6 failed: got {result}, expected {0}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = maxProfit([9, 1, 9])
        assert result == 8, f"Test 7 failed: got {result}, expected {8}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = maxProfit([100, 90, 80, 70, 60, 50, 40])
        assert result == 0, f"Test 8 failed: got {result}, expected {0}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = maxProfit([2, 2, 5, 0, 0, 3, 1, 4])
        assert result == 4, f"Test 9 failed: got {result}, expected {4}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = maxProfit([4294967295, 0, 4294967296])
        assert result == 4294967296, f"Test 10 failed: got {result}, expected {4294967296}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = maxProfit([13, 1, 5, 3, 6, 5])
        assert result == 5, f"Test 11 failed: got {result}, expected {5}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = maxProfit([3, 6, 3, 5, 1, 7, 0, 0, 0])
        assert result == 6, f"Test 12 failed: got {result}, expected {6}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = maxProfit([1000000000, 7, 4, 6, 3, 5, 1, 7])
        assert result == 6, f"Test 13 failed: got {result}, expected {6}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = maxProfit([7, 1, 5, 3, 6, 4, 0])
        assert result == 5, f"Test 14 failed: got {result}, expected {5}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = maxProfit([7, 6, 4, 3, 1, 100])
        assert result == 99, f"Test 15 failed: got {result}, expected {99}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = maxProfit([999999998, 20, 6, 7])
        assert result == 1, f"Test 16 failed: got {result}, expected {1}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = maxProfit([20, 6, 4, 3, 1, 4294967296, 0])
        assert result == 4294967295, f"Test 17 failed: got {result}, expected {4294967295}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = maxProfit([6, 4, 3, 1, 11, 0, 0])
        assert result == 10, f"Test 18 failed: got {result}, expected {10}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = maxProfit([4, 1, 13, 70])
        assert result == 69, f"Test 19 failed: got {result}, expected {69}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = maxProfit([2, 0, 0, 80, 18])
        assert result == 80, f"Test 20 failed: got {result}, expected {80}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = maxProfit([0, 100, 2])
        assert result == 100, f"Test 21 failed: got {result}, expected {100}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = maxProfit([1, 0])
        assert result == 0, f"Test 22 failed: got {result}, expected {0}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = maxProfit([1, 2, 5])
        assert result == 4, f"Test 23 failed: got {result}, expected {4}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = maxProfit([0, 1, 0])
        assert result == 1, f"Test 24 failed: got {result}, expected {1}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = maxProfit([1, 0])
        assert result == 0, f"Test 25 failed: got {result}, expected {0}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = maxProfit([0, 10, 0, 0, 0])
        assert result == 10, f"Test 26 failed: got {result}, expected {10}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = maxProfit([4, 3, 5, 1, 0, 0])
        assert result == 2, f"Test 27 failed: got {result}, expected {2}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = maxProfit([9007199254740991, 18, 16, 4, 6, 3, 5, 1, 7])
        assert result == 6, f"Test 28 failed: got {result}, expected {6}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = maxProfit([7, 1, 4, 3, 6, 4])
        assert result == 5, f"Test 29 failed: got {result}, expected {5}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = maxProfit([4, 3, 5, 1, 7, 8])
        assert result == 7, f"Test 30 failed: got {result}, expected {7}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = maxProfit([7, 1, 3, 6, 4, 0])
        assert result == 5, f"Test 31 failed: got {result}, expected {5}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = maxProfit([7, 6, 4, 80, 1])
        assert result == 76, f"Test 32 failed: got {result}, expected {76}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = maxProfit([2, 4, 1, 5])
        assert result == 4, f"Test 33 failed: got {result}, expected {4}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = maxProfit([5, 0, 2, 1])
        assert result == 2, f"Test 34 failed: got {result}, expected {2}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = maxProfit([1000000001, 0, 0, 10, 0, 0])
        assert result == 10, f"Test 35 failed: got {result}, expected {10}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = maxProfit([9007199254740991, 0, 3, 0, 100, 0])
        assert result == 100, f"Test 36 failed: got {result}, expected {100}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = maxProfit([6, 2, 16, 1, 9])
        assert result == 14, f"Test 37 failed: got {result}, expected {14}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = maxProfit([6, 2, 8, 1, 9, 0])
        assert result == 8, f"Test 38 failed: got {result}, expected {8}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = maxProfit([999999999, 11, 2, 9, 5])
        assert result == 7, f"Test 39 failed: got {result}, expected {7}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = maxProfit([20, 15, 1, 11, 2, 9, 4])
        assert result == 10, f"Test 40 failed: got {result}, expected {10}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = maxProfit([4, 9, 2, 1000000001, 15, 9007199254740990, 0])
        assert result == 9007199254740988, f"Test 41 failed: got {result}, expected {9007199254740988}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = maxProfit([40, 50, 13, 70, 80, 90, 0])
        assert result == 77, f"Test 42 failed: got {result}, expected {77}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = maxProfit([7, 5, 2, 3, 4294967296])
        assert result == 4294967294, f"Test 43 failed: got {result}, expected {4294967294}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = maxProfit([999999999, 1, 1000000002, 0, 9])
        assert result == 1000000001, f"Test 44 failed: got {result}, expected {1000000001}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = maxProfit([999999999, 1, 1000000000, 6, 1, 0])
        assert result == 999999999, f"Test 45 failed: got {result}, expected {999999999}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = maxProfit([1000000001, 999999998, 999999999, 1000000000, 0])
        assert result == 2, f"Test 46 failed: got {result}, expected {2}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = maxProfit([1000000000, 999999999, 70, 1000000001, 0])
        assert result == 999999931, f"Test 47 failed: got {result}, expected {999999931}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = maxProfit([1000000001, 17, 4294967296])
        assert result == 4294967279, f"Test 48 failed: got {result}, expected {4294967279}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = maxProfit([999999999, 999999998, 1000000001, 9007199254740991, 0])
        assert result == 9007198254740993, f"Test 49 failed: got {result}, expected {9007198254740993}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = maxProfit([4294967294, 0, 9, 0])
        assert result == 9, f"Test 50 failed: got {result}, expected {9}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = maxProfit([20, 19, 18, 40, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 2, 1, 0])
        assert result == 22, f"Test 51 failed: got {result}, expected {22}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
