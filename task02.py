def main() -> None:
    """
    Считывает список целых чисел, удаляет первое
    вхождение значения 3 и выводит новый список.
    """
    input_numbers = list(map(int, input().split()))

    if input_numbers.count(3) != 1:
        print("В списке должно быть ровно одно значение 3.")
        return

    input_numbers.remove(3)
    print(input_numbers)


if __name__ == "__main__":
    main()
