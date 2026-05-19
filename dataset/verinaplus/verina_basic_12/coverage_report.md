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

    # Test case 52
    try:
        result = cubeSurfaceArea(2048)
        assert result == 25165824, f"Test 52 failed: got {result}, expected {25165824}"
        print(f"Test 52 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 52 failed: {e}")
        test_results.append(False)

    # Test case 53
    try:
        result = cubeSurfaceArea(201)
        assert result == 242406, f"Test 53 failed: got {result}, expected {242406}"
        print(f"Test 53 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 53 failed: {e}")
        test_results.append(False)

    # Test case 54
    try:
        result = cubeSurfaceArea(4095)
        assert result == 100614150, f"Test 54 failed: got {result}, expected {100614150}"
        print(f"Test 54 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 54 failed: {e}")
        test_results.append(False)

    # Test case 55
    try:
        result = cubeSurfaceArea(13)
        assert result == 1014, f"Test 55 failed: got {result}, expected {1014}"
        print(f"Test 55 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 55 failed: {e}")
        test_results.append(False)

    # Test case 56
    try:
        result = cubeSurfaceArea(9998)
        assert result == 599760024, f"Test 56 failed: got {result}, expected {599760024}"
        print(f"Test 56 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 56 failed: {e}")
        test_results.append(False)

    # Test case 57
    try:
        result = cubeSurfaceArea(18446744073709551613)
        assert result == 2041694201525630780116164857937065410614, f"Test 57 failed: got {result}, expected {2041694201525630780116164857937065410614}"
        print(f"Test 57 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 57 failed: {e}")
        test_results.append(False)

    # Test case 58
    try:
        result = cubeSurfaceArea(128)
        assert result == 98304, f"Test 58 failed: got {result}, expected {98304}"
        print(f"Test 58 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 58 failed: {e}")
        test_results.append(False)

    # Test case 59
    try:
        result = cubeSurfaceArea(131070)
        assert result == 103076069400, f"Test 59 failed: got {result}, expected {103076069400}"
        print(f"Test 59 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 59 failed: {e}")
        test_results.append(False)

    # Test case 60
    try:
        result = cubeSurfaceArea(98)
        assert result == 57624, f"Test 60 failed: got {result}, expected {57624}"
        print(f"Test 60 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 60 failed: {e}")
        test_results.append(False)

    # Test case 61
    try:
        result = cubeSurfaceArea(40)
        assert result == 9600, f"Test 61 failed: got {result}, expected {9600}"
        print(f"Test 61 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 61 failed: {e}")
        test_results.append(False)

    # Test case 62
    try:
        result = cubeSurfaceArea(25)
        assert result == 3750, f"Test 62 failed: got {result}, expected {3750}"
        print(f"Test 62 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 62 failed: {e}")
        test_results.append(False)

    # Test case 63
    try:
        result = cubeSurfaceArea(510)
        assert result == 1560600, f"Test 63 failed: got {result}, expected {1560600}"
        print(f"Test 63 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 63 failed: {e}")
        test_results.append(False)

    # Test case 64
    try:
        result = cubeSurfaceArea(258)
        assert result == 399384, f"Test 64 failed: got {result}, expected {399384}"
        print(f"Test 64 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 64 failed: {e}")
        test_results.append(False)

    # Test case 65
    try:
        result = cubeSurfaceArea(200)
        assert result == 240000, f"Test 65 failed: got {result}, expected {240000}"
        print(f"Test 65 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 65 failed: {e}")
        test_results.append(False)

    # Test case 66
    try:
        result = cubeSurfaceArea(999998)
        assert result == 5999976000024, f"Test 66 failed: got {result}, expected {5999976000024}"
        print(f"Test 66 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 66 failed: {e}")
        test_results.append(False)

    # Test case 67
    try:
        result = cubeSurfaceArea(203)
        assert result == 247254, f"Test 67 failed: got {result}, expected {247254}"
        print(f"Test 67 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 67 failed: {e}")
        test_results.append(False)

    # Test case 68
    try:
        result = cubeSurfaceArea(30)
        assert result == 5400, f"Test 68 failed: got {result}, expected {5400}"
        print(f"Test 68 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 68 failed: {e}")
        test_results.append(False)

    # Test case 69
    try:
        result = cubeSurfaceArea(9997)
        assert result == 599640054, f"Test 69 failed: got {result}, expected {599640054}"
        print(f"Test 69 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 69 failed: {e}")
        test_results.append(False)

    # Test case 70
    try:
        result = cubeSurfaceArea(39)
        assert result == 9126, f"Test 70 failed: got {result}, expected {9126}"
        print(f"Test 70 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 70 failed: {e}")
        test_results.append(False)

    # Test case 71
    try:
        result = cubeSurfaceArea(2046)
        assert result == 25116696, f"Test 71 failed: got {result}, expected {25116696}"
        print(f"Test 71 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 71 failed: {e}")
        test_results.append(False)

    # Test case 72
    try:
        result = cubeSurfaceArea(80)
        assert result == 38400, f"Test 72 failed: got {result}, expected {38400}"
        print(f"Test 72 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 72 failed: {e}")
        test_results.append(False)

    # Test case 73
    try:
        result = cubeSurfaceArea(126)
        assert result == 95256, f"Test 73 failed: got {result}, expected {95256}"
        print(f"Test 73 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 73 failed: {e}")
        test_results.append(False)

    # Test case 74
    try:
        result = cubeSurfaceArea(9223372036854775808)
        assert result == 510423550381407695195061911147652317184, f"Test 74 failed: got {result}, expected {510423550381407695195061911147652317184}"
        print(f"Test 74 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 74 failed: {e}")
        test_results.append(False)

    # Test case 75
    try:
        result = cubeSurfaceArea(62)
        assert result == 23064, f"Test 75 failed: got {result}, expected {23064}"
        print(f"Test 75 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 75 failed: {e}")
        test_results.append(False)

    # Test case 76
    try:
        result = cubeSurfaceArea(2147483646)
        assert result == 27670116059024719896, f"Test 76 failed: got {result}, expected {27670116059024719896}"
        print(f"Test 76 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 76 failed: {e}")
        test_results.append(False)

    # Test case 77
    try:
        result = cubeSurfaceArea(262)
        assert result == 411864, f"Test 77 failed: got {result}, expected {411864}"
        print(f"Test 77 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 77 failed: {e}")
        test_results.append(False)

    # Test case 78
    try:
        result = cubeSurfaceArea(198)
        assert result == 235224, f"Test 78 failed: got {result}, expected {235224}"
        print(f"Test 78 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 78 failed: {e}")
        test_results.append(False)

    # Test case 79
    try:
        result = cubeSurfaceArea(4294967294)
        assert result == 110680464339178094616, f"Test 79 failed: got {result}, expected {110680464339178094616}"
        print(f"Test 79 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 79 failed: {e}")
        test_results.append(False)

    # Test case 80
    try:
        result = cubeSurfaceArea(264)
        assert result == 418176, f"Test 80 failed: got {result}, expected {418176}"
        print(f"Test 80 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 80 failed: {e}")
        test_results.append(False)

    # Test case 81
    try:
        result = cubeSurfaceArea(18446744073709551612)
        assert result == 2041694201525630779894803929052550791264, f"Test 81 failed: got {result}, expected {2041694201525630779894803929052550791264}"
        print(f"Test 81 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 81 failed: {e}")
        test_results.append(False)

    # Test case 82
    try:
        result = cubeSurfaceArea(67)
        assert result == 26934, f"Test 82 failed: got {result}, expected {26934}"
        print(f"Test 82 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 82 failed: {e}")
        test_results.append(False)

    # Test case 83
    try:
        result = cubeSurfaceArea(526)
        assert result == 1660056, f"Test 83 failed: got {result}, expected {1660056}"
        print(f"Test 83 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 83 failed: {e}")
        test_results.append(False)

    # Test case 84
    try:
        result = cubeSurfaceArea(127)
        assert result == 96774, f"Test 84 failed: got {result}, expected {96774}"
        print(f"Test 84 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 84 failed: {e}")
        test_results.append(False)

    # Test case 85
    try:
        result = cubeSurfaceArea(36)
        assert result == 7776, f"Test 85 failed: got {result}, expected {7776}"
        print(f"Test 85 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 85 failed: {e}")
        test_results.append(False)

    # Test case 86
    try:
        result = cubeSurfaceArea(24)
        assert result == 3456, f"Test 86 failed: got {result}, expected {3456}"
        print(f"Test 86 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 86 failed: {e}")
        test_results.append(False)

    # Test case 87
    try:
        result = cubeSurfaceArea(42)
        assert result == 10584, f"Test 87 failed: got {result}, expected {10584}"
        print(f"Test 87 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 87 failed: {e}")
        test_results.append(False)

    # Test case 88
    try:
        result = cubeSurfaceArea(2147483645)
        assert result == 27670116033254916150, f"Test 88 failed: got {result}, expected {27670116033254916150}"
        print(f"Test 88 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 88 failed: {e}")
        test_results.append(False)

    # Test case 89
    try:
        result = cubeSurfaceArea(254)
        assert result == 387096, f"Test 89 failed: got {result}, expected {387096}"
        print(f"Test 89 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 89 failed: {e}")
        test_results.append(False)

    # Test case 90
    try:
        result = cubeSurfaceArea(512)
        assert result == 1572864, f"Test 90 failed: got {result}, expected {1572864}"
        print(f"Test 90 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 90 failed: {e}")
        test_results.append(False)

    # Test case 91
    try:
        result = cubeSurfaceArea(8589934590)
        assert result == 442721857562870808600, f"Test 91 failed: got {result}, expected {442721857562870808600}"
        print(f"Test 91 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 91 failed: {e}")
        test_results.append(False)

    # Test case 92
    try:
        result = cubeSurfaceArea(65537)
        assert result == 25770590214, f"Test 92 failed: got {result}, expected {25770590214}"
        print(f"Test 92 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 92 failed: {e}")
        test_results.append(False)

    # Test case 93
    try:
        result = cubeSurfaceArea(37)
        assert result == 8214, f"Test 93 failed: got {result}, expected {8214}"
        print(f"Test 93 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 93 failed: {e}")
        test_results.append(False)

    # Test case 94
    try:
        result = cubeSurfaceArea(3996)
        assert result == 95808096, f"Test 94 failed: got {result}, expected {95808096}"
        print(f"Test 94 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 94 failed: {e}")
        test_results.append(False)

    # Test case 95
    try:
        result = cubeSurfaceArea(998)
        assert result == 5976024, f"Test 95 failed: got {result}, expected {5976024}"
        print(f"Test 95 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 95 failed: {e}")
        test_results.append(False)

    # Test case 96
    try:
        result = cubeSurfaceArea(65534)
        assert result == 25768230936, f"Test 96 failed: got {result}, expected {25768230936}"
        print(f"Test 96 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 96 failed: {e}")
        test_results.append(False)

    # Test case 97
    try:
        result = cubeSurfaceArea(36893488147419103226)
        assert result == 8166776806102523120464659431748261642456, f"Test 97 failed: got {result}, expected {8166776806102523120464659431748261642456}"
        print(f"Test 97 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 97 failed: {e}")
        test_results.append(False)

    # Test case 98
    try:
        result = cubeSurfaceArea(18446744073709551610)
        assert result == 2041694201525630779452082071283521552600, f"Test 98 failed: got {result}, expected {2041694201525630779452082071283521552600}"
        print(f"Test 98 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 98 failed: {e}")
        test_results.append(False)

    # Test case 99
    try:
        result = cubeSurfaceArea(2000)
        assert result == 24000000, f"Test 99 failed: got {result}, expected {24000000}"
        print(f"Test 99 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 99 failed: {e}")
        test_results.append(False)

    # Test case 100
    try:
        result = cubeSurfaceArea(1025)
        assert result == 6303750, f"Test 100 failed: got {result}, expected {6303750}"
        print(f"Test 100 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 100 failed: {e}")
        test_results.append(False)

    # Test case 101
    try:
        result = cubeSurfaceArea(32764)
        assert result == 6440878176, f"Test 101 failed: got {result}, expected {6440878176}"
        print(f"Test 101 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 101 failed: {e}")
        test_results.append(False)

    # Test case 102
    try:
        result = cubeSurfaceArea(36893488147419103220)
        assert result == 8166776806102523117808328285134086210400, f"Test 102 failed: got {result}, expected {8166776806102523117808328285134086210400}"
        print(f"Test 102 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 102 failed: {e}")
        test_results.append(False)

    # Test case 103
    try:
        result = cubeSurfaceArea(406)
        assert result == 989016, f"Test 103 failed: got {result}, expected {989016}"
        print(f"Test 103 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 103 failed: {e}")
        test_results.append(False)

    # Test case 104
    try:
        result = cubeSurfaceArea(82)
        assert result == 40344, f"Test 104 failed: got {result}, expected {40344}"
        print(f"Test 104 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 104 failed: {e}")
        test_results.append(False)

    # Test case 105
    try:
        result = cubeSurfaceArea(2050)
        assert result == 25215000, f"Test 105 failed: got {result}, expected {25215000}"
        print(f"Test 105 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 105 failed: {e}")
        test_results.append(False)

    # Test case 106
    try:
        result = cubeSurfaceArea(19)
        assert result == 2166, f"Test 106 failed: got {result}, expected {2166}"
        print(f"Test 106 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 106 failed: {e}")
        test_results.append(False)

    # Test case 107
    try:
        result = cubeSurfaceArea(3995)
        assert result == 95760150, f"Test 107 failed: got {result}, expected {95760150}"
        print(f"Test 107 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 107 failed: {e}")
        test_results.append(False)

    # Test case 108
    try:
        result = cubeSurfaceArea(97)
        assert result == 56454, f"Test 108 failed: got {result}, expected {56454}"
        print(f"Test 108 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 108 failed: {e}")
        test_results.append(False)

    # Test case 109
    try:
        result = cubeSurfaceArea(9223372036854775806)
        assert result == 510423550381407694973700982263137697816, f"Test 109 failed: got {result}, expected {510423550381407694973700982263137697816}"
        print(f"Test 109 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 109 failed: {e}")
        test_results.append(False)

    # Test case 110
    try:
        result = cubeSurfaceArea(2049)
        assert result == 25190406, f"Test 110 failed: got {result}, expected {25190406}"
        print(f"Test 110 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 110 failed: {e}")
        test_results.append(False)

    return test_results

if __name__ == '__main__':
    results = run_tests()
    print(f"\n{sum(results)}/{len(results)} tests passed")
```
