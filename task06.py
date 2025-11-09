def main() -> None:
    """
    Считывает целое число и выводит
    список его делителей.
    """
    try:
        number = int(input())
        if number == 0:
            print([])
            return
        abs_number = abs(number)
        divisors = [i for i in range(1, abs_number + 1) if abs_number % i == 0]
        print(divisors)
    except ValueError:
        print("Введено нецелое число.")


if __name__ == "__main__":
    main()
