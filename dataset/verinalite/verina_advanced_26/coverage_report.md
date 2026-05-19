# Coverage Report

Total executable lines: 15
Covered lines: 15
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def letterCombinations(digits):
2: ✓     if not digits:
3: ✓         return []
4: ✓     mapping = {
5:           '2': "abc",
6:           '3': "def",
7:           '4': "ghi",
8:           '5': "jkl",
9:           '6': "mno",
10:           '7': "pqrs",
11:           '8': "tuv",
12:           '9': "wxyz"
13:       }
14: ✓     combinations = [""]
15: ✓     for digit in digits:
16: ✓         if digit not in mapping:
17: ✓             combinations = []
18: ✓             break
19: ✓         temp = []
20: ✓         for combination in combinations:
21: ✓             for letter in mapping[digit]:
22: ✓                 temp.append(combination + letter)
23: ✓         combinations = temp
24: ✓     return combinations
```

## Complete Test File

```python
def letterCombinations(digits):
    if not digits:
        return []
    mapping = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }
    combinations = [""]
    for digit in digits:
        if digit not in mapping:
            combinations = []
            break
        temp = []
        for combination in combinations:
            for letter in mapping[digit]:
                temp.append(combination + letter)
        combinations = temp
    return combinations

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = letterCombinations('')
        assert result == '[]', f"Test 1 failed: got {result}, expected {'[]'}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = letterCombinations('2')
        assert result == '["a", "b", "c"]', f"Test 2 failed: got {result}, expected {'["a", "b", "c"]'}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = letterCombinations('9')
        assert result == '["w", "x", "y", "z"]', f"Test 3 failed: got {result}, expected {'["w", "x", "y", "z"]'}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = letterCombinations('23')
        assert result == '["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]', f"Test 4 failed: got {result}, expected {'["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]'}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = letterCombinations('27')
        assert result == '["ap", "aq", "ar", "as", "bp", "bq", "br", "bs", "cp", "cq", "cr", "cs"]', f"Test 5 failed: got {result}, expected {'["ap", "aq", "ar", "as", "bp", "bq", "br", "bs", "cp", "cq", "cr", "cs"]'}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = letterCombinations('0')
        assert result == '[]', f"Test 6 failed: got {result}, expected {'[]'}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = letterCombinations('21')
        assert result == '[]', f"Test 7 failed: got {result}, expected {'[]'}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = letterCombinations('79')
        assert result == '["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]', f"Test 8 failed: got {result}, expected {'["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]'}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = letterCombinations('222')
        assert result == '"bcc", "caa", "cab", "cac", "cba", "cbb", "cbc", "cca", "ccb", "ccc"]', f"Test 9 failed: got {result}, expected {'"bcc", "caa", "cab", "cac", "cba", "cbb", "cbc", "cca", "ccb", "ccc"]'}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = letterCombinations('999')
        assert result == '"zwz", "zxw", "zxx", "zxy", "zxz", "zyw", "zyx", "zyy", "zyz", "zzw", "zzx", "zzy", "zzz"]', f"Test 10 failed: got {result}, expected {'"zwz", "zxw", "zxx", "zxy", "zxz", "zyw", "zyx", "zyy", "zyz", "zzw", "zzx", "zzy", "zzz"]'}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = letterCombinations('234')
        assert result == '"bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]', f"Test 11 failed: got {result}, expected {'"bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]'}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = letterCombinations('568')
        assert result == '"kov", "lmt", "lmu", "lmv", "lnt", "lnu", "lnv", "lot", "lou", "lov"]', f"Test 12 failed: got {result}, expected {'"kov", "lmt", "lmu", "lmv", "lnt", "lnu", "lnv", "lot", "lou", "lov"]'}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = letterCombinations('762')
        assert result == '"sob", "soc"]', f"Test 13 failed: got {result}, expected {'"sob", "soc"]'}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = letterCombinations('843')
        assert result == '"uif", "vgd", "vge", "vgf", "vhd", "vhe", "vhf", "vid", "vie", "vif"]', f"Test 14 failed: got {result}, expected {'"uif", "vgd", "vge", "vgf", "vhd", "vhe", "vhf", "vid", "vie", "vif"]'}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = letterCombinations('294')
        assert result == '"czh", "czi"]', f"Test 15 failed: got {result}, expected {'"czh", "czi"]'}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = letterCombinations('5678')
        assert result == '"lost", "losu", "losv"]', f"Test 16 failed: got {result}, expected {'"lost", "losu", "losv"]'}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = letterCombinations('2345')
        assert result == '"cfhj", "cfhk", "cfhl", "cfij", "cfik", "cfil"]', f"Test 17 failed: got {result}, expected {'"cfhj", "cfhk", "cfhl", "cfij", "cfik", "cfil"]'}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = letterCombinations('6789')
        assert result == '"ostz", "osuw", "osux", "osuy", "osuz", "osvw", "osvx", "osvy", "osvz"]', f"Test 18 failed: got {result}, expected {'"ostz", "osuw", "osux", "osuy", "osuz", "osvw", "osvx", "osvy", "osvz"]'}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = letterCombinations('2222')
        assert result == '"ccba", "ccbb", "ccbc", "ccca", "cccb", "cccc"]', f"Test 19 failed: got {result}, expected {'"ccba", "ccbb", "ccbc", "ccca", "cccb", "cccc"]'}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = letterCombinations('7777')
        assert result == '"ssss"]', f"Test 20 failed: got {result}, expected {'"ssss"]'}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = letterCombinations('9999')
        assert result == '"zzzz"]', f"Test 21 failed: got {result}, expected {'"zzzz"]'}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = letterCombinations('23456789')
        assert result == '"cfilosvw", "cfilosvx", "cfilosvy", "cfilosvz"]', f"Test 22 failed: got {result}, expected {'"cfilosvw", "cfilosvx", "cfilosvy", "cfilosvz"]'}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = letterCombinations('98765432')
        assert result == '"zvsoliec", "zvsolifa", "zvsolifb", "zvsolifc"]', f"Test 23 failed: got {result}, expected {'"zvsoliec", "zvsolifa", "zvsolifb", "zvsolifc"]'}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = letterCombinations('272727')
        assert result == '"cscsap", "cscsaq", "cscsar", "cscsas", "cscsbp", "cscsbq", "cscsbr", "cscsbs", "cscscp", "cscscq", "cscscr", "cscscs"]', f"Test 24 failed: got {result}, expected {'"cscsap", "cscsaq", "cscsar", "cscsas", "cscsbp", "cscsbq", "cscsbr", "cscsbs", "cscscp", "cscscq", "cscscr", "cscscs"]'}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = letterCombinations('739')
        assert result == '"rfy", "rfz", "sdw", "sdx", "sdy", "sdz", "sew", "sex", "sey", "sez", "sfw", "sfx", "sfy", "sfz"]', f"Test 25 failed: got {result}, expected {'"rfy", "rfz", "sdw", "sdx", "sdy", "sdz", "sew", "sex", "sey", "sez", "sfw", "sfx", "sfy", "sfz"]'}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = letterCombinations('4856')
        assert result == '"ivkm", "ivkn", "ivko", "ivlm", "ivln", "ivlo"]', f"Test 26 failed: got {result}, expected {'"ivkm", "ivkn", "ivko", "ivlm", "ivln", "ivlo"]'}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = letterCombinations('9327')
        assert result == '"zfas", "zfbp", "zfbq", "zfbr", "zfbs", "zfcp", "zfcq", "zfcr", "zfcs"]', f"Test 27 failed: got {result}, expected {'"zfas", "zfbp", "zfbq", "zfbr", "zfbs", "zfcp", "zfcq", "zfcr", "zfcs"]'}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = letterCombinations('2468')
        assert result == '"cint", "cinu", "cinv", "ciot", "ciou", "ciov"]', f"Test 28 failed: got {result}, expected {'"cint", "cinu", "cinv", "ciot", "ciou", "ciov"]'}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = letterCombinations('8642')
        assert result == '"voha", "vohb", "vohc", "voia", "voib", "voic"]', f"Test 29 failed: got {result}, expected {'"voha", "vohb", "vohc", "voia", "voib", "voic"]'}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = letterCombinations('3579')
        assert result == '"flqz", "flrw", "flrx", "flry", "flrz", "flsw", "flsx", "flsy", "flsz"]', f"Test 30 failed: got {result}, expected {'"flqz", "flrw", "flrx", "flry", "flrz", "flsw", "flsx", "flsy", "flsz"]'}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = letterCombinations('2793')
        assert result == '"csxd", "csxe", "csxf", "csyd", "csye", "csyf", "cszd", "csze", "cszf"]', f"Test 31 failed: got {result}, expected {'"csxd", "csxe", "csxf", "csyd", "csye", "csyf", "cszd", "csze", "cszf"]'}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = letterCombinations('222999')
        assert result == '"ccczxw", "ccczxx", "ccczxy", "ccczxz", "ccczyw", "ccczyx", "ccczyy", "ccczyz", "ccczzw", "ccczzx", "ccczzy", "ccczzz"]', f"Test 32 failed: got {result}, expected {'"ccczxw", "ccczxx", "ccczxy", "ccczxz", "ccczyw", "ccczyx", "ccczyy", "ccczyz", "ccczzw", "ccczzx", "ccczzy", "ccczzz"]'}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = letterCombinations('789234')
        assert result == '"svzbfg", "svzbfh", "svzbfi", "svzcdg", "svzcdh", "svzcdi", "svzceg", "svzceh", "svzcei", "svzcfg", "svzcfh", "svzcfi"]', f"Test 33 failed: got {result}, expected {'"svzbfg", "svzbfh", "svzbfi", "svzcdg", "svzcdh", "svzcdi", "svzceg", "svzceh", "svzcei", "svzcfg", "svzcfh", "svzcfi"]'}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = letterCombinations('9384756')
        assert result == '"zfvisjn", "zfvisjo", "zfviskm", "zfviskn", "zfvisko", "zfvislm", "zfvisln", "zfvislo"]', f"Test 34 failed: got {result}, expected {'"zfvisjn", "zfvisjo", "zfviskm", "zfviskn", "zfvisko", "zfvislm", "zfvisln", "zfvislo"]'}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = letterCombinations('1')
        assert result == '[]', f"Test 35 failed: got {result}, expected {'[]'}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = letterCombinations('10')
        assert result == '[]', f"Test 36 failed: got {result}, expected {'[]'}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = letterCombinations('201')
        assert result == '[]', f"Test 37 failed: got {result}, expected {'[]'}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = letterCombinations('2a3')
        assert result == '[]', f"Test 38 failed: got {result}, expected {'[]'}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = letterCombinations('3972')
        assert result == '"fzqa", "fzqb", "fzqc", "fzra", "fzrb", "fzrc", "fzsa", "fzsb", "fzsc"]', f"Test 39 failed: got {result}, expected {'"fzqa", "fzqb", "fzqc", "fzra", "fzrb", "fzrc", "fzsa", "fzsb", "fzsc"]'}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = letterCombinations('32')
        assert result == '["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"]', f"Test 40 failed: got {result}, expected {'["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"]'}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = letterCombinations('999222')
        assert result == '"zzzbca", "zzzbcb", "zzzbcc", "zzzcaa", "zzzcab", "zzzcac", "zzzcba", "zzzcbb", "zzzcbc", "zzzcca", "zzzccb", "zzzccc"]', f"Test 41 failed: got {result}, expected {'"zzzbca", "zzzbcb", "zzzbcc", "zzzcaa", "zzzcab", "zzzcac", "zzzcba", "zzzcbb", "zzzcbc", "zzzcca", "zzzccb", "zzzccc"]'}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = letterCombinations('97')
        assert result == '["wp", "wq", "wr", "ws", "xp", "xq", "xr", "xs", "yp", "yq", "yr", "ys", "zp", "zq", "zr", "zs"]', f"Test 42 failed: got {result}, expected {'["wp", "wq", "wr", "ws", "xp", "xq", "xr", "xs", "yp", "yq", "yr", "ys", "zp", "zq", "zr", "zs"]'}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = letterCombinations('865')
        assert result == '"uol", "vmj", "vmk", "vml", "vnj", "vnk", "vnl", "voj", "vok", "vol"]', f"Test 43 failed: got {result}, expected {'"uol", "vmj", "vmk", "vml", "vnj", "vnk", "vnl", "voj", "vok", "vol"]'}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = letterCombinations('267')
        assert result == '"cor", "cos"]', f"Test 44 failed: got {result}, expected {'"cor", "cos"]'}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = letterCombinations('492')
        assert result == '"izb", "izc"]', f"Test 45 failed: got {result}, expected {'"izb", "izc"]'}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = letterCombinations('9876')
        assert result == '"zvqm", "zvqn", "zvqo", "zvrm", "zvrn", "zvro", "zvsm", "zvsn", "zvso"]', f"Test 46 failed: got {result}, expected {'"zvqm", "zvqn", "zvqo", "zvrm", "zvrn", "zvro", "zvsm", "zvsn", "zvso"]'}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = letterCombinations('7239')
        assert result == '"scdz", "scew", "scex", "scey", "scez", "scfw", "scfx", "scfy", "scfz"]', f"Test 47 failed: got {result}, expected {'"scdz", "scew", "scex", "scey", "scez", "scfw", "scfx", "scfy", "scfz"]'}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = letterCombinations('9753')
        assert result == '"zsjd", "zsje", "zsjf", "zskd", "zske", "zskf", "zsld", "zsle", "zslf"]', f"Test 48 failed: got {result}, expected {'"zsjd", "zsje", "zsjf", "zskd", "zske", "zskf", "zsld", "zsle", "zslf"]'}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = letterCombinations('432987')
        assert result == '"ifcztp", "ifcztq", "ifcztr", "ifczts", "ifczup", "ifczuq", "ifczur", "ifczus", "ifczvp", "ifczvq", "ifczvr", "ifczvs"]', f"Test 49 failed: got {result}, expected {'"ifcztp", "ifcztq", "ifcztr", "ifczts", "ifczup", "ifczuq", "ifczur", "ifczus", "ifczvp", "ifczvq", "ifczvr", "ifczvs"]'}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = letterCombinations('6574839')
        assert result == '"olsivew", "olsivex", "olsivey", "olsivez", "olsivfw", "olsivfx", "olsivfy", "olsivfz"]', f"Test 50 failed: got {result}, expected {'"olsivew", "olsivex", "olsivey", "olsivez", "olsivfw", "olsivfx", "olsivfy", "olsivfz"]'}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = letterCombinations('348')
        assert result == '"eiv", "fgt", "fgu", "fgv", "fht", "fhu", "fhv", "fit", "fiu", "fiv"]', f"Test 51 failed: got {result}, expected {'"eiv", "fgt", "fgu", "fgv", "fht", "fhu", "fhv", "fit", "fiu", "fiv"]'}"
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
