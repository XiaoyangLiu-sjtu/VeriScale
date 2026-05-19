# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def sumOfFourthPowerOfOddNumbers(n):
2: ✓     return sum((2 * i - 1)**4 for i in range(1, n + 1))
```

## Complete Test File

```python
def sumOfFourthPowerOfOddNumbers(n):
    return sum((2 * i - 1)**4 for i in range(1, n + 1))

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = sumOfFourthPowerOfOddNumbers(0)
        assert result == 0, f"Test 1 failed: got {result}, expected {0}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = sumOfFourthPowerOfOddNumbers(1)
        assert result == 1, f"Test 2 failed: got {result}, expected {1}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = sumOfFourthPowerOfOddNumbers(2)
        assert result == 82, f"Test 3 failed: got {result}, expected {82}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = sumOfFourthPowerOfOddNumbers(3)
        assert result == 707, f"Test 4 failed: got {result}, expected {707}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = sumOfFourthPowerOfOddNumbers(4)
        assert result == 3108, f"Test 5 failed: got {result}, expected {3108}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = sumOfFourthPowerOfOddNumbers(5)
        assert result == 9669, f"Test 6 failed: got {result}, expected {9669}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = sumOfFourthPowerOfOddNumbers(6)
        assert result == 24310, f"Test 7 failed: got {result}, expected {24310}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = sumOfFourthPowerOfOddNumbers(7)
        assert result == 52871, f"Test 8 failed: got {result}, expected {52871}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = sumOfFourthPowerOfOddNumbers(8)
        assert result == 103496, f"Test 9 failed: got {result}, expected {103496}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = sumOfFourthPowerOfOddNumbers(9)
        assert result == 187017, f"Test 10 failed: got {result}, expected {187017}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = sumOfFourthPowerOfOddNumbers(10)
        assert result == 317338, f"Test 11 failed: got {result}, expected {317338}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = sumOfFourthPowerOfOddNumbers(11)
        assert result == 511819, f"Test 12 failed: got {result}, expected {511819}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = sumOfFourthPowerOfOddNumbers(12)
        assert result == 791660, f"Test 13 failed: got {result}, expected {791660}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = sumOfFourthPowerOfOddNumbers(15)
        assert result == 2421007, f"Test 14 failed: got {result}, expected {2421007}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = sumOfFourthPowerOfOddNumbers(16)
        assert result == 3344528, f"Test 15 failed: got {result}, expected {3344528}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = sumOfFourthPowerOfOddNumbers(17)
        assert result == 4530449, f"Test 16 failed: got {result}, expected {4530449}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = sumOfFourthPowerOfOddNumbers(20)
        assert result == 10218676, f"Test 17 failed: got {result}, expected {10218676}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = sumOfFourthPowerOfOddNumbers(31)
        assert result == 91533855, f"Test 18 failed: got {result}, expected {91533855}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = sumOfFourthPowerOfOddNumbers(32)
        assert result == 107286816, f"Test 19 failed: got {result}, expected {107286816}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = sumOfFourthPowerOfOddNumbers(33)
        assert result == 125137441, f"Test 20 failed: got {result}, expected {125137441}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = sumOfFourthPowerOfOddNumbers(63)
        assert result == 3175130175, f"Test 21 failed: got {result}, expected {3175130175}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = sumOfFourthPowerOfOddNumbers(64)
        assert result == 3435274816, f"Test 22 failed: got {result}, expected {3435274816}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = sumOfFourthPowerOfOddNumbers(65)
        assert result == 3712197697, f"Test 23 failed: got {result}, expected {3712197697}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = sumOfFourthPowerOfOddNumbers(99)
        assert result == 30429094179, f"Test 24 failed: got {result}, expected {30429094179}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = sumOfFourthPowerOfOddNumbers(100)
        assert result == 31997333380, f"Test 25 failed: got {result}, expected {31997333380}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = sumOfFourthPowerOfOddNumbers(101)
        assert result == 33629574181, f"Test 26 failed: got {result}, expected {33629574181}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = sumOfFourthPowerOfOddNumbers(127)
        assert result == 105717319807, f"Test 27 failed: got {result}, expected {105717319807}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = sumOfFourthPowerOfOddNumbers(128)
        assert result == 109945570432, f"Test 28 failed: got {result}, expected {109945570432}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = sumOfFourthPowerOfOddNumbers(129)
        assert result == 114308040833, f"Test 29 failed: got {result}, expected {114308040833}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = sumOfFourthPowerOfOddNumbers(255)
        assert result == 3450208293119, f"Test 30 failed: got {result}, expected {3450208293119}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = sumOfFourthPowerOfOddNumbers(256)
        assert result == 3518392469760, f"Test 31 failed: got {result}, expected {3518392469760}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = sumOfFourthPowerOfOddNumbers(257)
        assert result == 3587650392321, f"Test 32 failed: got {result}, expected {3587650392321}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = sumOfFourthPowerOfOddNumbers(511)
        assert result == 111494409822719, f"Test 33 failed: got {result}, expected {111494409822719}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = sumOfFourthPowerOfOddNumbers(512)
        assert result == 112589632770560, f"Test 34 failed: got {result}, expected {112589632770560}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = sumOfFourthPowerOfOddNumbers(513)
        assert result == 113693445661185, f"Test 35 failed: got {result}, expected {113693445661185}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = sumOfFourthPowerOfOddNumbers(1023)
        assert result == 3585318987121663, f"Test 36 failed: got {result}, expected {3585318987121663}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = sumOfFourthPowerOfOddNumbers(1024)
        assert result == 3602876838585344, f"Test 37 failed: got {result}, expected {3602876838585344}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = sumOfFourthPowerOfOddNumbers(18)
        assert result == 6031074, f"Test 38 failed: got {result}, expected {6031074}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = sumOfFourthPowerOfOddNumbers(29)
        assert result == 65570653, f"Test 39 failed: got {result}, expected {65570653}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = sumOfFourthPowerOfOddNumbers(258)
        assert result == 3657994692946, f"Test 40 failed: got {result}, expected {3657994692946}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = sumOfFourthPowerOfOddNumbers(1025)
        assert result == 3620503409542145, f"Test 41 failed: got {result}, expected {3620503409542145}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = sumOfFourthPowerOfOddNumbers(28)
        assert result == 55014652, f"Test 42 failed: got {result}, expected {55014652}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = sumOfFourthPowerOfOddNumbers(2047)
        assert result == 115010927354742783, f"Test 43 failed: got {result}, expected {115010927354742783}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = sumOfFourthPowerOfOddNumbers(8187)
        assert result == 117699312174516271675, f"Test 44 failed: got {result}, expected {117699312174516271675}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = sumOfFourthPowerOfOddNumbers(202)
        assert result == 1076212311642, f"Test 45 failed: got {result}, expected {1076212311642}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = sumOfFourthPowerOfOddNumbers(34)
        assert result == 145288562, f"Test 46 failed: got {result}, expected {145288562}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = sumOfFourthPowerOfOddNumbers(62)
        assert result == 2930989550, f"Test 47 failed: got {result}, expected {2930989550}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = sumOfFourthPowerOfOddNumbers(56)
        assert result == 1761873400, f"Test 48 failed: got {result}, expected {1761873400}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = sumOfFourthPowerOfOddNumbers(197)
        assert result == 949449310853, f"Test 49 failed: got {result}, expected {949449310853}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = sumOfFourthPowerOfOddNumbers(254)
        assert result == 3383085328558, f"Test 50 failed: got {result}, expected {3383085328558}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = sumOfFourthPowerOfOddNumbers(259)
        assert result == 3729438102467, f"Test 51 failed: got {result}, expected {3729438102467}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = sumOfFourthPowerOfOddNumbers(394)
        assert result == 30382867248410, f"Test 52 failed: got {result}, expected {30382867248410}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
