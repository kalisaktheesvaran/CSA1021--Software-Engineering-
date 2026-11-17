"""Lexicographically smallest string obtainable by swapping exactly two characters
(at most one swap). Greedy: find first position i where a smaller char exists later,
swap it with the LAST occurrence of the smallest such char."""
def smallest_after_one_swap(s):
    a = list(s)
    n = len(a)
    for i in range(n):
        m = min(a[i:])
        if m < a[i]:
            j = n - 1 - a[::-1].index(m)   # last occurrence of the minimum
            a[i], a[j] = a[j], a[i]
            return "".join(a)
    return s  # already smallest

if __name__ == "__main__":
    for t in ["dcba", "abcd", "bca", "zyxw", "cbaab", "a"]:
        print(f"{t!r:8} -> {smallest_after_one_swap(t)!r}")
