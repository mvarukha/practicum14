def main() -> None:
    """
    Считывает 10 чисел, создает новый список
    из сумм соседних элементов и выводит его.
    """
    input_numbers = [int(input()) for _ in range(10)]
    print([input_numbers[ind] + input_numbers[ind + 1] for ind in range(8)])


if __name__ == "__main__":
    main()
