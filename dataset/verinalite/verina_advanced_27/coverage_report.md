# Coverage Report

Total executable lines: 19
Covered lines: 19
Missed lines: 0
Coverage percentage: 100.00%

## Source Code with Coverage

```python
1: ✓ def longestCommonSubsequence(s1, s2):
2: ✓     m, n = len(s1), len(s2)
3: ✓     dp = [[0]*(n+1) for _ in range(m+1)]
4: ✓     for i in range(1, m+1):
5: ✓         for j in range(1, n+1):
6: ✓             if s1[i-1] == s2[j-1]:
7: ✓                 dp[i][j] = dp[i-1][j-1] + 1
8:               else:
9: ✓                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
10: ✓     i, j = m, n
11: ✓     lcs = []
12: ✓     while i > 0 and j > 0:
13: ✓         if s1[i-1] == s2[j-1]:
14: ✓             lcs.append(s1[i-1])
15: ✓             i -= 1
16: ✓             j -= 1
17: ✓         elif dp[i-1][j] >= dp[i][j-1]:
18: ✓             i -= 1
19:           else:
20: ✓             j -= 1
21: ✓     return ''.join(reversed(lcs))
```

## Complete Test File

```python
def longestCommonSubsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.append(s1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(lcs))

def run_tests():
    test_results = []
    # Test case 1
    try:
        result = longestCommonSubsequence('abcde', 'ace')
        assert result == 'ace', f"Test 1 failed: got {result}, expected {'ace'}"
        print(f"Test 1 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 1 failed: {e}")
        test_results.append(False)

    # Test case 2
    try:
        result = longestCommonSubsequence('aaaa', 'bbaaa')
        assert result == 'aaa', f"Test 2 failed: got {result}, expected {'aaa'}"
        print(f"Test 2 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 2 failed: {e}")
        test_results.append(False)

    # Test case 3
    try:
        result = longestCommonSubsequence('xyz', 'abc')
        assert result == '', f"Test 3 failed: got {result}, expected {''}"
        print(f"Test 3 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 3 failed: {e}")
        test_results.append(False)

    # Test case 4
    try:
        result = longestCommonSubsequence('axbxc', 'abxc')
        assert result == 'abxc', f"Test 4 failed: got {result}, expected {'abxc'}"
        print(f"Test 4 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 4 failed: {e}")
        test_results.append(False)

    # Test case 5
    try:
        result = longestCommonSubsequence('AGGTAB', 'GXTXAYB')
        assert result == 'GTAB', f"Test 5 failed: got {result}, expected {'GTAB'}"
        print(f"Test 5 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 5 failed: {e}")
        test_results.append(False)

    # Test case 6
    try:
        result = longestCommonSubsequence('abababab', 'baba')
        assert result == 'baba', f"Test 6 failed: got {result}, expected {'baba'}"
        print(f"Test 6 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 6 failed: {e}")
        test_results.append(False)

    # Test case 7
    try:
        result = longestCommonSubsequence('a b c d e', 'abcde')
        assert result == 'abcde', f"Test 7 failed: got {result}, expected {'abcde'}"
        print(f"Test 7 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 7 failed: {e}")
        test_results.append(False)

    # Test case 8
    try:
        result = longestCommonSubsequence('  lead and trail  ', 'leadtrail')
        assert result == 'leadtrail', f"Test 8 failed: got {result}, expected {'leadtrail'}"
        print(f"Test 8 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 8 failed: {e}")
        test_results.append(False)

    # Test case 9
    try:
        result = longestCommonSubsequence('!@#$%^&*()', '$^&')
        assert result == '$^&', f"Test 9 failed: got {result}, expected {'$^&'}"
        print(f"Test 9 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 9 failed: {e}")
        test_results.append(False)

    # Test case 10
    try:
        result = longestCommonSubsequence('1234567890', '24680')
        assert result == '24680', f"Test 10 failed: got {result}, expected {'24680'}"
        print(f"Test 10 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 10 failed: {e}")
        test_results.append(False)

    # Test case 11
    try:
        result = longestCommonSubsequence('a1b2c3d4', 'zz1yy2xx3')
        assert result == '123', f"Test 11 failed: got {result}, expected {'123'}"
        print(f"Test 11 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 11 failed: {e}")
        test_results.append(False)

    # Test case 12
    try:
        result = longestCommonSubsequence('racecar', 'carrace')
        assert result == 'race', f"Test 12 failed: got {result}, expected {'race'}"
        print(f"Test 12 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 12 failed: {e}")
        test_results.append(False)

    # Test case 13
    try:
        result = longestCommonSubsequence('subsequence', 'sbsqnc')
        assert result == 'sbsqnc', f"Test 13 failed: got {result}, expected {'sbsqnc'}"
        print(f"Test 13 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 13 failed: {e}")
        test_results.append(False)

    # Test case 14
    try:
        result = longestCommonSubsequence('sbsqnc', 'subsequence')
        assert result == 'sbsqnc', f"Test 14 failed: got {result}, expected {'sbsqnc'}"
        print(f"Test 14 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 14 failed: {e}")
        test_results.append(False)

    # Test case 15
    try:
        result = longestCommonSubsequence('🙂🙃🙂🙃', '🙃🙂')
        assert result == '🙃🙂', f"Test 15 failed: got {result}, expected {'🙃🙂'}"
        print(f"Test 15 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 15 failed: {e}")
        test_results.append(False)

    # Test case 16
    try:
        result = longestCommonSubsequence('👨\u200d👩\u200d👧\u200d👦family', '👩\u200d👧fam')
        assert result == '👩\u200d👧fam', f"Test 16 failed: got {result}, expected {'👩\u200d👧fam'}"
        print(f"Test 16 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 16 failed: {e}")
        test_results.append(False)

    # Test case 17
    try:
        result = longestCommonSubsequence('مرحباالعالم', 'العلم')
        assert result == 'العلم', f"Test 17 failed: got {result}, expected {'العلم'}"
        print(f"Test 17 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 17 failed: {e}")
        test_results.append(False)

    # Test case 18
    try:
        result = longestCommonSubsequence('line1\nline2\nline3', 'ln1\nln3')
        assert result == 'ln1\nln3', f"Test 18 failed: got {result}, expected {'ln1\nln3'}"
        print(f"Test 18 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 18 failed: {e}")
        test_results.append(False)

    # Test case 19
    try:
        result = longestCommonSubsequence('col1\tcol2\tcol3', 'c1\tc3')
        assert result == 'c1\tc3', f"Test 19 failed: got {result}, expected {'c1\tc3'}"
        print(f"Test 19 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 19 failed: {e}")
        test_results.append(False)

    # Test case 20
    try:
        result = longestCommonSubsequence('XMJYAUZ', 'MZJAWXU')
        assert result == 'MJAU', f"Test 20 failed: got {result}, expected {'MJAU'}"
        print(f"Test 20 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 20 failed: {e}")
        test_results.append(False)

    # Test case 21
    try:
        result = longestCommonSubsequence('abc', 'bac')
        assert result == 'bc', f"Test 21 failed: got {result}, expected {'bc'}"
        print(f"Test 21 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 21 failed: {e}")
        test_results.append(False)

    # Test case 22
    try:
        result = longestCommonSubsequence('αβγδεζη', 'βδεζ')
        assert result == 'βδεζ', f"Test 22 failed: got {result}, expected {'βδεζ'}"
        print(f"Test 22 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 22 failed: {e}")
        test_results.append(False)

    # Test case 23
    try:
        result = longestCommonSubsequence('He said: "Lean\\\\4"', 'Lean\\\\4')
        assert result == 'Lean\\\\4', f"Test 23 failed: got {result}, expected {'Lean\\\\4'}"
        print(f"Test 23 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 23 failed: {e}")
        test_results.append(False)

    # Test case 24
    try:
        result = longestCommonSubsequence('abcabcabcabcabc', 'aaabbbccc')
        assert result == 'aaabbbc', f"Test 24 failed: got {result}, expected {'aaabbbc'}"
        print(f"Test 24 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 24 failed: {e}")
        test_results.append(False)

    # Test case 25
    try:
        result = longestCommonSubsequence('axbxcxdxexf', 'abcdef')
        assert result == 'abcdef', f"Test 25 failed: got {result}, expected {'abcdef'}"
        print(f"Test 25 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 25 failed: {e}")
        test_results.append(False)

    # Test case 26
    try:
        result = longestCommonSubsequence('abcde_x', 'ace')
        assert result == 'ace', f"Test 26 failed: got {result}, expected {'ace'}"
        print(f"Test 26 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 26 failed: {e}")
        test_results.append(False)

    # Test case 27
    try:
        result = longestCommonSubsequence('He said: "Lean\\\\4"', 'ace_x')
        assert result == 'ae', f"Test 27 failed: got {result}, expected {'ae'}"
        print(f"Test 27 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 27 failed: {e}")
        test_results.append(False)

    # Test case 28
    try:
        result = longestCommonSubsequence('a b c d e_x', 'abababab')
        assert result == 'ab', f"Test 28 failed: got {result}, expected {'ab'}"
        print(f"Test 28 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 28 failed: {e}")
        test_results.append(False)

    # Test case 29
    try:
        result = longestCommonSubsequence('abcde', 'ace_x 0')
        assert result == 'ace', f"Test 29 failed: got {result}, expected {'ace'}"
        print(f"Test 29 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 29 failed: {e}")
        test_results.append(False)

    # Test case 30
    try:
        result = longestCommonSubsequence('aaaa edge', 'bbaaa_x')
        assert result == 'aaa', f"Test 30 failed: got {result}, expected {'aaa'}"
        print(f"Test 30 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 30 failed: {e}")
        test_results.append(False)

    # Test case 31
    try:
        result = longestCommonSubsequence('aaaa_x', 'bbaaa')
        assert result == 'aaa', f"Test 31 failed: got {result}, expected {'aaa'}"
        print(f"Test 31 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 31 failed: {e}")
        test_results.append(False)

    # Test case 32
    try:
        result = longestCommonSubsequence('zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba', 'abc')
        assert result == 'ab', f"Test 32 failed: got {result}, expected {'ab'}"
        print(f"Test 32 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 32 failed: {e}")
        test_results.append(False)

    # Test case 33
    try:
        result = longestCommonSubsequence('baaaaaaaaaaaaaaaaaaa', 'cba')
        assert result == 'ba', f"Test 33 failed: got {result}, expected {'ba'}"
        print(f"Test 33 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 33 failed: {e}")
        test_results.append(False)

    # Test case 34
    try:
        result = longestCommonSubsequence('xyz_x', 'cba_x_x')
        assert result == 'x_x', f"Test 34 failed: got {result}, expected {'x_x'}"
        print(f"Test 34 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 34 failed: {e}")
        test_results.append(False)

    # Test case 35
    try:
        result = longestCommonSubsequence('axbxc edge', 'aaaa edge')
        assert result == 'a edge', f"Test 35 failed: got {result}, expected {'a edge'}"
        print(f"Test 35 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 35 failed: {e}")
        test_results.append(False)

    # Test case 36
    try:
        result = longestCommonSubsequence('ace_x 0', 'abxc_x')
        assert result == 'ac_x', f"Test 36 failed: got {result}, expected {'ac_x'}"
        print(f"Test 36 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 36 failed: {e}")
        test_results.append(False)

    # Test case 37
    try:
        result = longestCommonSubsequence('axbxc', 'abxc 1')
        assert result == 'abxc', f"Test 37 failed: got {result}, expected {'abxc'}"
        print(f"Test 37 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 37 failed: {e}")
        test_results.append(False)

    # Test case 38
    try:
        result = longestCommonSubsequence('axbxc edge', 'abxc')
        assert result == 'abxc', f"Test 38 failed: got {result}, expected {'abxc'}"
        print(f"Test 38 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 38 failed: {e}")
        test_results.append(False)

    # Test case 39
    try:
        result = longestCommonSubsequence('axbxc', 'cxba')
        assert result == 'xb', f"Test 39 failed: got {result}, expected {'xb'}"
        print(f"Test 39 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 39 failed: {e}")
        test_results.append(False)

    # Test case 40
    try:
        result = longestCommonSubsequence('axbxc', 'x_cxba')
        assert result == 'xc', f"Test 40 failed: got {result}, expected {'xc'}"
        print(f"Test 40 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 40 failed: {e}")
        test_results.append(False)

    # Test case 41
    try:
        result = longestCommonSubsequence('x_cxbxa', 'abxc_x')
        assert result == 'xcx', f"Test 41 failed: got {result}, expected {'xcx'}"
        print(f"Test 41 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 41 failed: {e}")
        test_results.append(False)

    # Test case 42
    try:
        result = longestCommonSubsequence('BATGGA', 'BYAXTXG')
        assert result == 'BATG', f"Test 42 failed: got {result}, expected {'BATG'}"
        print(f"Test 42 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 42 failed: {e}")
        test_results.append(False)

    # Test case 43
    try:
        result = longestCommonSubsequence('abxc', 'acegikmoqsuwy')
        assert result == 'ac', f"Test 43 failed: got {result}, expected {'ac'}"
        print(f"Test 43 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 43 failed: {e}")
        test_results.append(False)

    # Test case 44
    try:
        result = longestCommonSubsequence('egde ', ' edge')
        assert result == 'ede', f"Test 44 failed: got {result}, expected {'ede'}"
        print(f"Test 44 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 44 failed: {e}")
        test_results.append(False)

    # Test case 45
    try:
        result = longestCommonSubsequence('axbxc_x', 'a_x')
        assert result == 'a_x', f"Test 45 failed: got {result}, expected {'a_x'}"
        print(f"Test 45 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 45 failed: {e}")
        test_results.append(False)

    # Test case 46
    try:
        result = longestCommonSubsequence('a_x edge', 'a 0')
        assert result == 'a ', f"Test 46 failed: got {result}, expected {'a '}"
        print(f"Test 46 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 46 failed: {e}")
        test_results.append(False)

    # Test case 47
    try:
        result = longestCommonSubsequence('  lead and trail  ', 'baba_x edge')
        assert result == 'aa ', f"Test 47 failed: got {result}, expected {'aa '}"
        print(f"Test 47 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 47 failed: {e}")
        test_results.append(False)

    # Test case 48
    try:
        result = longestCommonSubsequence('abababab_x', 'baba 0')
        assert result == 'baba', f"Test 48 failed: got {result}, expected {'baba'}"
        print(f"Test 48 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 48 failed: {e}")
        test_results.append(False)

    # Test case 49
    try:
        result = longestCommonSubsequence('ab\x00cd\x00ef', 'abcabcabcabcabc_x')
        assert result == 'abc', f"Test 49 failed: got {result}, expected {'abc'}"
        print(f"Test 49 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 49 failed: {e}")
        test_results.append(False)

    # Test case 50
    try:
        result = longestCommonSubsequence('abababab edge', 'abcdef')
        assert result == 'abde', f"Test 50 failed: got {result}, expected {'abde'}"
        print(f"Test 50 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 50 failed: {e}")
        test_results.append(False)

    # Test case 51
    try:
        result = longestCommonSubsequence('abababab 0', 'baba_x edge 1 1')
        assert result == 'baba ', f"Test 51 failed: got {result}, expected {'baba '}"
        print(f"Test 51 passed")
        test_results.append(True)
    except Exception as e:
        print(f"Test 51 failed: {e}")
        test_results.append(False)

    # Test case 52
    try:
        result = longestCommonSubsequence('ABCdef', 'x_b edge')
        assert result == 'de', f"Test 52 failed: got {result}, expected {'de'}"
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
