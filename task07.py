def main() -> None:
    """
    Считывает список целых чисел и выводит
    сумму чётных и сумму нечётных элементов.
    """
    try:
        nums = list(map(int, input().split()))
        sum_even = sum(n for n in nums if n % 2 == 0)
        sum_odd = sum(n for n in nums if n % 2)
        print(sum_even, sum_odd)
    except ValueError:
        print("Введены нецелые числа или некорректные данные.")


if __name__ == "__main__":
    main()
