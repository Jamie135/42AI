kata = (19, 42, 21)


if __name__ == "__main__":
    # map applique la fonction str (conversion en string) sur tous l'iterable kata
    print(f"The {len(kata)} numbers are: {', '.join(map(str, kata))}")
