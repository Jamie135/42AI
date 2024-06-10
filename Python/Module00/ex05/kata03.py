kata = "The right format"


def main():
    # ce f-string indique que le champ sera de taille max 42
    # et que kata sera aligner a droite (>) des tirets '-'
    formatted_str = f"{kata:->42}"
    print(f"{formatted_str}", end="")


if __name__ == "__main__":
    main()
