def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)

    def dfs(s, start):

        if start == len(s):
            dp[-1] = True
            return

        if dp[start]:
            return 

        for word in wordDict:
            if s.startswith(word, start):
                dp[start] = True
                dfs(s, start + len(word))


    dfs(s, 0)
    return dp[-1]
    
    
tests = [
    ("leetcode", ["leet", "code"], True),
    ("applepenapple", ["apple", "pen"], True),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),

    ("a", ["a"], True),
    ("a", ["b"], False),

    ("aaaaaaa", ["aaaa", "aaa"], True),
    ("aaaaaaa", ["aaaa", "aa"], False),

    ("catskicatcats", ["cats","cat","dog","ski"], True),

    ("cars", ["car", "ca", "rs"], True),
    ("abcd", ["a", "abc", "b", "cd"], True),

    ("catsanddog", ["cat", "cats", "and", "sand", "dog"], True),

    ("pineapplepenapple",
     ["apple", "pen", "applepen", "pine", "pineapple"],
     True),

    ("aaaaaaaaaaaaaaaaab",
     ["a", "aa", "aaa", "aaaa", "aaaaa"],
     False),

    ("hellohello", ["hello"], True),

    ("goalspecial", ["go", "goal", "goals", "special"], True),
]


for s, wordDict, expected in tests:
    result = wordBreak(s, wordDict)

    print(f"s={s!r}")
    print("wordDict:", wordDict)
    print("result:", result)
    print("expected:", expected)
    print("correct:", result == expected)
    print()