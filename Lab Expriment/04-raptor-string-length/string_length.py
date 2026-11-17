"""Python equivalent of the RAPTOR flowchart: find the length of a string
without using len() -- loop and count characters, as the flowchart does."""
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

if __name__ == "__main__":
    for t in ["hello", "RAPTOR", "", "lab experiment 4"]:
        print(f"Input: {t!r:22} Length: {string_length(t)}  (len() check: {len(t)})")
