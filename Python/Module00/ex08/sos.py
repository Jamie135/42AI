import sys


# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}


def morse(text):
    encoded = ""
    for c in text.upper():
        if c in morse_code:
            encoded += morse_code[c] + ' '
        else:
            return "ERROR"
    # strip removes all leading and trailing spaces
    return encoded.strip()


def main():
    args = " ".join(sys.argv[1:])
    if args:
        print(morse(args))
    else:
        print("Usage: python3 sos.py \"your text here\"")


if __name__ == "__main__":
    main()
