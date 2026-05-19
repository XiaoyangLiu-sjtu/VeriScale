# Coverage Report

Total executable lines: 9
Covered lines: 9
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def below_zero(operations):
2: ✓     cumulative = [0]
3: ✓     negative_found = False
4: ✓     for op in operations:
5: ✓         new_sum = cumulative[-1] + op
6: ✓         cumulative.append(new_sum)
7: ✓         if new_sum < 0:
8: ✓             negative_found = True
9: ✓     return cumulative, negative_found
```

## Complete Test File

```python
def below_zero(operations):
    cumulative = [0]
    negative_found = False
    for op in operations:
        new_sum = cumulative[-1] + op
        cumulative.append(new_sum)
        if new_sum < 0:
            negative_found = True
    return cumulative, negative_found

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = below_zero([1, 2, 3])
        assert result == ([0, 1, 3, 6], False), f"Test 1 failed: got {result}, expected {([0, 1, 3, 6], False)}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = below_zero([-1, 2, -1])
        assert result == ([0, -1, 1, 0], True), f"Test 2 failed: got {result}, expected {([0, -1, 1, 0], True)}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = below_zero([])
        assert result == ([0], False), f"Test 3 failed: got {result}, expected {([0], False)}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = below_zero([0, 0, 0])
        assert result == ([0, 0, 0, 0], False), f"Test 4 failed: got {result}, expected {([0, 0, 0, 0], False)}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = below_zero([10, -20, 5])
        assert result == ([0, 10, -10, -5], True), f"Test 5 failed: got {result}, expected {([0, 10, -10, -5], True)}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = below_zero([-1, -2, -3])
        assert result == ([0, -1, -3, -6], True), f"Test 6 failed: got {result}, expected {([0, -1, -3, -6], True)}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = below_zero([1, -1, 1, -1])
        assert result == ([0, 1, 0, 1, 0], False), f"Test 7 failed: got {result}, expected {([0, 1, 0, 1, 0], False)}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = below_zero([-5, 3, 1])
        assert result == ([0, -5, -2, -1], True), f"Test 8 failed: got {result}, expected {([0, -5, -2, -1], True)}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = below_zero([1000, 2000, -1500, -700, -900])
        assert result == ([0, 1000, 3000, 1500, 800, -100], True), f"Test 9 failed: got {result}, expected {([0, 1000, 3000, 1500, 800, -100], True)}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = below_zero([9223372036854775807, 9223372036854775807, -18446744073709551614])
        assert result == ([0, 9223372036854775807, 18446744073709551614, 0], False), f"Test 10 failed: got {result}, expected {([0, 9223372036854775807, 18446744073709551614, 0], False)}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = below_zero([1, 2, 4, 0])
        assert result == ([0, 1, 3, 7, 7], False), f"Test 11 failed: got {result}, expected {([0, 1, 3, 7, 7], False)}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = below_zero([1, 2, 3, 0])
        assert result == ([0, 1, 3, 6, 6], False), f"Test 12 failed: got {result}, expected {([0, 1, 3, 6, 6], False)}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = below_zero([-700, 2000, 0])
        assert result == ([0, -700, 1300, 1300], True), f"Test 13 failed: got {result}, expected {([0, -700, 1300, 1300], True)}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = below_zero([-2, -1])
        assert result == ([0, -2, -3], True), f"Test 14 failed: got {result}, expected {([0, -2, -3], True)}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = below_zero([0, 0, -8])
        assert result == ([0, 0, 0, -8], True), f"Test 15 failed: got {result}, expected {([0, 0, 0, -8], True)}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = below_zero([0, 0, 0, -6])
        assert result == ([0, 0, 0, 0, -6], True), f"Test 16 failed: got {result}, expected {([0, 0, 0, 0, -6], True)}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = below_zero([0, 0, -50, 0])
        assert result == ([0, 0, 0, -50, -50], True), f"Test 17 failed: got {result}, expected {([0, 0, 0, -50, -50], True)}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = below_zero([1, -20, 5])
        assert result == ([0, 1, -19, -14], True), f"Test 18 failed: got {result}, expected {([0, 1, -19, -14], True)}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = below_zero([-987654321, 0, 0])
        assert result == ([0, -987654321, -987654321, -987654321], True), f"Test 19 failed: got {result}, expected {([0, -987654321, -987654321, -987654321], True)}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = below_zero([1, 0, -987654321])
        assert result == ([0, 1, 1, -987654320], True), f"Test 20 failed: got {result}, expected {([0, 1, 1, -987654320], True)}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = below_zero([0, 1, 0])
        assert result == ([0, 0, 1, 1], False), f"Test 21 failed: got {result}, expected {([0, 0, 1, 1], False)}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = below_zero([-7, -1, 0])
        assert result == ([0, -7, -8, -8], True), f"Test 22 failed: got {result}, expected {([0, -7, -8, -8], True)}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = below_zero([0, -1, -3])
        assert result == ([0, 0, -1, -4], True), f"Test 23 failed: got {result}, expected {([0, 0, -1, -4], True)}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = below_zero([-4, -1, 0])
        assert result == ([0, -4, -5, -5], True), f"Test 24 failed: got {result}, expected {([0, -4, -5, -5], True)}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = below_zero([0, 1, -1])
        assert result == ([0, 0, 1, 0], False), f"Test 25 failed: got {result}, expected {([0, 0, 1, 0], False)}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = below_zero([-1, -1, 4, 0])
        assert result == ([0, -1, -2, 2, 2], True), f"Test 26 failed: got {result}, expected {([0, -1, -2, 2, 2], True)}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = below_zero([1, 5, 1, -1])
        assert result == ([0, 1, 6, 7, 6], False), f"Test 27 failed: got {result}, expected {([0, 1, 6, 7, 6], False)}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = below_zero([1, -1, 1, -1, 0])
        assert result == ([0, 1, 0, 1, 0, 0], False), f"Test 28 failed: got {result}, expected {([0, 1, 0, 1, 0, 0], False)}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = below_zero([-1, -42, -1, 1])
        assert result == ([0, -1, -43, -44, -43], True), f"Test 29 failed: got {result}, expected {([0, -1, -43, -44, -43], True)}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = below_zero([-1, 1, 1])
        assert result == ([0, -1, 0, 1], True), f"Test 30 failed: got {result}, expected {([0, -1, 0, 1], True)}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = below_zero([5, -3, -3, -900])
        assert result == ([0, 5, 2, -1, -901], True), f"Test 31 failed: got {result}, expected {([0, 5, 2, -1, -901], True)}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = below_zero([5, -6, -3, 2147483647])
        assert result == ([0, 5, -1, -4, 2147483643], True), f"Test 32 failed: got {result}, expected {([0, 5, -1, -4, 2147483643], True)}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = below_zero([5, -3, 7, -900])
        assert result == ([0, 5, 2, 9, -891], True), f"Test 33 failed: got {result}, expected {([0, 5, 2, 9, -891], True)}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = below_zero([1000, 0, -3, 5])
        assert result == ([0, 1000, 1000, 997, 1002], False), f"Test 34 failed: got {result}, expected {([0, 1000, 1000, 997, 1002], False)}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = below_zero([-5, 3, 1, 0, 10])
        assert result == ([0, -5, -2, -1, -1, 9], True), f"Test 35 failed: got {result}, expected {([0, -5, -2, -1, -1, 9], True)}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = below_zero([-25, -25, -50, 100, 0, 0])
        assert result == ([0, -25, -50, -100, 0, 0, 0], True), f"Test 36 failed: got {result}, expected {([0, -25, -50, -100, 0, 0, 0], True)}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = below_zero([100, -50, -25, -20])
        assert result == ([0, 100, 50, 25, 5], False), f"Test 37 failed: got {result}, expected {([0, 100, 50, 25, 5], False)}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = below_zero([-123456788, 0, 0, -123456788, -1, 2])
        assert result == ([0, -123456788, -123456788, -123456788, -246913576, -246913577, -246913575], True), f"Test 38 failed: got {result}, expected {([0, -123456788, -123456788, -123456788, -246913576, -246913577, -246913575], True)}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = below_zero([-1000, -2000, 700, 900])
        assert result == ([0, -1000, -3000, -2300, -1400], True), f"Test 39 failed: got {result}, expected {([0, -1000, -3000, -2300, -1400], True)}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = below_zero([-1000, -2000, -899, 700, 900, 0, 0])
        assert result == ([0, -1000, -3000, -3899, -3199, -2299, -2299, -2299], True), f"Test 40 failed: got {result}, expected {([0, -1000, -3000, -3899, -3199, -2299, -2299, -2299], True)}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = below_zero([-2147483648, 1, 2147483647])
        assert result == ([0, -2147483648, -2147483647, 0], True), f"Test 41 failed: got {result}, expected {([0, -2147483648, -2147483647, 0], True)}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = below_zero([2147483647, 1, -2147483648, 0, 8])
        assert result == ([0, 2147483647, 2147483648, 0, 0, 8], False), f"Test 42 failed: got {result}, expected {([0, 2147483647, 2147483648, 0, 0, 8], False)}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = below_zero([-2147483648, -1, 80])
        assert result == ([0, -2147483648, -2147483649, -2147483569], True), f"Test 43 failed: got {result}, expected {([0, -2147483648, -2147483649, -2147483569], True)}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = below_zero([987654321, -1111111110, 0, -12])
        assert result == ([0, 987654321, -123456789, -123456789, -123456801], True), f"Test 44 failed: got {result}, expected {([0, 987654321, -123456789, -123456789, -123456801], True)}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = below_zero([-123456789, -987654321, 1111111110, 0])
        assert result == ([0, -123456789, -1111111110, 0, 0], True), f"Test 45 failed: got {result}, expected {([0, -123456789, -1111111110, 0, 0], True)}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = below_zero([0, -123456788, -987654321, 0])
        assert result == ([0, 0, -123456788, -1111111109, -1111111109], True), f"Test 46 failed: got {result}, expected {([0, 0, -123456788, -1111111109, -1111111109], True)}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = below_zero([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -899, 0])
        assert result == ([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -909, -909], True), f"Test 47 failed: got {result}, expected {([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -909, -909], True)}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = below_zero([-1, -1, -1, -1, -1, -1, -1, -1, -1, -42, -49])
        assert result == ([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -51, -100], True), f"Test 48 failed: got {result}, expected {([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -51, -100], True)}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = below_zero([50, -10, -10, -10, -10, -1111111111, -899, 987654321, 2147483648])
        assert result == ([0, 50, 40, 30, 20, 10, -1111111101, -1111112000, -123457679, 2024025969], True), f"Test 49 failed: got {result}, expected {([0, 50, 40, 30, 20, 10, -1111111101, -1111112000, -123457679, 2024025969], True)}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = below_zero([-50, 10, 10, 10, 0])
        assert result == ([0, -50, -40, -30, -20, -20], True), f"Test 50 failed: got {result}, expected {([0, -50, -40, -30, -20, -20], True)}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = below_zero([-42, 0, 1, -2, 3, -4, 5, -6, 7, -2147483648])
        assert result == ([0, -42, -42, -41, -43, -40, -44, -39, -45, -38, -2147483686], True), f"Test 51 failed: got {result}, expected {([0, -42, -42, -41, -43, -40, -44, -39, -45, -38, -2147483686], True)}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = below_zero([42, 0, 0])
        assert result == ([0, 42, 42, 42], False), f"Test 52 failed: got {result}, expected {([0, 42, 42, 42], False)}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = below_zero([-18446744073709551614, 9223372036854775807, 9223372036854775807, 987654321, -4, 0])
        assert result == ([0, -18446744073709551614, -9223372036854775807, 0, 987654321, 987654317, 987654317], True), f"Test 53 failed: got {result}, expected {([0, -18446744073709551614, -9223372036854775807, 0, 987654321, 987654317, 987654317], True)}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
