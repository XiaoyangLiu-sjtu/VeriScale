# Coverage Report

Total executable lines: 4
Covered lines: 4
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def sumAndAverage(n):
2: ✓     total = n * (n + 1) // 2
3: ✓     average = total / n
4: ✓     return total, average
```

## Complete Test File

```python
def sumAndAverage(n):
    total = n * (n + 1) // 2
    average = total / n
    return total, average

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = sumAndAverage(5)
        assert result == (15, 3.0), f"Test 1 failed: got {result}, expected {(15, 3.0)}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = sumAndAverage(1)
        assert result == (1, 1.0), f"Test 2 failed: got {result}, expected {(1, 1.0)}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = sumAndAverage(10)
        assert result == (55, 5.5), f"Test 3 failed: got {result}, expected {(55, 5.5)}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = sumAndAverage(2)
        assert result == (3, 1.5), f"Test 4 failed: got {result}, expected {(3, 1.5)}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = sumAndAverage(3)
        assert result == (6, 2.0), f"Test 5 failed: got {result}, expected {(6, 2.0)}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = sumAndAverage(4)
        assert result == (10, 2.5), f"Test 6 failed: got {result}, expected {(10, 2.5)}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = sumAndAverage(16)
        assert result == (136, 8.5), f"Test 7 failed: got {result}, expected {(136, 8.5)}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = sumAndAverage(31)
        assert result == (496, 16.0), f"Test 8 failed: got {result}, expected {(496, 16.0)}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = sumAndAverage(32)
        assert result == (528, 16.5), f"Test 9 failed: got {result}, expected {(528, 16.5)}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = sumAndAverage(33)
        assert result == (561, 17.0), f"Test 10 failed: got {result}, expected {(561, 17.0)}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = sumAndAverage(63)
        assert result == (2016, 32.0), f"Test 11 failed: got {result}, expected {(2016, 32.0)}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = sumAndAverage(64)
        assert result == (2080, 32.5), f"Test 12 failed: got {result}, expected {(2080, 32.5)}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = sumAndAverage(65)
        assert result == (2145, 33.0), f"Test 13 failed: got {result}, expected {(2145, 33.0)}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = sumAndAverage(99)
        assert result == (4950, 50.0), f"Test 14 failed: got {result}, expected {(4950, 50.0)}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = sumAndAverage(100)
        assert result == (5050, 50.5), f"Test 15 failed: got {result}, expected {(5050, 50.5)}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = sumAndAverage(101)
        assert result == (5151, 51.0), f"Test 16 failed: got {result}, expected {(5151, 51.0)}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = sumAndAverage(255)
        assert result == (32640, 128.0), f"Test 17 failed: got {result}, expected {(32640, 128.0)}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = sumAndAverage(256)
        assert result == (32896, 128.5), f"Test 18 failed: got {result}, expected {(32896, 128.5)}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = sumAndAverage(257)
        assert result == (33153, 129.0), f"Test 19 failed: got {result}, expected {(33153, 129.0)}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = sumAndAverage(999)
        assert result == (499500, 500.0), f"Test 20 failed: got {result}, expected {(499500, 500.0)}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = sumAndAverage(1000)
        assert result == (500500, 500.5), f"Test 21 failed: got {result}, expected {(500500, 500.5)}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = sumAndAverage(1024)
        assert result == (524800, 512.5), f"Test 22 failed: got {result}, expected {(524800, 512.5)}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = sumAndAverage(4096)
        assert result == (8390656, 2048.5), f"Test 23 failed: got {result}, expected {(8390656, 2048.5)}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = sumAndAverage(65535)
        assert result == (2147450880, 32768.0), f"Test 24 failed: got {result}, expected {(2147450880, 32768.0)}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = sumAndAverage(65536)
        assert result == (2147516416, 32768.5), f"Test 25 failed: got {result}, expected {(2147516416, 32768.5)}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = sumAndAverage(6)
        assert result == (21, 3.5), f"Test 26 failed: got {result}, expected {(21, 3.5)}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = sumAndAverage(11)
        assert result == (66, 6.0), f"Test 27 failed: got {result}, expected {(66, 6.0)}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = sumAndAverage(998)
        assert result == (498501, 499.5), f"Test 28 failed: got {result}, expected {(498501, 499.5)}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = sumAndAverage(251)
        assert result == (31626, 126.0), f"Test 29 failed: got {result}, expected {(31626, 126.0)}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = sumAndAverage(4097)
        assert result == (8394753, 2049.0), f"Test 30 failed: got {result}, expected {(8394753, 2049.0)}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = sumAndAverage(253)
        assert result == (32131, 127.0), f"Test 31 failed: got {result}, expected {(32131, 127.0)}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = sumAndAverage(12)
        assert result == (78, 6.5), f"Test 32 failed: got {result}, expected {(78, 6.5)}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = sumAndAverage(20)
        assert result == (210, 10.5), f"Test 33 failed: got {result}, expected {(210, 10.5)}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = sumAndAverage(510)
        assert result == (130305, 255.5), f"Test 34 failed: got {result}, expected {(130305, 255.5)}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = sumAndAverage(1995)
        assert result == (1991010, 998.0), f"Test 35 failed: got {result}, expected {(1991010, 998.0)}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = sumAndAverage(15)
        assert result == (120, 8.0), f"Test 36 failed: got {result}, expected {(120, 8.0)}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = sumAndAverage(17)
        assert result == (153, 9.0), f"Test 37 failed: got {result}, expected {(153, 9.0)}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = sumAndAverage(36)
        assert result == (666, 18.5), f"Test 38 failed: got {result}, expected {(666, 18.5)}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = sumAndAverage(39)
        assert result == (780, 20.0), f"Test 39 failed: got {result}, expected {(780, 20.0)}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = sumAndAverage(1994)
        assert result == (1989015, 997.5), f"Test 40 failed: got {result}, expected {(1989015, 997.5)}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = sumAndAverage(34)
        assert result == (595, 17.5), f"Test 41 failed: got {result}, expected {(595, 17.5)}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = sumAndAverage(252)
        assert result == (31878, 126.5), f"Test 42 failed: got {result}, expected {(31878, 126.5)}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = sumAndAverage(250)
        assert result == (31375, 125.5), f"Test 43 failed: got {result}, expected {(31375, 125.5)}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = sumAndAverage(102)
        assert result == (5253, 51.5), f"Test 44 failed: got {result}, expected {(5253, 51.5)}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = sumAndAverage(129)
        assert result == (8385, 65.0), f"Test 45 failed: got {result}, expected {(8385, 65.0)}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = sumAndAverage(1998)
        assert result == (1997001, 999.5), f"Test 46 failed: got {result}, expected {(1997001, 999.5)}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = sumAndAverage(202)
        assert result == (20503, 101.5), f"Test 47 failed: got {result}, expected {(20503, 101.5)}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = sumAndAverage(512)
        assert result == (131328, 256.5), f"Test 48 failed: got {result}, expected {(131328, 256.5)}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = sumAndAverage(21)
        assert result == (231, 11.0), f"Test 49 failed: got {result}, expected {(231, 11.0)}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = sumAndAverage(1001)
        assert result == (501501, 501.0), f"Test 50 failed: got {result}, expected {(501501, 501.0)}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = sumAndAverage(1025)
        assert result == (525825, 513.0), f"Test 51 failed: got {result}, expected {(525825, 513.0)}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = sumAndAverage(2000)
        assert result == (2001000, 1000.5), f"Test 52 failed: got {result}, expected {(2001000, 1000.5)}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = sumAndAverage(8192)
        assert result == (33558528, 4096.5), f"Test 53 failed: got {result}, expected {(33558528, 4096.5)}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = sumAndAverage(62)
        assert result == (1953, 31.5), f"Test 54 failed: got {result}, expected {(1953, 31.5)}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = sumAndAverage(8)
        assert result == (36, 4.5), f"Test 55 failed: got {result}, expected {(36, 4.5)}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = sumAndAverage(65534)
        assert result == (2147385345, 32767.5), f"Test 56 failed: got {result}, expected {(2147385345, 32767.5)}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = sumAndAverage(131072)
        assert result == (8590000128, 65536.5), f"Test 57 failed: got {result}, expected {(8590000128, 65536.5)}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = sumAndAverage(7)
        assert result == (28, 4.0), f"Test 58 failed: got {result}, expected {(28, 4.0)}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = sumAndAverage(68)
        assert result == (2346, 34.5), f"Test 59 failed: got {result}, expected {(2346, 34.5)}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = sumAndAverage(204)
        assert result == (20910, 102.5), f"Test 60 failed: got {result}, expected {(20910, 102.5)}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = sumAndAverage(67)
        assert result == (2278, 34.0), f"Test 61 failed: got {result}, expected {(2278, 34.0)}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = sumAndAverage(131074)
        assert result == (8590262275, 65537.5), f"Test 62 failed: got {result}, expected {(8590262275, 65537.5)}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
