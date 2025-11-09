def main() -> None:
    """
    Считывает список целых чисел, вычисляет
    и выводит их среднее значение.
    """
    try:
        nums = list(map(int, input().split()))
        if not nums:
            print("Список пуст.")
            return
        print(sum(nums) / len(nums))
    except ValueError:
        print("Введены некорректные данные.")


if __name__ == "__main__":
    main()
