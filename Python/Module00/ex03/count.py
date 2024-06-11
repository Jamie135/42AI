import sys


def text_analyzer(text=None):

    # docstring
    """
    This function counts the number of upper characters, lower characters,
    punctuation, and spaces in a given text.
    """

    if text is None:
        text = input("What is the text to analyze?\n")

    if not isinstance(text, str):
        print("Error: argument is not a string")
        return

    upper = 0
    lower = 0
    space = 0
    punctuation = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            space += 1
        else:
            punctuation += 1

    print(f"The text contains {len(text)} character(s):")
    print(f"- {upper} upper letter(s)")
    print(f"- {lower} lower letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {space} space(s)")


# if __name__ == "__main__":
#     text_analyzer("Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.")
#     text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")
#     text_analyzer()
#     text_analyzer(42)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Error: too many arguments")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        text_analyzer()
