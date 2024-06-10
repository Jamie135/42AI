import sys


def main():
    if len(sys.argv) == 1:
        return
    else:
        str = ''.join(sys.argv[1:])
        res = str[::-1].swapcase()
        print(res)


if __name__ == "__main__":
    main()


# sys est un module qui permet l'acces aux arguments passe dans la commande

# [start:stop:step] est une slice notation
# step = -1 signifie qu'on commence depuis la fin de la sequence
