import sys
import string


def filter(s, n):
    try:
        words = s.split()
        # create a set of all punctuation character
        punctuations = set(string.punctuation)
        filtered = []
        for word in words:
            cleaned_word = "".join(c for c in word if c not in punctuations)
            if len(cleaned_word) > n:
                filtered.append(cleaned_word)
        filtered = list(dict.fromkeys(filtered))
        print(filtered)
    except Exception as e:
        print("ERROR")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("ERROR")
    else:
        try:
            n = int(sys.argv[2])
            filter(sys.argv[1], n)
        except ValueError:
            print("ERROR")
