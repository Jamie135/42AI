import sys


def main():
    if len(sys.argv) == 1:
        return
    else:
        joined = ''.join(sys.argv[1:])
        res = joined[::-1].swapcase()
        print(res)


if __name__ == "__main__":
    main()


# sys est un module qui permet l'acces aux arguments passe dans la commande

# [start:stop:step] est une slice notation
# step = -1 signifie qu'on commence depuis la fin de la sequence
