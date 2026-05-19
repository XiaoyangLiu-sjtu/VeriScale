# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def SwapBitvectors(X, Y):
2: ✓     return (Y, X)
```

## Complete Test File

```python
def SwapBitvectors(X, Y):
    return (Y, X)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = SwapBitvectors(0, 0)
        assert result == (0, 0), f"Test 1 failed: got {result}, expected {(0, 0)}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = SwapBitvectors(5, 10)
        assert result == (10, 5), f"Test 2 failed: got {result}, expected {(10, 5)}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = SwapBitvectors(255, 1)
        assert result == (1, 255), f"Test 3 failed: got {result}, expected {(1, 255)}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = SwapBitvectors(128, 64)
        assert result == (64, 128), f"Test 4 failed: got {result}, expected {(64, 128)}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = SwapBitvectors(15, 15)
        assert result == (15, 15), f"Test 5 failed: got {result}, expected {(15, 15)}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = SwapBitvectors(0, 255)
        assert result == (255, 0), f"Test 6 failed: got {result}, expected {(255, 0)}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = SwapBitvectors(255, 0)
        assert result == (0, 255), f"Test 7 failed: got {result}, expected {(0, 255)}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = SwapBitvectors(255, 255)
        assert result == (255, 255), f"Test 8 failed: got {result}, expected {(255, 255)}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = SwapBitvectors(1, 0)
        assert result == (0, 1), f"Test 9 failed: got {result}, expected {(0, 1)}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = SwapBitvectors(0, 1)
        assert result == (1, 0), f"Test 10 failed: got {result}, expected {(1, 0)}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = SwapBitvectors(1, 255)
        assert result == (255, 1), f"Test 11 failed: got {result}, expected {(255, 1)}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = SwapBitvectors(127, 128)
        assert result == (128, 127), f"Test 12 failed: got {result}, expected {(128, 127)}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = SwapBitvectors(128, 127)
        assert result == (127, 128), f"Test 13 failed: got {result}, expected {(127, 128)}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = SwapBitvectors(128, 128)
        assert result == (128, 128), f"Test 14 failed: got {result}, expected {(128, 128)}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = SwapBitvectors(127, 127)
        assert result == (127, 127), f"Test 15 failed: got {result}, expected {(127, 127)}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = SwapBitvectors(16, 15)
        assert result == (15, 16), f"Test 16 failed: got {result}, expected {(15, 16)}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = SwapBitvectors(15, 16)
        assert result == (16, 15), f"Test 17 failed: got {result}, expected {(16, 15)}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = SwapBitvectors(64, 32)
        assert result == (32, 64), f"Test 18 failed: got {result}, expected {(32, 64)}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = SwapBitvectors(32, 64)
        assert result == (64, 32), f"Test 19 failed: got {result}, expected {(64, 32)}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = SwapBitvectors(170, 85)
        assert result == (85, 170), f"Test 20 failed: got {result}, expected {(85, 170)}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = SwapBitvectors(85, 170)
        assert result == (170, 85), f"Test 21 failed: got {result}, expected {(170, 85)}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = SwapBitvectors(204, 51)
        assert result == (51, 204), f"Test 22 failed: got {result}, expected {(51, 204)}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = SwapBitvectors(51, 204)
        assert result == (204, 51), f"Test 23 failed: got {result}, expected {(204, 51)}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = SwapBitvectors(254, 255)
        assert result == (255, 254), f"Test 24 failed: got {result}, expected {(255, 254)}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = SwapBitvectors(255, 254)
        assert result == (254, 255), f"Test 25 failed: got {result}, expected {(254, 255)}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = SwapBitvectors(2, 3)
        assert result == (3, 2), f"Test 26 failed: got {result}, expected {(3, 2)}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = SwapBitvectors(3, 2)
        assert result == (2, 3), f"Test 27 failed: got {result}, expected {(2, 3)}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = SwapBitvectors(42, 42)
        assert result == (42, 42), f"Test 28 failed: got {result}, expected {(42, 42)}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = SwapBitvectors(99, 100)
        assert result == (100, 99), f"Test 29 failed: got {result}, expected {(100, 99)}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = SwapBitvectors(100, 99)
        assert result == (99, 100), f"Test 30 failed: got {result}, expected {(99, 100)}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = SwapBitvectors(200, 55)
        assert result == (55, 200), f"Test 31 failed: got {result}, expected {(55, 200)}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = SwapBitvectors(55, 200)
        assert result == (200, 55), f"Test 32 failed: got {result}, expected {(200, 55)}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = SwapBitvectors(13, 240)
        assert result == (240, 13), f"Test 33 failed: got {result}, expected {(240, 13)}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = SwapBitvectors(240, 13)
        assert result == (13, 240), f"Test 34 failed: got {result}, expected {(13, 240)}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = SwapBitvectors(250, 5)
        assert result == (5, 250), f"Test 35 failed: got {result}, expected {(5, 250)}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = SwapBitvectors(5, 250)
        assert result == (250, 5), f"Test 36 failed: got {result}, expected {(250, 5)}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = SwapBitvectors(111, 222)
        assert result == (222, 111), f"Test 37 failed: got {result}, expected {(222, 111)}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = SwapBitvectors(222, 111)
        assert result == (111, 222), f"Test 38 failed: got {result}, expected {(111, 222)}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = SwapBitvectors(73, 146)
        assert result == (146, 73), f"Test 39 failed: got {result}, expected {(146, 73)}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = SwapBitvectors(146, 73)
        assert result == (73, 146), f"Test 40 failed: got {result}, expected {(73, 146)}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = SwapBitvectors(37, 218)
        assert result == (218, 37), f"Test 41 failed: got {result}, expected {(218, 37)}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = SwapBitvectors(218, 37)
        assert result == (37, 218), f"Test 42 failed: got {result}, expected {(37, 218)}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = SwapBitvectors(0, 204)
        assert result == (204, 0), f"Test 43 failed: got {result}, expected {(204, 0)}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = SwapBitvectors(0, 73)
        assert result == (73, 0), f"Test 44 failed: got {result}, expected {(73, 0)}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = SwapBitvectors(0, 13)
        assert result == (13, 0), f"Test 45 failed: got {result}, expected {(13, 0)}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = SwapBitvectors(16, 51)
        assert result == (51, 16), f"Test 46 failed: got {result}, expected {(51, 16)}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = SwapBitvectors(100, 0)
        assert result == (0, 100), f"Test 47 failed: got {result}, expected {(0, 100)}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = SwapBitvectors(254, 10)
        assert result == (10, 254), f"Test 48 failed: got {result}, expected {(10, 254)}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = SwapBitvectors(254, 4)
        assert result == (4, 254), f"Test 49 failed: got {result}, expected {(4, 254)}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = SwapBitvectors(11, 55)
        assert result == (55, 11), f"Test 50 failed: got {result}, expected {(55, 11)}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = SwapBitvectors(9, 9)
        assert result == (9, 9), f"Test 51 failed: got {result}, expected {(9, 9)}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = SwapBitvectors(6, 10)
        assert result == (10, 6), f"Test 52 failed: got {result}, expected {(10, 6)}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = SwapBitvectors(4, 217)
        assert result == (217, 4), f"Test 53 failed: got {result}, expected {(217, 4)}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = SwapBitvectors(6, 2)
        assert result == (2, 6), f"Test 54 failed: got {result}, expected {(2, 6)}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = SwapBitvectors(12, 8)
        assert result == (8, 12), f"Test 55 failed: got {result}, expected {(8, 12)}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = SwapBitvectors(5, 9)
        assert result == (9, 5), f"Test 56 failed: got {result}, expected {(9, 5)}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = SwapBitvectors(0, 3)
        assert result == (3, 0), f"Test 57 failed: got {result}, expected {(3, 0)}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = SwapBitvectors(510, 0)
        assert result == (0, 254), f"Test 58 failed: got {result}, expected {(0, 254)}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = SwapBitvectors(510, 1)
        assert result == (1, 254), f"Test 59 failed: got {result}, expected {(1, 254)}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = SwapBitvectors(254, 2)
        assert result == (2, 254), f"Test 60 failed: got {result}, expected {(2, 254)}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = SwapBitvectors(256, 2)
        assert result == (2, 0), f"Test 61 failed: got {result}, expected {(2, 0)}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = SwapBitvectors(250, 15)
        assert result == (15, 250), f"Test 62 failed: got {result}, expected {(15, 250)}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = SwapBitvectors(255, 73)
        assert result == (73, 255), f"Test 63 failed: got {result}, expected {(73, 255)}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = SwapBitvectors(250, 36)
        assert result == (36, 250), f"Test 64 failed: got {result}, expected {(36, 250)}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = SwapBitvectors(51, 0)
        assert result == (0, 51), f"Test 65 failed: got {result}, expected {(0, 51)}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = SwapBitvectors(258, 0)
        assert result == (0, 2), f"Test 66 failed: got {result}, expected {(0, 2)}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = SwapBitvectors(130, 0)
        assert result == (0, 130), f"Test 67 failed: got {result}, expected {(0, 130)}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = SwapBitvectors(260, 42)
        assert result == (42, 4), f"Test 68 failed: got {result}, expected {(42, 4)}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = SwapBitvectors(253, 64)
        assert result == (64, 253), f"Test 69 failed: got {result}, expected {(64, 253)}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = SwapBitvectors(55, 64)
        assert result == (64, 55), f"Test 70 failed: got {result}, expected {(64, 55)}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = SwapBitvectors(256, 64)
        assert result == (64, 0), f"Test 71 failed: got {result}, expected {(64, 0)}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = SwapBitvectors(0, 218)
        assert result == (218, 0), f"Test 72 failed: got {result}, expected {(218, 0)}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = SwapBitvectors(257, 13)
        assert result == (13, 1), f"Test 73 failed: got {result}, expected {(13, 1)}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = SwapBitvectors(111, 66)
        assert result == (66, 111), f"Test 74 failed: got {result}, expected {(66, 111)}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = SwapBitvectors(128, 0)
        assert result == (0, 128), f"Test 75 failed: got {result}, expected {(0, 128)}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = SwapBitvectors(111, 4)
        assert result == (4, 111), f"Test 76 failed: got {result}, expected {(4, 111)}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = SwapBitvectors(15, 64)
        assert result == (64, 15), f"Test 77 failed: got {result}, expected {(64, 15)}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = SwapBitvectors(16, 0)
        assert result == (0, 16), f"Test 78 failed: got {result}, expected {(0, 16)}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = SwapBitvectors(17, 15)
        assert result == (15, 17), f"Test 79 failed: got {result}, expected {(15, 17)}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = SwapBitvectors(66, 15)
        assert result == (15, 66), f"Test 80 failed: got {result}, expected {(15, 66)}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = SwapBitvectors(0, 16)
        assert result == (16, 0), f"Test 81 failed: got {result}, expected {(16, 0)}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = SwapBitvectors(14, 12)
        assert result == (12, 14), f"Test 82 failed: got {result}, expected {(12, 14)}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = SwapBitvectors(31, 0)
        assert result == (0, 31), f"Test 83 failed: got {result}, expected {(0, 31)}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = SwapBitvectors(200, 15)
        assert result == (15, 200), f"Test 84 failed: got {result}, expected {(15, 200)}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = SwapBitvectors(37, 0)
        assert result == (0, 37), f"Test 85 failed: got {result}, expected {(0, 37)}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = SwapBitvectors(0, 12)
        assert result == (12, 0), f"Test 86 failed: got {result}, expected {(12, 0)}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = SwapBitvectors(0, 146)
        assert result == (146, 0), f"Test 87 failed: got {result}, expected {(146, 0)}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = SwapBitvectors(2, 512)
        assert result == (0, 2), f"Test 88 failed: got {result}, expected {(0, 2)}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = SwapBitvectors(0, 2)
        assert result == (2, 0), f"Test 89 failed: got {result}, expected {(2, 0)}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = SwapBitvectors(0, 256)
        assert result == (0, 0), f"Test 90 failed: got {result}, expected {(0, 0)}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = SwapBitvectors(86, 255)
        assert result == (255, 86), f"Test 91 failed: got {result}, expected {(255, 86)}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = SwapBitvectors(255, 510)
        assert result == (254, 255), f"Test 92 failed: got {result}, expected {(254, 255)}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = SwapBitvectors(255, 511)
        assert result == (255, 255), f"Test 93 failed: got {result}, expected {(255, 255)}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = SwapBitvectors(32, 1)
        assert result == (1, 32), f"Test 94 failed: got {result}, expected {(1, 32)}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = SwapBitvectors(256, 0)
        assert result == (0, 0), f"Test 95 failed: got {result}, expected {(0, 0)}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = SwapBitvectors(99, 42)
        assert result == (42, 99), f"Test 96 failed: got {result}, expected {(42, 99)}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = SwapBitvectors(255, 10)
        assert result == (10, 255), f"Test 97 failed: got {result}, expected {(10, 255)}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = SwapBitvectors(255, 201)
        assert result == (201, 255), f"Test 98 failed: got {result}, expected {(201, 255)}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = SwapBitvectors(256, 255)
        assert result == (255, 0), f"Test 99 failed: got {result}, expected {(255, 0)}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = SwapBitvectors(253, 255)
        assert result == (255, 253), f"Test 100 failed: got {result}, expected {(255, 253)}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = SwapBitvectors(249, 9)
        assert result == (9, 249), f"Test 101 failed: got {result}, expected {(9, 249)}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = SwapBitvectors(0, 257)
        assert result == (1, 0), f"Test 102 failed: got {result}, expected {(1, 0)}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = SwapBitvectors(146, 258)
        assert result == (2, 146), f"Test 103 failed: got {result}, expected {(2, 146)}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = SwapBitvectors(1, 6)
        assert result == (6, 1), f"Test 104 failed: got {result}, expected {(6, 1)}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = SwapBitvectors(1, 11)
        assert result == (11, 1), f"Test 105 failed: got {result}, expected {(11, 1)}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = SwapBitvectors(1, 9)
        assert result == (9, 1), f"Test 106 failed: got {result}, expected {(9, 1)}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = SwapBitvectors(0, 1020)
        assert result == (252, 0), f"Test 107 failed: got {result}, expected {(252, 0)}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = SwapBitvectors(8, 0)
        assert result == (0, 8), f"Test 108 failed: got {result}, expected {(0, 8)}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = SwapBitvectors(1, 14)
        assert result == (14, 1), f"Test 109 failed: got {result}, expected {(14, 1)}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = SwapBitvectors(2, 0)
        assert result == (0, 2), f"Test 110 failed: got {result}, expected {(0, 2)}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    # Test case 111
    try:
        result = SwapBitvectors(0, 113)
        assert result == (113, 0), f"Test 111 failed: got {result}, expected {(113, 0)}"
        print(f"Test 111 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 111 failed: {e}")
        test_results.append(False)

    # Test case 112
    try:
        result = SwapBitvectors(0, 36)
        assert result == (36, 0), f"Test 112 failed: got {result}, expected {(36, 0)}"
        print(f"Test 112 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 112 failed: {e}")
        test_results.append(False)

    # Test case 113
    try:
        result = SwapBitvectors(0, 74)
        assert result == (74, 0), f"Test 113 failed: got {result}, expected {(74, 0)}"
        print(f"Test 113 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 113 failed: {e}")
        test_results.append(False)

    # Test case 114
    try:
        result = SwapBitvectors(1, 1)
        assert result == (1, 1), f"Test 114 failed: got {result}, expected {(1, 1)}"
        print(f"Test 114 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 114 failed: {e}")
        test_results.append(False)

    # Test case 115
    try:
        result = SwapBitvectors(5, 255)
        assert result == (255, 5), f"Test 115 failed: got {result}, expected {(255, 5)}"
        print(f"Test 115 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 115 failed: {e}")
        test_results.append(False)

    # Test case 116
    try:
        result = SwapBitvectors(2, 256)
        assert result == (0, 2), f"Test 116 failed: got {result}, expected {(0, 2)}"
        print(f"Test 116 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 116 failed: {e}")
        test_results.append(False)

    # Test case 117
    try:
        result = SwapBitvectors(1, 239)
        assert result == (239, 1), f"Test 117 failed: got {result}, expected {(239, 1)}"
        print(f"Test 117 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 117 failed: {e}")
        test_results.append(False)

    # Test case 118
    try:
        result = SwapBitvectors(1, 510)
        assert result == (254, 1), f"Test 118 failed: got {result}, expected {(254, 1)}"
        print(f"Test 118 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 118 failed: {e}")
        test_results.append(False)

    # Test case 119
    try:
        result = SwapBitvectors(1, 256)
        assert result == (0, 1), f"Test 119 failed: got {result}, expected {(0, 1)}"
        print(f"Test 119 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 119 failed: {e}")
        test_results.append(False)

    # Test case 120
    try:
        result = SwapBitvectors(0, 512)
        assert result == (0, 0), f"Test 120 failed: got {result}, expected {(0, 0)}"
        print(f"Test 120 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 120 failed: {e}")
        test_results.append(False)

    # Test case 121
    try:
        result = SwapBitvectors(2, 259)
        assert result == (3, 2), f"Test 121 failed: got {result}, expected {(3, 2)}"
        print(f"Test 121 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 121 failed: {e}")
        test_results.append(False)

    # Test case 122
    try:
        result = SwapBitvectors(9, 258)
        assert result == (2, 9), f"Test 122 failed: got {result}, expected {(2, 9)}"
        print(f"Test 122 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 122 failed: {e}")
        test_results.append(False)

    # Test case 123
    try:
        result = SwapBitvectors(1, 254)
        assert result == (254, 1), f"Test 123 failed: got {result}, expected {(254, 1)}"
        print(f"Test 123 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 123 failed: {e}")
        test_results.append(False)

    # Test case 124
    try:
        result = SwapBitvectors(170, 0)
        assert result == (0, 170), f"Test 124 failed: got {result}, expected {(0, 170)}"
        print(f"Test 124 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 124 failed: {e}")
        test_results.append(False)

    # Test case 125
    try:
        result = SwapBitvectors(127, 129)
        assert result == (129, 127), f"Test 125 failed: got {result}, expected {(129, 127)}"
        print(f"Test 125 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 125 failed: {e}")
        test_results.append(False)

    # Test case 126
    try:
        result = SwapBitvectors(126, 131)
        assert result == (131, 126), f"Test 126 failed: got {result}, expected {(131, 126)}"
        print(f"Test 126 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 126 failed: {e}")
        test_results.append(False)

    # Test case 127
    try:
        result = SwapBitvectors(250, 478)
        assert result == (222, 250), f"Test 127 failed: got {result}, expected {(222, 250)}"
        print(f"Test 127 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 127 failed: {e}")
        test_results.append(False)

    # Test case 128
    try:
        result = SwapBitvectors(86, 217)
        assert result == (217, 86), f"Test 128 failed: got {result}, expected {(217, 86)}"
        print(f"Test 128 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 128 failed: {e}")
        test_results.append(False)

    # Test case 129
    try:
        result = SwapBitvectors(222, 36)
        assert result == (36, 222), f"Test 129 failed: got {result}, expected {(36, 222)}"
        print(f"Test 129 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 129 failed: {e}")
        test_results.append(False)

    # Test case 130
    try:
        result = SwapBitvectors(127, 0)
        assert result == (0, 127), f"Test 130 failed: got {result}, expected {(0, 127)}"
        print(f"Test 130 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 130 failed: {e}")
        test_results.append(False)

    # Test case 131
    try:
        result = SwapBitvectors(129, 254)
        assert result == (254, 129), f"Test 131 failed: got {result}, expected {(254, 129)}"
        print(f"Test 131 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 131 failed: {e}")
        test_results.append(False)

    # Test case 132
    try:
        result = SwapBitvectors(128, 512)
        assert result == (0, 128), f"Test 132 failed: got {result}, expected {(0, 128)}"
        print(f"Test 132 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 132 failed: {e}")
        test_results.append(False)

    # Test case 133
    try:
        result = SwapBitvectors(258, 126)
        assert result == (126, 2), f"Test 133 failed: got {result}, expected {(126, 2)}"
        print(f"Test 133 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 133 failed: {e}")
        test_results.append(False)

    # Test case 134
    try:
        result = SwapBitvectors(129, 511)
        assert result == (255, 129), f"Test 134 failed: got {result}, expected {(255, 129)}"
        print(f"Test 134 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 134 failed: {e}")
        test_results.append(False)

    # Test case 135
    try:
        result = SwapBitvectors(1018, 0)
        assert result == (0, 250), f"Test 135 failed: got {result}, expected {(0, 250)}"
        print(f"Test 135 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 135 failed: {e}")
        test_results.append(False)

    # Test case 136
    try:
        result = SwapBitvectors(0, 128)
        assert result == (128, 0), f"Test 136 failed: got {result}, expected {(128, 0)}"
        print(f"Test 136 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 136 failed: {e}")
        test_results.append(False)

    # Test case 137
    try:
        result = SwapBitvectors(436, 127)
        assert result == (127, 180), f"Test 137 failed: got {result}, expected {(127, 180)}"
        print(f"Test 137 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 137 failed: {e}")
        test_results.append(False)

    # Test case 138
    try:
        result = SwapBitvectors(15, 1)
        assert result == (1, 15), f"Test 138 failed: got {result}, expected {(1, 15)}"
        print(f"Test 138 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 138 failed: {e}")
        test_results.append(False)

    # Test case 139
    try:
        result = SwapBitvectors(0, 129)
        assert result == (129, 0), f"Test 139 failed: got {result}, expected {(129, 0)}"
        print(f"Test 139 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 139 failed: {e}")
        test_results.append(False)

    # Test case 140
    try:
        result = SwapBitvectors(128, 260)
        assert result == (4, 128), f"Test 140 failed: got {result}, expected {(4, 128)}"
        print(f"Test 140 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 140 failed: {e}")
        test_results.append(False)

    # Test case 141
    try:
        result = SwapBitvectors(168, 128)
        assert result == (128, 168), f"Test 141 failed: got {result}, expected {(128, 168)}"
        print(f"Test 141 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 141 failed: {e}")
        test_results.append(False)

    # Test case 142
    try:
        result = SwapBitvectors(41, 0)
        assert result == (0, 41), f"Test 142 failed: got {result}, expected {(0, 41)}"
        print(f"Test 142 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 142 failed: {e}")
        test_results.append(False)

    # Test case 143
    try:
        result = SwapBitvectors(256, 129)
        assert result == (129, 0), f"Test 143 failed: got {result}, expected {(129, 0)}"
        print(f"Test 143 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 143 failed: {e}")
        test_results.append(False)

    # Test case 144
    try:
        result = SwapBitvectors(5, 128)
        assert result == (128, 5), f"Test 144 failed: got {result}, expected {(128, 5)}"
        print(f"Test 144 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 144 failed: {e}")
        test_results.append(False)

    # Test case 145
    try:
        result = SwapBitvectors(112, 127)
        assert result == (127, 112), f"Test 145 failed: got {result}, expected {(127, 112)}"
        print(f"Test 145 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 145 failed: {e}")
        test_results.append(False)

    # Test case 146
    try:
        result = SwapBitvectors(127, 64)
        assert result == (64, 127), f"Test 146 failed: got {result}, expected {(64, 127)}"
        print(f"Test 146 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 146 failed: {e}")
        test_results.append(False)

    # Test case 147
    try:
        result = SwapBitvectors(258, 128)
        assert result == (128, 2), f"Test 147 failed: got {result}, expected {(128, 2)}"
        print(f"Test 147 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 147 failed: {e}")
        test_results.append(False)

    # Test case 148
    try:
        result = SwapBitvectors(127, 1020)
        assert result == (252, 127), f"Test 148 failed: got {result}, expected {(252, 127)}"
        print(f"Test 148 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 148 failed: {e}")
        test_results.append(False)

    # Test case 149
    try:
        result = SwapBitvectors(14, 127)
        assert result == (127, 14), f"Test 149 failed: got {result}, expected {(127, 14)}"
        print(f"Test 149 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 149 failed: {e}")
        test_results.append(False)

    # Test case 150
    try:
        result = SwapBitvectors(127, 518)
        assert result == (6, 127), f"Test 150 failed: got {result}, expected {(6, 127)}"
        print(f"Test 150 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 150 failed: {e}")
        test_results.append(False)

    # Test case 151
    try:
        result = SwapBitvectors(126, 255)
        assert result == (255, 126), f"Test 151 failed: got {result}, expected {(255, 126)}"
        print(f"Test 151 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 151 failed: {e}")
        test_results.append(False)

    # Test case 152
    try:
        result = SwapBitvectors(126, 128)
        assert result == (128, 126), f"Test 152 failed: got {result}, expected {(128, 126)}"
        print(f"Test 152 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 152 failed: {e}")
        test_results.append(False)

    # Test case 153
    try:
        result = SwapBitvectors(16, 204)
        assert result == (204, 16), f"Test 153 failed: got {result}, expected {(204, 16)}"
        print(f"Test 153 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 153 failed: {e}")
        test_results.append(False)

    # Test case 154
    try:
        result = SwapBitvectors(0, 17)
        assert result == (17, 0), f"Test 154 failed: got {result}, expected {(17, 0)}"
        print(f"Test 154 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 154 failed: {e}")
        test_results.append(False)

    # Test case 155
    try:
        result = SwapBitvectors(126, 10)
        assert result == (10, 126), f"Test 155 failed: got {result}, expected {(10, 126)}"
        print(f"Test 155 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 155 failed: {e}")
        test_results.append(False)

    # Test case 156
    try:
        result = SwapBitvectors(16, 239)
        assert result == (239, 16), f"Test 156 failed: got {result}, expected {(239, 16)}"
        print(f"Test 156 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 156 failed: {e}")
        test_results.append(False)

    # Test case 157
    try:
        result = SwapBitvectors(17, 30)
        assert result == (30, 17), f"Test 157 failed: got {result}, expected {(30, 17)}"
        print(f"Test 157 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 157 failed: {e}")
        test_results.append(False)

    # Test case 158
    try:
        result = SwapBitvectors(168, 15)
        assert result == (15, 168), f"Test 158 failed: got {result}, expected {(15, 168)}"
        print(f"Test 158 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 158 failed: {e}")
        test_results.append(False)

    # Test case 159
    try:
        result = SwapBitvectors(17, 11)
        assert result == (11, 17), f"Test 159 failed: got {result}, expected {(11, 17)}"
        print(f"Test 159 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 159 failed: {e}")
        test_results.append(False)

    # Test case 160
    try:
        result = SwapBitvectors(32, 203)
        assert result == (203, 32), f"Test 160 failed: got {result}, expected {(203, 32)}"
        print(f"Test 160 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 160 failed: {e}")
        test_results.append(False)

    # Test case 161
    try:
        result = SwapBitvectors(15, 66)
        assert result == (66, 15), f"Test 161 failed: got {result}, expected {(66, 15)}"
        print(f"Test 161 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 161 failed: {e}")
        test_results.append(False)

    # Test case 162
    try:
        result = SwapBitvectors(0, 15)
        assert result == (15, 0), f"Test 162 failed: got {result}, expected {(15, 0)}"
        print(f"Test 162 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 162 failed: {e}")
        test_results.append(False)

    # Test case 163
    try:
        result = SwapBitvectors(18, 17)
        assert result == (17, 18), f"Test 163 failed: got {result}, expected {(17, 18)}"
        print(f"Test 163 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 163 failed: {e}")
        test_results.append(False)

    # Test case 164
    try:
        result = SwapBitvectors(14, 18)
        assert result == (18, 14), f"Test 164 failed: got {result}, expected {(18, 14)}"
        print(f"Test 164 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 164 failed: {e}")
        test_results.append(False)

    # Test case 165
    try:
        result = SwapBitvectors(250, 35)
        assert result == (35, 250), f"Test 165 failed: got {result}, expected {(35, 250)}"
        print(f"Test 165 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 165 failed: {e}")
        test_results.append(False)

    # Test case 166
    try:
        result = SwapBitvectors(128, 33)
        assert result == (33, 128), f"Test 166 failed: got {result}, expected {(33, 128)}"
        print(f"Test 166 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 166 failed: {e}")
        test_results.append(False)

    # Test case 167
    try:
        result = SwapBitvectors(1, 32)
        assert result == (32, 1), f"Test 167 failed: got {result}, expected {(32, 1)}"
        print(f"Test 167 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 167 failed: {e}")
        test_results.append(False)

    # Test case 168
    try:
        result = SwapBitvectors(0, 32)
        assert result == (32, 0), f"Test 168 failed: got {result}, expected {(32, 0)}"
        print(f"Test 168 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 168 failed: {e}")
        test_results.append(False)

    # Test case 169
    try:
        result = SwapBitvectors(130, 260)
        assert result == (4, 130), f"Test 169 failed: got {result}, expected {(4, 130)}"
        print(f"Test 169 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 169 failed: {e}")
        test_results.append(False)

    # Test case 170
    try:
        result = SwapBitvectors(66, 32)
        assert result == (32, 66), f"Test 170 failed: got {result}, expected {(32, 66)}"
        print(f"Test 170 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 170 failed: {e}")
        test_results.append(False)

    # Test case 171
    try:
        result = SwapBitvectors(64, 219)
        assert result == (219, 64), f"Test 171 failed: got {result}, expected {(219, 64)}"
        print(f"Test 171 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 171 failed: {e}")
        test_results.append(False)

    # Test case 172
    try:
        result = SwapBitvectors(64, 64)
        assert result == (64, 64), f"Test 172 failed: got {result}, expected {(64, 64)}"
        print(f"Test 172 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 172 failed: {e}")
        test_results.append(False)

    # Test case 173
    try:
        result = SwapBitvectors(1, 34)
        assert result == (34, 1), f"Test 173 failed: got {result}, expected {(34, 1)}"
        print(f"Test 173 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 173 failed: {e}")
        test_results.append(False)

    # Test case 174
    try:
        result = SwapBitvectors(64, 17)
        assert result == (17, 64), f"Test 174 failed: got {result}, expected {(17, 64)}"
        print(f"Test 174 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 174 failed: {e}")
        test_results.append(False)

    # Test case 175
    try:
        result = SwapBitvectors(65, 33)
        assert result == (33, 65), f"Test 175 failed: got {result}, expected {(33, 65)}"
        print(f"Test 175 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 175 failed: {e}")
        test_results.append(False)

    # Test case 176
    try:
        result = SwapBitvectors(30, 128)
        assert result == (128, 30), f"Test 176 failed: got {result}, expected {(128, 30)}"
        print(f"Test 176 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 176 failed: {e}")
        test_results.append(False)

    # Test case 177
    try:
        result = SwapBitvectors(64, 0)
        assert result == (0, 64), f"Test 177 failed: got {result}, expected {(0, 64)}"
        print(f"Test 177 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 177 failed: {e}")
        test_results.append(False)

    # Test case 178
    try:
        result = SwapBitvectors(0, 33)
        assert result == (33, 0), f"Test 178 failed: got {result}, expected {(33, 0)}"
        print(f"Test 178 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 178 failed: {e}")
        test_results.append(False)

    # Test case 179
    try:
        result = SwapBitvectors(32, 126)
        assert result == (126, 32), f"Test 179 failed: got {result}, expected {(126, 32)}"
        print(f"Test 179 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 179 failed: {e}")
        test_results.append(False)

    # Test case 180
    try:
        result = SwapBitvectors(62, 64)
        assert result == (64, 62), f"Test 180 failed: got {result}, expected {(64, 62)}"
        print(f"Test 180 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 180 failed: {e}")
        test_results.append(False)

    # Test case 181
    try:
        result = SwapBitvectors(31, 64)
        assert result == (64, 31), f"Test 181 failed: got {result}, expected {(64, 31)}"
        print(f"Test 181 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 181 failed: {e}")
        test_results.append(False)

    # Test case 182
    try:
        result = SwapBitvectors(33, 62)
        assert result == (62, 33), f"Test 182 failed: got {result}, expected {(62, 33)}"
        print(f"Test 182 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 182 failed: {e}")
        test_results.append(False)

    # Test case 183
    try:
        result = SwapBitvectors(11, 64)
        assert result == (64, 11), f"Test 183 failed: got {result}, expected {(64, 11)}"
        print(f"Test 183 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 183 failed: {e}")
        test_results.append(False)

    # Test case 184
    try:
        result = SwapBitvectors(36, 83)
        assert result == (83, 36), f"Test 184 failed: got {result}, expected {(83, 36)}"
        print(f"Test 184 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 184 failed: {e}")
        test_results.append(False)

    # Test case 185
    try:
        result = SwapBitvectors(0, 85)
        assert result == (85, 0), f"Test 185 failed: got {result}, expected {(85, 0)}"
        print(f"Test 185 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 185 failed: {e}")
        test_results.append(False)

    # Test case 186
    try:
        result = SwapBitvectors(0, 84)
        assert result == (84, 0), f"Test 186 failed: got {result}, expected {(84, 0)}"
        print(f"Test 186 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 186 failed: {e}")
        test_results.append(False)

    # Test case 187
    try:
        result = SwapBitvectors(511, 260)
        assert result == (4, 255), f"Test 187 failed: got {result}, expected {(4, 255)}"
        print(f"Test 187 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 187 failed: {e}")
        test_results.append(False)

    # Test case 188
    try:
        result = SwapBitvectors(112, 16)
        assert result == (16, 112), f"Test 188 failed: got {result}, expected {(16, 112)}"
        print(f"Test 188 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 188 failed: {e}")
        test_results.append(False)

    # Test case 189
    try:
        result = SwapBitvectors(170, 9)
        assert result == (9, 170), f"Test 189 failed: got {result}, expected {(9, 170)}"
        print(f"Test 189 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 189 failed: {e}")
        test_results.append(False)

    # Test case 190
    try:
        result = SwapBitvectors(170, 170)
        assert result == (170, 170), f"Test 190 failed: got {result}, expected {(170, 170)}"
        print(f"Test 190 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 190 failed: {e}")
        test_results.append(False)

    # Test case 191
    try:
        result = SwapBitvectors(100, 85)
        assert result == (85, 100), f"Test 191 failed: got {result}, expected {(85, 100)}"
        print(f"Test 191 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 191 failed: {e}")
        test_results.append(False)

    # Test case 192
    try:
        result = SwapBitvectors(170, 66)
        assert result == (66, 170), f"Test 192 failed: got {result}, expected {(66, 170)}"
        print(f"Test 192 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 192 failed: {e}")
        test_results.append(False)

    # Test case 193
    try:
        result = SwapBitvectors(1, 169)
        assert result == (169, 1), f"Test 193 failed: got {result}, expected {(169, 1)}"
        print(f"Test 193 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 193 failed: {e}")
        test_results.append(False)

    # Test case 194
    try:
        result = SwapBitvectors(512, 171)
        assert result == (171, 0), f"Test 194 failed: got {result}, expected {(171, 0)}"
        print(f"Test 194 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 194 failed: {e}")
        test_results.append(False)

    # Test case 195
    try:
        result = SwapBitvectors(126, 169)
        assert result == (169, 126), f"Test 195 failed: got {result}, expected {(169, 126)}"
        print(f"Test 195 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 195 failed: {e}")
        test_results.append(False)

    # Test case 196
    try:
        result = SwapBitvectors(85, 168)
        assert result == (168, 85), f"Test 196 failed: got {result}, expected {(168, 85)}"
        print(f"Test 196 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 196 failed: {e}")
        test_results.append(False)

    # Test case 197
    try:
        result = SwapBitvectors(0, 170)
        assert result == (170, 0), f"Test 197 failed: got {result}, expected {(170, 0)}"
        print(f"Test 197 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 197 failed: {e}")
        test_results.append(False)

    # Test case 198
    try:
        result = SwapBitvectors(169, 170)
        assert result == (170, 169), f"Test 198 failed: got {result}, expected {(170, 169)}"
        print(f"Test 198 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 198 failed: {e}")
        test_results.append(False)

    # Test case 199
    try:
        result = SwapBitvectors(257, 35)
        assert result == (35, 1), f"Test 199 failed: got {result}, expected {(35, 1)}"
        print(f"Test 199 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 199 failed: {e}")
        test_results.append(False)

    # Test case 200
    try:
        result = SwapBitvectors(112, 0)
        assert result == (0, 112), f"Test 200 failed: got {result}, expected {(0, 112)}"
        print(f"Test 200 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 200 failed: {e}")
        test_results.append(False)

    # Test case 201
    try:
        result = SwapBitvectors(204, 102)
        assert result == (102, 204), f"Test 201 failed: got {result}, expected {(102, 204)}"
        print(f"Test 201 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 201 failed: {e}")
        test_results.append(False)

    # Test case 202
    try:
        result = SwapBitvectors(204, 52)
        assert result == (52, 204), f"Test 202 failed: got {result}, expected {(52, 204)}"
        print(f"Test 202 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 202 failed: {e}")
        test_results.append(False)

    # Test case 203
    try:
        result = SwapBitvectors(168, 50)
        assert result == (50, 168), f"Test 203 failed: got {result}, expected {(50, 168)}"
        print(f"Test 203 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 203 failed: {e}")
        test_results.append(False)

    # Test case 204
    try:
        result = SwapBitvectors(0, 51)
        assert result == (51, 0), f"Test 204 failed: got {result}, expected {(51, 0)}"
        print(f"Test 204 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 204 failed: {e}")
        test_results.append(False)

    # Test case 205
    try:
        result = SwapBitvectors(254, 9)
        assert result == (9, 254), f"Test 205 failed: got {result}, expected {(9, 254)}"
        print(f"Test 205 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 205 failed: {e}")
        test_results.append(False)

    # Test case 206
    try:
        result = SwapBitvectors(205, 62)
        assert result == (62, 205), f"Test 206 failed: got {result}, expected {(62, 205)}"
        print(f"Test 206 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 206 failed: {e}")
        test_results.append(False)

    # Test case 207
    try:
        result = SwapBitvectors(204, 0)
        assert result == (0, 204), f"Test 207 failed: got {result}, expected {(0, 204)}"
        print(f"Test 207 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 207 failed: {e}")
        test_results.append(False)

    # Test case 208
    try:
        result = SwapBitvectors(408, 50)
        assert result == (50, 152), f"Test 208 failed: got {result}, expected {(50, 152)}"
        print(f"Test 208 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 208 failed: {e}")
        test_results.append(False)

    # Test case 209
    try:
        result = SwapBitvectors(203, 51)
        assert result == (51, 203), f"Test 209 failed: got {result}, expected {(51, 203)}"
        print(f"Test 209 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 209 failed: {e}")
        test_results.append(False)

    # Test case 210
    try:
        result = SwapBitvectors(51, 171)
        assert result == (171, 51), f"Test 210 failed: got {result}, expected {(171, 51)}"
        print(f"Test 210 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 210 failed: {e}")
        test_results.append(False)

    # Test case 211
    try:
        result = SwapBitvectors(51, 99)
        assert result == (99, 51), f"Test 211 failed: got {result}, expected {(99, 51)}"
        print(f"Test 211 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 211 failed: {e}")
        test_results.append(False)

    # Test case 212
    try:
        result = SwapBitvectors(102, 408)
        assert result == (152, 102), f"Test 212 failed: got {result}, expected {(152, 102)}"
        print(f"Test 212 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 212 failed: {e}")
        test_results.append(False)

    # Test case 213
    try:
        result = SwapBitvectors(33, 202)
        assert result == (202, 33), f"Test 213 failed: got {result}, expected {(202, 33)}"
        print(f"Test 213 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 213 failed: {e}")
        test_results.append(False)

    # Test case 214
    try:
        result = SwapBitvectors(52, 203)
        assert result == (203, 52), f"Test 214 failed: got {result}, expected {(203, 52)}"
        print(f"Test 214 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 214 failed: {e}")
        test_results.append(False)

    # Test case 215
    try:
        result = SwapBitvectors(52, 204)
        assert result == (204, 52), f"Test 215 failed: got {result}, expected {(204, 52)}"
        print(f"Test 215 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 215 failed: {e}")
        test_results.append(False)

    # Test case 216
    try:
        result = SwapBitvectors(102, 202)
        assert result == (202, 102), f"Test 216 failed: got {result}, expected {(202, 102)}"
        print(f"Test 216 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 216 failed: {e}")
        test_results.append(False)

    # Test case 217
    try:
        result = SwapBitvectors(52, 63)
        assert result == (63, 52), f"Test 217 failed: got {result}, expected {(63, 52)}"
        print(f"Test 217 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 217 failed: {e}")
        test_results.append(False)

    # Test case 218
    try:
        result = SwapBitvectors(102, 239)
        assert result == (239, 102), f"Test 218 failed: got {result}, expected {(239, 102)}"
        print(f"Test 218 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 218 failed: {e}")
        test_results.append(False)

    # Test case 219
    try:
        result = SwapBitvectors(254, 481)
        assert result == (225, 254), f"Test 219 failed: got {result}, expected {(225, 254)}"
        print(f"Test 219 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 219 failed: {e}")
        test_results.append(False)

    # Test case 220
    try:
        result = SwapBitvectors(254, 406)
        assert result == (150, 254), f"Test 220 failed: got {result}, expected {(150, 254)}"
        print(f"Test 220 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 220 failed: {e}")
        test_results.append(False)

    # Test case 221
    try:
        result = SwapBitvectors(147, 254)
        assert result == (254, 147), f"Test 221 failed: got {result}, expected {(254, 147)}"
        print(f"Test 221 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 221 failed: {e}")
        test_results.append(False)

    # Test case 222
    try:
        result = SwapBitvectors(508, 0)
        assert result == (0, 252), f"Test 222 failed: got {result}, expected {(0, 252)}"
        print(f"Test 222 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 222 failed: {e}")
        test_results.append(False)

    # Test case 223
    try:
        result = SwapBitvectors(253, 254)
        assert result == (254, 253), f"Test 223 failed: got {result}, expected {(254, 253)}"
        print(f"Test 223 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 223 failed: {e}")
        test_results.append(False)

    # Test case 224
    try:
        result = SwapBitvectors(252, 254)
        assert result == (254, 252), f"Test 224 failed: got {result}, expected {(254, 252)}"
        print(f"Test 224 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 224 failed: {e}")
        test_results.append(False)

    # Test case 225
    try:
        result = SwapBitvectors(254, 0)
        assert result == (0, 254), f"Test 225 failed: got {result}, expected {(0, 254)}"
        print(f"Test 225 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 225 failed: {e}")
        test_results.append(False)

    # Test case 226
    try:
        result = SwapBitvectors(254, 254)
        assert result == (254, 254), f"Test 226 failed: got {result}, expected {(254, 254)}"
        print(f"Test 226 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 226 failed: {e}")
        test_results.append(False)

    # Test case 227
    try:
        result = SwapBitvectors(258, 254)
        assert result == (254, 2), f"Test 227 failed: got {result}, expected {(254, 2)}"
        print(f"Test 227 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 227 failed: {e}")
        test_results.append(False)

    # Test case 228
    try:
        result = SwapBitvectors(37, 510)
        assert result == (254, 37), f"Test 228 failed: got {result}, expected {(254, 37)}"
        print(f"Test 228 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 228 failed: {e}")
        test_results.append(False)

    # Test case 229
    try:
        result = SwapBitvectors(35, 816)
        assert result == (48, 35), f"Test 229 failed: got {result}, expected {(48, 35)}"
        print(f"Test 229 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 229 failed: {e}")
        test_results.append(False)

    # Test case 230
    try:
        result = SwapBitvectors(512, 253)
        assert result == (253, 0), f"Test 230 failed: got {result}, expected {(253, 0)}"
        print(f"Test 230 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 230 failed: {e}")
        test_results.append(False)

    # Test case 231
    try:
        result = SwapBitvectors(255, 253)
        assert result == (253, 255), f"Test 231 failed: got {result}, expected {(253, 255)}"
        print(f"Test 231 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 231 failed: {e}")
        test_results.append(False)

    # Test case 232
    try:
        result = SwapBitvectors(0, 252)
        assert result == (252, 0), f"Test 232 failed: got {result}, expected {(252, 0)}"
        print(f"Test 232 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 232 failed: {e}")
        test_results.append(False)

    # Test case 233
    try:
        result = SwapBitvectors(1, 3)
        assert result == (3, 1), f"Test 233 failed: got {result}, expected {(3, 1)}"
        print(f"Test 233 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 233 failed: {e}")
        test_results.append(False)

    # Test case 234
    try:
        result = SwapBitvectors(0, 510)
        assert result == (254, 0), f"Test 234 failed: got {result}, expected {(254, 0)}"
        print(f"Test 234 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 234 failed: {e}")
        test_results.append(False)

    # Test case 235
    try:
        result = SwapBitvectors(0, 481)
        assert result == (225, 0), f"Test 235 failed: got {result}, expected {(225, 0)}"
        print(f"Test 235 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 235 failed: {e}")
        test_results.append(False)

    # Test case 236
    try:
        result = SwapBitvectors(4, 3)
        assert result == (3, 4), f"Test 236 failed: got {result}, expected {(3, 4)}"
        print(f"Test 236 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 236 failed: {e}")
        test_results.append(False)

    # Test case 237
    try:
        result = SwapBitvectors(0, 4)
        assert result == (4, 0), f"Test 237 failed: got {result}, expected {(4, 0)}"
        print(f"Test 237 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 237 failed: {e}")
        test_results.append(False)

    # Test case 238
    try:
        result = SwapBitvectors(73, 254)
        assert result == (254, 73), f"Test 238 failed: got {result}, expected {(254, 73)}"
        print(f"Test 238 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 238 failed: {e}")
        test_results.append(False)

    # Test case 239
    try:
        result = SwapBitvectors(224, 102)
        assert result == (102, 224), f"Test 239 failed: got {result}, expected {(102, 224)}"
        print(f"Test 239 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 239 failed: {e}")
        test_results.append(False)

    # Test case 240
    try:
        result = SwapBitvectors(4, 2)
        assert result == (2, 4), f"Test 240 failed: got {result}, expected {(2, 4)}"
        print(f"Test 240 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 240 failed: {e}")
        test_results.append(False)

    # Test case 241
    try:
        result = SwapBitvectors(3, 4)
        assert result == (4, 3), f"Test 241 failed: got {result}, expected {(4, 3)}"
        print(f"Test 241 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 241 failed: {e}")
        test_results.append(False)

    # Test case 242
    try:
        result = SwapBitvectors(0, 202)
        assert result == (202, 0), f"Test 242 failed: got {result}, expected {(202, 0)}"
        print(f"Test 242 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 242 failed: {e}")
        test_results.append(False)

    # Test case 243
    try:
        result = SwapBitvectors(42, 40)
        assert result == (40, 42), f"Test 243 failed: got {result}, expected {(40, 42)}"
        print(f"Test 243 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 243 failed: {e}")
        test_results.append(False)

    # Test case 244
    try:
        result = SwapBitvectors(168, 42)
        assert result == (42, 168), f"Test 244 failed: got {result}, expected {(42, 168)}"
        print(f"Test 244 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 244 failed: {e}")
        test_results.append(False)

    # Test case 245
    try:
        result = SwapBitvectors(43, 42)
        assert result == (42, 43), f"Test 245 failed: got {result}, expected {(42, 43)}"
        print(f"Test 245 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 245 failed: {e}")
        test_results.append(False)

    # Test case 246
    try:
        result = SwapBitvectors(42, 84)
        assert result == (84, 42), f"Test 246 failed: got {result}, expected {(84, 42)}"
        print(f"Test 246 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 246 failed: {e}")
        test_results.append(False)

    # Test case 247
    try:
        result = SwapBitvectors(1, 44)
        assert result == (44, 1), f"Test 247 failed: got {result}, expected {(44, 1)}"
        print(f"Test 247 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 247 failed: {e}")
        test_results.append(False)

    # Test case 248
    try:
        result = SwapBitvectors(86, 148)
        assert result == (148, 86), f"Test 248 failed: got {result}, expected {(148, 86)}"
        print(f"Test 248 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 248 failed: {e}")
        test_results.append(False)

    # Test case 249
    try:
        result = SwapBitvectors(0, 42)
        assert result == (42, 0), f"Test 249 failed: got {result}, expected {(42, 0)}"
        print(f"Test 249 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 249 failed: {e}")
        test_results.append(False)

    # Test case 250
    try:
        result = SwapBitvectors(131, 0)
        assert result == (0, 131), f"Test 250 failed: got {result}, expected {(0, 131)}"
        print(f"Test 250 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 250 failed: {e}")
        test_results.append(False)

    # Test case 251
    try:
        result = SwapBitvectors(84, 256)
        assert result == (0, 84), f"Test 251 failed: got {result}, expected {(0, 84)}"
        print(f"Test 251 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 251 failed: {e}")
        test_results.append(False)

    # Test case 252
    try:
        result = SwapBitvectors(41, 42)
        assert result == (42, 41), f"Test 252 failed: got {result}, expected {(42, 41)}"
        print(f"Test 252 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 252 failed: {e}")
        test_results.append(False)

    # Test case 253
    try:
        result = SwapBitvectors(99, 101)
        assert result == (101, 99), f"Test 253 failed: got {result}, expected {(101, 99)}"
        print(f"Test 253 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 253 failed: {e}")
        test_results.append(False)

    # Test case 254
    try:
        result = SwapBitvectors(0, 100)
        assert result == (100, 0), f"Test 254 failed: got {result}, expected {(100, 0)}"
        print(f"Test 254 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 254 failed: {e}")
        test_results.append(False)

    # Test case 255
    try:
        result = SwapBitvectors(100, 100)
        assert result == (100, 100), f"Test 255 failed: got {result}, expected {(100, 100)}"
        print(f"Test 255 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 255 failed: {e}")
        test_results.append(False)

    # Test case 256
    try:
        result = SwapBitvectors(0, 83)
        assert result == (83, 0), f"Test 256 failed: got {result}, expected {(83, 0)}"
        print(f"Test 256 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 256 failed: {e}")
        test_results.append(False)

    # Test case 257
    try:
        result = SwapBitvectors(0, 11)
        assert result == (11, 0), f"Test 257 failed: got {result}, expected {(11, 0)}"
        print(f"Test 257 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 257 failed: {e}")
        test_results.append(False)

    # Test case 258
    try:
        result = SwapBitvectors(518, 100)
        assert result == (100, 6), f"Test 258 failed: got {result}, expected {(100, 6)}"
        print(f"Test 258 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 258 failed: {e}")
        test_results.append(False)

    # Test case 259
    try:
        result = SwapBitvectors(74, 100)
        assert result == (100, 74), f"Test 259 failed: got {result}, expected {(100, 74)}"
        print(f"Test 259 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 259 failed: {e}")
        test_results.append(False)

    # Test case 260
    try:
        result = SwapBitvectors(43, 101)
        assert result == (101, 43), f"Test 260 failed: got {result}, expected {(101, 43)}"
        print(f"Test 260 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 260 failed: {e}")
        test_results.append(False)

    # Test case 261
    try:
        result = SwapBitvectors(0, 199)
        assert result == (199, 0), f"Test 261 failed: got {result}, expected {(199, 0)}"
        print(f"Test 261 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 261 failed: {e}")
        test_results.append(False)

    # Test case 262
    try:
        result = SwapBitvectors(254, 99)
        assert result == (99, 254), f"Test 262 failed: got {result}, expected {(99, 254)}"
        print(f"Test 262 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 262 failed: {e}")
        test_results.append(False)

    # Test case 263
    try:
        result = SwapBitvectors(0, 99)
        assert result == (99, 0), f"Test 263 failed: got {result}, expected {(99, 0)}"
        print(f"Test 263 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 263 failed: {e}")
        test_results.append(False)

    # Test case 264
    try:
        result = SwapBitvectors(408, 198)
        assert result == (198, 152), f"Test 264 failed: got {result}, expected {(198, 152)}"
        print(f"Test 264 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 264 failed: {e}")
        test_results.append(False)

    # Test case 265
    try:
        result = SwapBitvectors(200, 198)
        assert result == (198, 200), f"Test 265 failed: got {result}, expected {(198, 200)}"
        print(f"Test 265 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 265 failed: {e}")
        test_results.append(False)

    # Test case 266
    try:
        result = SwapBitvectors(201, 35)
        assert result == (35, 201), f"Test 266 failed: got {result}, expected {(35, 201)}"
        print(f"Test 266 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 266 failed: {e}")
        test_results.append(False)

    # Test case 267
    try:
        result = SwapBitvectors(199, 55)
        assert result == (55, 199), f"Test 267 failed: got {result}, expected {(55, 199)}"
        print(f"Test 267 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 267 failed: {e}")
        test_results.append(False)

    # Test case 268
    try:
        result = SwapBitvectors(402, 57)
        assert result == (57, 146), f"Test 268 failed: got {result}, expected {(57, 146)}"
        print(f"Test 268 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 268 failed: {e}")
        test_results.append(False)

    # Test case 269
    try:
        result = SwapBitvectors(200, 220)
        assert result == (220, 200), f"Test 269 failed: got {result}, expected {(220, 200)}"
        print(f"Test 269 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 269 failed: {e}")
        test_results.append(False)

    # Test case 270
    try:
        result = SwapBitvectors(200, 0)
        assert result == (0, 200), f"Test 270 failed: got {result}, expected {(0, 200)}"
        print(f"Test 270 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 270 failed: {e}")
        test_results.append(False)

    # Test case 271
    try:
        result = SwapBitvectors(399, 43)
        assert result == (43, 143), f"Test 271 failed: got {result}, expected {(43, 143)}"
        print(f"Test 271 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 271 failed: {e}")
        test_results.append(False)

    # Test case 272
    try:
        result = SwapBitvectors(130, 56)
        assert result == (56, 130), f"Test 272 failed: got {result}, expected {(56, 130)}"
        print(f"Test 272 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 272 failed: {e}")
        test_results.append(False)

    # Test case 273
    try:
        result = SwapBitvectors(199, 0)
        assert result == (0, 199), f"Test 273 failed: got {result}, expected {(0, 199)}"
        print(f"Test 273 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 273 failed: {e}")
        test_results.append(False)

    # Test case 274
    try:
        result = SwapBitvectors(796, 0)
        assert result == (0, 28), f"Test 274 failed: got {result}, expected {(0, 28)}"
        print(f"Test 274 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 274 failed: {e}")
        test_results.append(False)

    # Test case 275
    try:
        result = SwapBitvectors(398, 54)
        assert result == (54, 142), f"Test 275 failed: got {result}, expected {(54, 142)}"
        print(f"Test 275 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 275 failed: {e}")
        test_results.append(False)

    # Test case 276
    try:
        result = SwapBitvectors(256, 4)
        assert result == (4, 0), f"Test 276 failed: got {result}, expected {(4, 0)}"
        print(f"Test 276 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 276 failed: {e}")
        test_results.append(False)

    # Test case 277
    try:
        result = SwapBitvectors(55, 62)
        assert result == (62, 55), f"Test 277 failed: got {result}, expected {(62, 55)}"
        print(f"Test 277 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 277 failed: {e}")
        test_results.append(False)

    # Test case 278
    try:
        result = SwapBitvectors(55, 483)
        assert result == (227, 55), f"Test 278 failed: got {result}, expected {(227, 55)}"
        print(f"Test 278 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 278 failed: {e}")
        test_results.append(False)

    # Test case 279
    try:
        result = SwapBitvectors(99, 200)
        assert result == (200, 99), f"Test 279 failed: got {result}, expected {(200, 99)}"
        print(f"Test 279 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 279 failed: {e}")
        test_results.append(False)

    # Test case 280
    try:
        result = SwapBitvectors(55, 202)
        assert result == (202, 55), f"Test 280 failed: got {result}, expected {(202, 55)}"
        print(f"Test 280 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 280 failed: {e}")
        test_results.append(False)

    # Test case 281
    try:
        result = SwapBitvectors(125, 0)
        assert result == (0, 125), f"Test 281 failed: got {result}, expected {(0, 125)}"
        print(f"Test 281 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 281 failed: {e}")
        test_results.append(False)

    # Test case 282
    try:
        result = SwapBitvectors(10, 240)
        assert result == (240, 10), f"Test 282 failed: got {result}, expected {(240, 10)}"
        print(f"Test 282 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 282 failed: {e}")
        test_results.append(False)

    # Test case 283
    try:
        result = SwapBitvectors(13, 1)
        assert result == (1, 13), f"Test 283 failed: got {result}, expected {(1, 13)}"
        print(f"Test 283 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 283 failed: {e}")
        test_results.append(False)

    # Test case 284
    try:
        result = SwapBitvectors(14, 10)
        assert result == (10, 14), f"Test 284 failed: got {result}, expected {(10, 14)}"
        print(f"Test 284 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 284 failed: {e}")
        test_results.append(False)

    # Test case 285
    try:
        result = SwapBitvectors(85, 101)
        assert result == (101, 85), f"Test 285 failed: got {result}, expected {(101, 85)}"
        print(f"Test 285 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 285 failed: {e}")
        test_results.append(False)

    # Test case 286
    try:
        result = SwapBitvectors(14, 239)
        assert result == (239, 14), f"Test 286 failed: got {result}, expected {(239, 14)}"
        print(f"Test 286 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 286 failed: {e}")
        test_results.append(False)

    # Test case 287
    try:
        result = SwapBitvectors(169, 13)
        assert result == (13, 169), f"Test 287 failed: got {result}, expected {(13, 169)}"
        print(f"Test 287 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 287 failed: {e}")
        test_results.append(False)

    # Test case 288
    try:
        result = SwapBitvectors(146, 203)
        assert result == (203, 146), f"Test 288 failed: got {result}, expected {(203, 146)}"
        print(f"Test 288 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 288 failed: {e}")
        test_results.append(False)

    # Test case 289
    try:
        result = SwapBitvectors(240, 252)
        assert result == (252, 240), f"Test 289 failed: got {result}, expected {(252, 240)}"
        print(f"Test 289 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 289 failed: {e}")
        test_results.append(False)

    # Test case 290
    try:
        result = SwapBitvectors(240, 216)
        assert result == (216, 240), f"Test 290 failed: got {result}, expected {(216, 240)}"
        print(f"Test 290 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 290 failed: {e}")
        test_results.append(False)

    # Test case 291
    try:
        result = SwapBitvectors(239, 14)
        assert result == (14, 239), f"Test 291 failed: got {result}, expected {(14, 239)}"
        print(f"Test 291 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 291 failed: {e}")
        test_results.append(False)

    # Test case 292
    try:
        result = SwapBitvectors(240, 12)
        assert result == (12, 240), f"Test 292 failed: got {result}, expected {(12, 240)}"
        print(f"Test 292 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 292 failed: {e}")
        test_results.append(False)

    # Test case 293
    try:
        result = SwapBitvectors(0, 239)
        assert result == (239, 0), f"Test 293 failed: got {result}, expected {(239, 0)}"
        print(f"Test 293 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 293 failed: {e}")
        test_results.append(False)

    # Test case 294
    try:
        result = SwapBitvectors(240, 5)
        assert result == (5, 240), f"Test 294 failed: got {result}, expected {(5, 240)}"
        print(f"Test 294 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 294 failed: {e}")
        test_results.append(False)

    # Test case 295
    try:
        result = SwapBitvectors(498, 5)
        assert result == (5, 242), f"Test 295 failed: got {result}, expected {(5, 242)}"
        print(f"Test 295 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 295 failed: {e}")
        test_results.append(False)

    # Test case 296
    try:
        result = SwapBitvectors(0, 10)
        assert result == (10, 0), f"Test 296 failed: got {result}, expected {(10, 0)}"
        print(f"Test 296 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 296 failed: {e}")
        test_results.append(False)

    # Test case 297
    try:
        result = SwapBitvectors(5, 252)
        assert result == (252, 5), f"Test 297 failed: got {result}, expected {(252, 5)}"
        print(f"Test 297 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 297 failed: {e}")
        test_results.append(False)

    # Test case 298
    try:
        result = SwapBitvectors(51, 250)
        assert result == (250, 51), f"Test 298 failed: got {result}, expected {(250, 51)}"
        print(f"Test 298 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 298 failed: {e}")
        test_results.append(False)

    # Test case 299
    try:
        result = SwapBitvectors(5, 0)
        assert result == (0, 5), f"Test 299 failed: got {result}, expected {(0, 5)}"
        print(f"Test 299 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 299 failed: {e}")
        test_results.append(False)

    # Test case 300
    try:
        result = SwapBitvectors(14, 8)
        assert result == (8, 14), f"Test 300 failed: got {result}, expected {(8, 14)}"
        print(f"Test 300 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 300 failed: {e}")
        test_results.append(False)

    # Test case 301
    try:
        result = SwapBitvectors(86, 251)
        assert result == (251, 86), f"Test 301 failed: got {result}, expected {(251, 86)}"
        print(f"Test 301 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 301 failed: {e}")
        test_results.append(False)

    # Test case 302
    try:
        result = SwapBitvectors(6, 249)
        assert result == (249, 6), f"Test 302 failed: got {result}, expected {(249, 6)}"
        print(f"Test 302 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 302 failed: {e}")
        test_results.append(False)

    # Test case 303
    try:
        result = SwapBitvectors(251, 499)
        assert result == (243, 251), f"Test 303 failed: got {result}, expected {(243, 251)}"
        print(f"Test 303 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 303 failed: {e}")
        test_results.append(False)

    # Test case 304
    try:
        result = SwapBitvectors(4, 17)
        assert result == (17, 4), f"Test 304 failed: got {result}, expected {(17, 4)}"
        print(f"Test 304 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 304 failed: {e}")
        test_results.append(False)

    # Test case 305
    try:
        result = SwapBitvectors(201, 501)
        assert result == (245, 201), f"Test 305 failed: got {result}, expected {(245, 201)}"
        print(f"Test 305 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 305 failed: {e}")
        test_results.append(False)

    # Test case 306
    try:
        result = SwapBitvectors(111, 221)
        assert result == (221, 111), f"Test 306 failed: got {result}, expected {(221, 111)}"
        print(f"Test 306 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 306 failed: {e}")
        test_results.append(False)

    # Test case 307
    try:
        result = SwapBitvectors(112, 221)
        assert result == (221, 112), f"Test 307 failed: got {result}, expected {(221, 112)}"
        print(f"Test 307 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 307 failed: {e}")
        test_results.append(False)

    # Test case 308
    try:
        result = SwapBitvectors(205, 222)
        assert result == (222, 205), f"Test 308 failed: got {result}, expected {(222, 205)}"
        print(f"Test 308 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 308 failed: {e}")
        test_results.append(False)

    # Test case 309
    try:
        result = SwapBitvectors(222, 510)
        assert result == (254, 222), f"Test 309 failed: got {result}, expected {(254, 222)}"
        print(f"Test 309 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 309 failed: {e}")
        test_results.append(False)

    # Test case 310
    try:
        result = SwapBitvectors(241, 443)
        assert result == (187, 241), f"Test 310 failed: got {result}, expected {(187, 241)}"
        print(f"Test 310 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 310 failed: {e}")
        test_results.append(False)

    # Test case 311
    try:
        result = SwapBitvectors(111, 443)
        assert result == (187, 111), f"Test 311 failed: got {result}, expected {(187, 111)}"
        print(f"Test 311 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 311 failed: {e}")
        test_results.append(False)

    # Test case 312
    try:
        result = SwapBitvectors(222, 0)
        assert result == (0, 222), f"Test 312 failed: got {result}, expected {(0, 222)}"
        print(f"Test 312 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 312 failed: {e}")
        test_results.append(False)

    # Test case 313
    try:
        result = SwapBitvectors(44, 111)
        assert result == (111, 44), f"Test 313 failed: got {result}, expected {(111, 44)}"
        print(f"Test 313 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 313 failed: {e}")
        test_results.append(False)

    # Test case 314
    try:
        result = SwapBitvectors(223, 444)
        assert result == (188, 223), f"Test 314 failed: got {result}, expected {(188, 223)}"
        print(f"Test 314 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 314 failed: {e}")
        test_results.append(False)

    # Test case 315
    try:
        result = SwapBitvectors(222, 109)
        assert result == (109, 222), f"Test 315 failed: got {result}, expected {(109, 222)}"
        print(f"Test 315 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 315 failed: {e}")
        test_results.append(False)

    # Test case 316
    try:
        result = SwapBitvectors(442, 253)
        assert result == (253, 186), f"Test 316 failed: got {result}, expected {(253, 186)}"
        print(f"Test 316 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 316 failed: {e}")
        test_results.append(False)

    # Test case 317
    try:
        result = SwapBitvectors(223, 112)
        assert result == (112, 223), f"Test 317 failed: got {result}, expected {(112, 223)}"
        print(f"Test 317 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 317 failed: {e}")
        test_results.append(False)

    # Test case 318
    try:
        result = SwapBitvectors(2072, 128)
        assert result == (128, 24), f"Test 318 failed: got {result}, expected {(128, 24)}"
        print(f"Test 318 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 318 failed: {e}")
        test_results.append(False)

    # Test case 319
    try:
        result = SwapBitvectors(144, 34)
        assert result == (34, 144), f"Test 319 failed: got {result}, expected {(34, 144)}"
        print(f"Test 319 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 319 failed: {e}")
        test_results.append(False)

    # Test case 320
    try:
        result = SwapBitvectors(260, 113)
        assert result == (113, 4), f"Test 320 failed: got {result}, expected {(113, 4)}"
        print(f"Test 320 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 320 failed: {e}")
        test_results.append(False)

    # Test case 321
    try:
        result = SwapBitvectors(73, 0)
        assert result == (0, 73), f"Test 321 failed: got {result}, expected {(0, 73)}"
        print(f"Test 321 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 321 failed: {e}")
        test_results.append(False)

    # Test case 322
    try:
        result = SwapBitvectors(31, 146)
        assert result == (146, 31), f"Test 322 failed: got {result}, expected {(146, 31)}"
        print(f"Test 322 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 322 failed: {e}")
        test_results.append(False)

    # Test case 323
    try:
        result = SwapBitvectors(72, 145)
        assert result == (145, 72), f"Test 323 failed: got {result}, expected {(145, 72)}"
        print(f"Test 323 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 323 failed: {e}")
        test_results.append(False)

    # Test case 324
    try:
        result = SwapBitvectors(15, 17)
        assert result == (17, 15), f"Test 324 failed: got {result}, expected {(17, 15)}"
        print(f"Test 324 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 324 failed: {e}")
        test_results.append(False)

    # Test case 325
    try:
        result = SwapBitvectors(147, 0)
        assert result == (0, 147), f"Test 325 failed: got {result}, expected {(0, 147)}"
        print(f"Test 325 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 325 failed: {e}")
        test_results.append(False)

    # Test case 326
    try:
        result = SwapBitvectors(582, 0)
        assert result == (0, 70), f"Test 326 failed: got {result}, expected {(0, 70)}"
        print(f"Test 326 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 326 failed: {e}")
        test_results.append(False)

    # Test case 327
    try:
        result = SwapBitvectors(146, 146)
        assert result == (146, 146), f"Test 327 failed: got {result}, expected {(146, 146)}"
        print(f"Test 327 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 327 failed: {e}")
        test_results.append(False)

    # Test case 328
    try:
        result = SwapBitvectors(218, 73)
        assert result == (73, 218), f"Test 328 failed: got {result}, expected {(73, 218)}"
        print(f"Test 328 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 328 failed: {e}")
        test_results.append(False)

    # Test case 329
    try:
        result = SwapBitvectors(146, 72)
        assert result == (72, 146), f"Test 329 failed: got {result}, expected {(72, 146)}"
        print(f"Test 329 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 329 failed: {e}")
        test_results.append(False)

    # Test case 330
    try:
        result = SwapBitvectors(67, 0)
        assert result == (0, 67), f"Test 330 failed: got {result}, expected {(0, 67)}"
        print(f"Test 330 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 330 failed: {e}")
        test_results.append(False)

    # Test case 331
    try:
        result = SwapBitvectors(292, 73)
        assert result == (73, 36), f"Test 331 failed: got {result}, expected {(73, 36)}"
        print(f"Test 331 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 331 failed: {e}")
        test_results.append(False)

    # Test case 332
    try:
        result = SwapBitvectors(12, 74)
        assert result == (74, 12), f"Test 332 failed: got {result}, expected {(74, 12)}"
        print(f"Test 332 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 332 failed: {e}")
        test_results.append(False)

    # Test case 333
    try:
        result = SwapBitvectors(66, 71)
        assert result == (71, 66), f"Test 333 failed: got {result}, expected {(71, 66)}"
        print(f"Test 333 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 333 failed: {e}")
        test_results.append(False)

    # Test case 334
    try:
        result = SwapBitvectors(44, 201)
        assert result == (201, 44), f"Test 334 failed: got {result}, expected {(201, 44)}"
        print(f"Test 334 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 334 failed: {e}")
        test_results.append(False)

    # Test case 335
    try:
        result = SwapBitvectors(1020, 218)
        assert result == (218, 252), f"Test 335 failed: got {result}, expected {(218, 252)}"
        print(f"Test 335 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 335 failed: {e}")
        test_results.append(False)

    # Test case 336
    try:
        result = SwapBitvectors(797, 85)
        assert result == (85, 29), f"Test 336 failed: got {result}, expected {(85, 29)}"
        print(f"Test 336 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 336 failed: {e}")
        test_results.append(False)

    # Test case 337
    try:
        result = SwapBitvectors(36, 218)
        assert result == (218, 36), f"Test 337 failed: got {result}, expected {(218, 36)}"
        print(f"Test 337 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 337 failed: {e}")
        test_results.append(False)

    # Test case 338
    try:
        result = SwapBitvectors(0, 217)
        assert result == (217, 0), f"Test 338 failed: got {result}, expected {(217, 0)}"
        print(f"Test 338 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 338 failed: {e}")
        test_results.append(False)

    # Test case 339
    try:
        result = SwapBitvectors(38, 169)
        assert result == (169, 38), f"Test 339 failed: got {result}, expected {(169, 38)}"
        print(f"Test 339 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 339 failed: {e}")
        test_results.append(False)

    # Test case 340
    try:
        result = SwapBitvectors(242, 436)
        assert result == (180, 242), f"Test 340 failed: got {result}, expected {(180, 242)}"
        print(f"Test 340 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 340 failed: {e}")
        test_results.append(False)

    # Test case 341
    try:
        result = SwapBitvectors(125, 217)
        assert result == (217, 125), f"Test 341 failed: got {result}, expected {(217, 125)}"
        print(f"Test 341 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 341 failed: {e}")
        test_results.append(False)

    # Test case 342
    try:
        result = SwapBitvectors(0, 70)
        assert result == (70, 0), f"Test 342 failed: got {result}, expected {(70, 0)}"
        print(f"Test 342 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 342 failed: {e}")
        test_results.append(False)

    # Test case 343
    try:
        result = SwapBitvectors(218, 36)
        assert result == (36, 218), f"Test 343 failed: got {result}, expected {(36, 218)}"
        print(f"Test 343 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 343 failed: {e}")
        test_results.append(False)

    # Test case 344
    try:
        result = SwapBitvectors(436, 16)
        assert result == (16, 180), f"Test 344 failed: got {result}, expected {(16, 180)}"
        print(f"Test 344 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 344 failed: {e}")
        test_results.append(False)

    # Test case 345
    try:
        result = SwapBitvectors(219, 76)
        assert result == (76, 219), f"Test 345 failed: got {result}, expected {(76, 219)}"
        print(f"Test 345 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 345 failed: {e}")
        test_results.append(False)

    # Test case 346
    try:
        result = SwapBitvectors(0, 37)
        assert result == (37, 0), f"Test 346 failed: got {result}, expected {(37, 0)}"
        print(f"Test 346 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 346 failed: {e}")
        test_results.append(False)

    # Test case 347
    try:
        result = SwapBitvectors(1, 37)
        assert result == (37, 1), f"Test 347 failed: got {result}, expected {(37, 1)}"
        print(f"Test 347 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 347 failed: {e}")
        test_results.append(False)

    # Test case 348
    try:
        result = SwapBitvectors(436, 37)
        assert result == (37, 180), f"Test 348 failed: got {result}, expected {(37, 180)}"
        print(f"Test 348 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 348 failed: {e}")
        test_results.append(False)

    # Test case 349
    try:
        result = SwapBitvectors(218, 198)
        assert result == (198, 218), f"Test 349 failed: got {result}, expected {(198, 218)}"
        print(f"Test 349 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 349 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
