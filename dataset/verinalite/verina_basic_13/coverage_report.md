# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def cubeElements(a):
2: ✓     return [x * x * x for x in a]
```

## Complete Test File

```python
def cubeElements(a):
    return [x * x * x for x in a]

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = cubeElements([1, 2, 3, 4])
        assert result == [1, 8, 27, 64], f"Test 1 failed: got {result}, expected {[1, 8, 27, 64]}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = cubeElements([0, -1, -2, 3])
        assert result == [0, -1, -8, 27], f"Test 2 failed: got {result}, expected {[0, -1, -8, 27]}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = cubeElements([])
        assert result == [], f"Test 3 failed: got {result}, expected {[]}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = cubeElements([5])
        assert result == [125], f"Test 4 failed: got {result}, expected {[125]}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = cubeElements([-3, -3])
        assert result == [-27, -27], f"Test 5 failed: got {result}, expected {[-27, -27]}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = cubeElements([2])
        assert result == [8], f"Test 6 failed: got {result}, expected {[8]}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = cubeElements([-2])
        assert result == [-8], f"Test 7 failed: got {result}, expected {[-8]}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = cubeElements([2, -2])
        assert result == [8, -8], f"Test 8 failed: got {result}, expected {[8, -8]}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = cubeElements([3, 4, 5])
        assert result == [27, 64, 125], f"Test 9 failed: got {result}, expected {[27, 64, 125]}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = cubeElements([-3, -4, -5])
        assert result == [-27, -64, -125], f"Test 10 failed: got {result}, expected {[-27, -64, -125]}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = cubeElements([10, -10, 100, -100])
        assert result == [1000, -1000, 1000000, -1000000], f"Test 11 failed: got {result}, expected {[1000, -1000, 1000000, -1000000]}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = cubeElements([-7, -7, -7, -7, -7])
        assert result == [-343, -343, -343, -343, -343], f"Test 12 failed: got {result}, expected {[-343, -343, -343, -343, -343]}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = cubeElements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        assert result == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000], f"Test 13 failed: got {result}, expected {[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = cubeElements([2, -3, 5, -7, 11, -13, 17, -19])
        assert result == [8, -27, 125, -343, 1331, -2197, 4913, -6859], f"Test 14 failed: got {result}, expected {[8, -27, 125, -343, 1331, -2197, 4913, -6859]}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = cubeElements([9223372036854775807, -9223372036854775808])
        assert result == [784637716923335095224261902710254454442933591094742482943, -784637716923335095479473677900958302012794430558004314112], f"Test 15 failed: got {result}, expected {[784637716923335095224261902710254454442933591094742482943, -784637716923335095479473677900958302012794430558004314112]}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = cubeElements([999999999999999999, -999999999999999999])
        assert result == [999999999999999997000000000000000002999999999999999999, -999999999999999997000000000000000002999999999999999999], f"Test 16 failed: got {result}, expected {[999999999999999997000000000000000002999999999999999999, -999999999999999997000000000000000002999999999999999999]}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = cubeElements([123456789, -987654321, 111111111, -222222222])
        assert result == [1881676371789154860897069, -963418328693495609108518161, 1371742108367626890260631, -10973936866941015122085048], f"Test 17 failed: got {result}, expected {[1881676371789154860897069, -963418328693495609108518161, 1371742108367626890260631, -10973936866941015122085048]}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = cubeElements([42, -42, 42, -42, 0])
        assert result == [74088, -74088, 74088, -74088, 0], f"Test 18 failed: got {result}, expected {[74088, -74088, 74088, -74088, 0]}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = cubeElements([8, 1, 8, 2, 8, 3, 8, 4])
        assert result == [512, 1, 512, 8, 512, 27, 512, 64], f"Test 19 failed: got {result}, expected {[512, 1, 512, 8, 512, 27, 512, 64]}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = cubeElements([6, -6, 0, 6, -6, 0])
        assert result == [216, -216, 0, 216, -216, 0], f"Test 20 failed: got {result}, expected {[216, -216, 0, 216, -216, 0]}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = cubeElements([15, -14, 13, -12, 11, -10, 9, -8, 7, -6, 5, -4, 3, -2, 1])
        assert result == [3375, -2744, 2197, -1728, 1331, -1000, 729, -512, 343, -216, 125, -64, 27, -8, 1], f"Test 21 failed: got {result}, expected {[3375, -2744, 2197, -1728, 1331, -1000, 729, -512, 343, -216, 125, -64, 27, -8, 1]}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = cubeElements([1000, -1000, 10000, -10000, 100000, -100000])
        assert result == [1000000000, -1000000000, 1000000000000, -1000000000000, 1000000000000000, -1000000000000000], f"Test 22 failed: got {result}, expected {[1000000000, -1000000000, 1000000000000, -1000000000000, 1000000000000000, -1000000000000000]}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = cubeElements([31, 32, 33, -31, -32, -33])
        assert result == [29791, 32768, 35937, -29791, -32768, -35937], f"Test 23 failed: got {result}, expected {[29791, 32768, 35937, -29791, -32768, -35937]}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = cubeElements([2147483646, 2147483647, -2147483647, -2147483646])
        assert result == '-9903520286612926114398470136]', f"Test 24 failed: got {result}, expected {'-9903520286612926114398470136]'}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = cubeElements([9223372036854775806, 9223372036854775807, -9223372036854775807, -9223372036854775806])
        assert result == '-784637716923335094969050127519550606928412983852609306616]', f"Test 25 failed: got {result}, expected {'-784637716923335094969050127519550606928412983852609306616]'}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = cubeElements([0, 1, 8, 27, 64, 125, 216])
        assert result == [0, 1, 512, 19683, 262144, 1953125, 10077696], f"Test 26 failed: got {result}, expected {[0, 1, 512, 19683, 262144, 1953125, 10077696]}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = cubeElements([5, -5])
        assert result == [125, -125], f"Test 27 failed: got {result}, expected {[125, -125]}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = cubeElements([12, -1, 0, 1, -12])
        assert result == [1728, -1, 0, 1, -1728], f"Test 28 failed: got {result}, expected {[1728, -1, 0, 1, -1728]}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = cubeElements([1000000000000000000000000, -1000000000000000000000000])
        assert result == '-1000000000000000000000000000000000000000000000000000000000000000000000000]', f"Test 29 failed: got {result}, expected {'-1000000000000000000000000000000000000000000000000000000000000000000000000]'}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = cubeElements([3141592653589793, -2718281828459045])
        assert result == [31006276680299813114880451174049119330924860257, -20085536923187662523657426895773681168823516125], f"Test 30 failed: got {result}, expected {[31006276680299813114880451174049119330924860257, -20085536923187662523657426895773681168823516125]}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = cubeElements([9, 99, 999, 9999, -9, -99, -999, -9999])
        assert result == [729, 970299, 997002999, 999700029999, -729, -970299, -997002999, -999700029999], f"Test 31 failed: got {result}, expected {[729, 970299, 997002999, 999700029999, -729, -970299, -997002999, -999700029999]}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = cubeElements([1, 3, 9, 27, 81, 243, -1, -3, -9, -27, -81, -243])
        assert result == [1, 27, 729, 19683, 531441, 14348907, -1, -27, -729, -19683, -531441, -14348907], f"Test 32 failed: got {result}, expected {[1, 27, 729, 19683, 531441, 14348907, -1, -27, -729, -19683, -531441, -14348907]}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = cubeElements([1, 3, 4])
        assert result == [1, 27, 64], f"Test 33 failed: got {result}, expected {[1, 27, 64]}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = cubeElements([-1, 2, 3, 4, 42])
        assert result == [-1, 8, 27, 64, 74088], f"Test 34 failed: got {result}, expected {[-1, 8, 27, 64, 74088]}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = cubeElements([1, 2, 4, 0, 0, -9])
        assert result == [1, 8, 64, 0, 0, -729], f"Test 35 failed: got {result}, expected {[1, 8, 64, 0, 0, -729]}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = cubeElements([4, 3, 2])
        assert result == [64, 27, 8], f"Test 36 failed: got {result}, expected {[64, 27, 8]}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = cubeElements([1, 2, 4])
        assert result == [1, 8, 64], f"Test 37 failed: got {result}, expected {[1, 8, 64]}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = cubeElements([1, 2, 3, 4, 0])
        assert result == [1, 8, 27, 64, 0], f"Test 38 failed: got {result}, expected {[1, 8, 27, 64, 0]}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = cubeElements([2, 2, 3, -2147483648])
        assert result == [8, 8, 27, -9903520314283042199192993792], f"Test 39 failed: got {result}, expected {[8, 8, 27, -9903520314283042199192993792]}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = cubeElements([1, 2, 0])
        assert result == [1, 8, 0], f"Test 40 failed: got {result}, expected {[1, 8, 0]}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = cubeElements([4, 3, 4])
        assert result == [64, 27, 64], f"Test 41 failed: got {result}, expected {[64, 27, 64]}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = cubeElements([999999999999999999, 4, 3, 2, 1])
        assert result == [999999999999999997000000000000000002999999999999999999, 64, 27, 8, 1], f"Test 42 failed: got {result}, expected {[999999999999999997000000000000000002999999999999999999, 64, 27, 8, 1]}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = cubeElements([1, 3, 4, 0, 0, 0])
        assert result == [1, 27, 64, 0, 0, 0], f"Test 43 failed: got {result}, expected {[1, 27, 64, 0, 0, 0]}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = cubeElements([-1, 2, 3, 4, 17])
        assert result == [-1, 8, 27, 64, 4913], f"Test 44 failed: got {result}, expected {[-1, 8, 27, 64, 4913]}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = cubeElements([1, 2, 0, 4, 0, 0])
        assert result == [1, 8, 0, 64, 0, 0], f"Test 45 failed: got {result}, expected {[1, 8, 0, 64, 0, 0]}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = cubeElements([-2, 3])
        assert result == [-8, 27], f"Test 46 failed: got {result}, expected {[-8, 27]}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = cubeElements([0, 1, -4, -1, 0])
        assert result == [0, 1, -64, -1, 0], f"Test 47 failed: got {result}, expected {[0, 1, -64, -1, 0]}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = cubeElements([-2, -1, 0])
        assert result == [-8, -1, 0], f"Test 48 failed: got {result}, expected {[-8, -1, 0]}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = cubeElements([-1, 10000, 64, 3, 0, 0])
        assert result == [-1, 1000000000000, 262144, 27, 0, 0], f"Test 49 failed: got {result}, expected {[-1, 1000000000000, 262144, 27, 0, 0]}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = cubeElements([0, -1, -2, 3, -1000000000000000000000000, 0, -33])
        assert result == [0, -1, -8, 27, -1000000000000000000000000000000000000000000000000000000000000000000000000, 0, -35937], f"Test 50 failed: got {result}, expected {[0, -1, -8, 27, -1000000000000000000000000000000000000000000000000000000000000000000000000, 0, -35937]}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = cubeElements([10000, -2, -1, 0, 27])
        assert result == [1000000000000, -8, -1, 0, 19683], f"Test 51 failed: got {result}, expected {[1000000000000, -8, -1, 0, 19683]}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = cubeElements([0, -1, -2, 111111111])
        assert result == [0, -1, -8, 1371742108367626890260631], f"Test 52 failed: got {result}, expected {[0, -1, -8, 1371742108367626890260631]}"
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
