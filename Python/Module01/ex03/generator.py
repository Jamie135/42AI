import random


def fisher_yates_shuffle(words):
    n = len(words)
    for i in range(n - 1, 0, -1):
        r = random.randint(0, i)
        words[i], words[r] = words[r], words[i]


def generator(text, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
    option precise if a action is performed to the substrings before it is yielded.
    """

    # check validity for text and option
    if not isinstance(text, str):
        yield "ERROR"
        return
    
    valid_option = [None, "shuffle", "unique", "ordered"]
    if option not in valid_option:
        yield "ERROR"
        return
    
    # split the text with sep
    words = text.split(sep)

    # apply passed option on our splited list
    if option == "ordered":
        words = sorted(words)
    elif option == "shuffle":
        fisher_yates_shuffle(words)
    elif option == "unique":
        seen = set() # keep track of words that have already been encountered
        unique_words = []
        for word in words:
            if word not in seen:
                seen.add(word)
                unique_words.append(word)
        words = unique_words
    
    for w in words:
        yield w


# text = "Le Lorem Ipsum est simplement du faux texte."
# print("Default split:")
# for word in generator(text, sep=" "):
#     print(word)

# print("\nShuffle option:")
# for word in generator(text, sep=" ", option="shuffle"):
#     print(word)

# print("\nOrdered option:")
# for word in generator(text, sep=" ", option="ordered"):
#     print(word)

# text = "Lorem Ipsum Lorem Ipsum"
# print("\nUnique option:")
# for word in generator(text, sep=" ", option="unique"):
#     print(word)

# print("\nError cases:")
# text = 1.0
# for word in generator(text, sep="."):
#     print(word)

# text = "Le Lorem Ipsum est simplement du faux texte."
# for word in generator(text, sep=" ", option="invalid"):
#     print(word)
