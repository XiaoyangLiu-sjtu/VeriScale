# Coverage Report

Total executable lines: 2
Covered lines: 2
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def cubeSurfaceArea(size):
2: ✓     return 6 * (size ** 2)
```

## Complete Test File

```python
def cubeSurfaceArea(size):
    return 6 * (size ** 2)

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = cubeSurfaceArea(3)
        assert result == 54, f"Test 1 failed: got {result}, expected {54}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = cubeSurfaceArea(1)
        assert result == 6, f"Test 2 failed: got {result}, expected {6}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = cubeSurfaceArea(10)
        assert result == 600, f"Test 3 failed: got {result}, expected {600}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = cubeSurfaceArea(5)
        assert result == 150, f"Test 4 failed: got {result}, expected {150}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = cubeSurfaceArea(2)
        assert result == 24, f"Test 5 failed: got {result}, expected {24}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = cubeSurfaceArea(4)
        assert result == 96, f"Test 6 failed: got {result}, expected {96}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = cubeSurfaceArea(6)
        assert result == 216, f"Test 7 failed: got {result}, expected {216}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = cubeSurfaceArea(7)
        assert result == 294, f"Test 8 failed: got {result}, expected {294}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = cubeSurfaceArea(8)
        assert result == 384, f"Test 9 failed: got {result}, expected {384}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = cubeSurfaceArea(9)
        assert result == 486, f"Test 10 failed: got {result}, expected {486}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = cubeSurfaceArea(11)
        assert result == 726, f"Test 11 failed: got {result}, expected {726}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = cubeSurfaceArea(12)
        assert result == 864, f"Test 12 failed: got {result}, expected {864}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = cubeSurfaceArea(15)
        assert result == 1350, f"Test 13 failed: got {result}, expected {1350}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = cubeSurfaceArea(16)
        assert result == 1536, f"Test 14 failed: got {result}, expected {1536}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = cubeSurfaceArea(17)
        assert result == 1734, f"Test 15 failed: got {result}, expected {1734}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = cubeSurfaceArea(31)
        assert result == 5766, f"Test 16 failed: got {result}, expected {5766}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = cubeSurfaceArea(32)
        assert result == 6144, f"Test 17 failed: got {result}, expected {6144}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = cubeSurfaceArea(33)
        assert result == 6534, f"Test 18 failed: got {result}, expected {6534}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = cubeSurfaceArea(63)
        assert result == 23814, f"Test 19 failed: got {result}, expected {23814}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = cubeSurfaceArea(64)
        assert result == 24576, f"Test 20 failed: got {result}, expected {24576}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = cubeSurfaceArea(65)
        assert result == 25350, f"Test 21 failed: got {result}, expected {25350}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = cubeSurfaceArea(99)
        assert result == 58806, f"Test 22 failed: got {result}, expected {58806}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = cubeSurfaceArea(100)
        assert result == 60000, f"Test 23 failed: got {result}, expected {60000}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = cubeSurfaceArea(101)
        assert result == 61206, f"Test 24 failed: got {result}, expected {61206}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = cubeSurfaceArea(255)
        assert result == 390150, f"Test 25 failed: got {result}, expected {390150}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = cubeSurfaceArea(256)
        assert result == 393216, f"Test 26 failed: got {result}, expected {393216}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = cubeSurfaceArea(257)
        assert result == 396294, f"Test 27 failed: got {result}, expected {396294}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = cubeSurfaceArea(999)
        assert result == 5988006, f"Test 28 failed: got {result}, expected {5988006}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = cubeSurfaceArea(1000)
        assert result == 6000000, f"Test 29 failed: got {result}, expected {6000000}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = cubeSurfaceArea(1024)
        assert result == 6291456, f"Test 30 failed: got {result}, expected {6291456}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = cubeSurfaceArea(4096)
        assert result == 100663296, f"Test 31 failed: got {result}, expected {100663296}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = cubeSurfaceArea(10000)
        assert result == 600000000, f"Test 32 failed: got {result}, expected {600000000}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = cubeSurfaceArea(65535)
        assert result == 25769017350, f"Test 33 failed: got {result}, expected {25769017350}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = cubeSurfaceArea(65536)
        assert result == 25769803776, f"Test 34 failed: got {result}, expected {25769803776}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = cubeSurfaceArea(1000000)
        assert result == 6000000000000, f"Test 35 failed: got {result}, expected {6000000000000}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = cubeSurfaceArea(1000000000)
        assert result == 6000000000000000000, f"Test 36 failed: got {result}, expected {6000000000000000000}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = cubeSurfaceArea(2147483647)
        assert result == 27670116084794523654, f"Test 37 failed: got {result}, expected {27670116084794523654}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = cubeSurfaceArea(4294967295)
        assert result == 110680464390717702150, f"Test 38 failed: got {result}, expected {110680464390717702150}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = cubeSurfaceArea(9223372036854775807)
        assert result == 510423550381407695084381446705395007494, f"Test 39 failed: got {result}, expected {510423550381407695084381446705395007494}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = cubeSurfaceArea(18)
        assert result == 1944, f"Test 40 failed: got {result}, expected {1944}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = cubeSurfaceArea(60)
        assert result == 21600, f"Test 41 failed: got {result}, expected {21600}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = cubeSurfaceArea(4097)
        assert result == 100712454, f"Test 42 failed: got {result}, expected {100712454}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = cubeSurfaceArea(66)
        assert result == 26136, f"Test 43 failed: got {result}, expected {26136}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = cubeSurfaceArea(4294967296)
        assert result == 110680464442257309696, f"Test 44 failed: got {result}, expected {110680464442257309696}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = cubeSurfaceArea(10001)
        assert result == 600120006, f"Test 45 failed: got {result}, expected {600120006}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = cubeSurfaceArea(1023)
        assert result == 6279174, f"Test 46 failed: got {result}, expected {6279174}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = cubeSurfaceArea(20)
        assert result == 2400, f"Test 47 failed: got {result}, expected {2400}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = cubeSurfaceArea(1000001)
        assert result == 6000012000006, f"Test 48 failed: got {result}, expected {6000012000006}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = cubeSurfaceArea(263)
        assert result == 415014, f"Test 49 failed: got {result}, expected {415014}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = cubeSurfaceArea(202)
        assert result == 244824, f"Test 50 failed: got {result}, expected {244824}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = cubeSurfaceArea(131071)
        assert result == 103077642246, f"Test 51 failed: got {result}, expected {103077642246}"
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
