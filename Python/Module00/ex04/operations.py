import sys


def operations(A, B):
    try:
        A = int(A)
        B = int(B)
    except ValueError:
        print("AssertionError: only integers are allowed")
        return

    sum_result = A + B
    print(f"Sum: {sum_result}")

    difference_result = A - B
    print(f"Difference: {difference_result}")

    product_result = A * B
    print(f"Product: {product_result}")

    try:
        quotient_result = A / B
        print(f"Quotient: {quotient_result}")
    except ZeroDivisionError:
        print("Quotient: ERROR (division by zero)")

    try:
        remainder_result = A % B
        print(f"Remainder: {remainder_result}")
    except ZeroDivisionError:
        print("Remainder: ERROR (modulo by zero)")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python operations.py <number1> <number2>")
        print("Example:")
        print("python operations.py 10 3")
    elif len(sys.argv) != 3:
        print("AssertionError: too many or too few arguments")
    else:
        _, A, B = sys.argv
        operations(A, B)
