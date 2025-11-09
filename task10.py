def main() -> None:
    """
    Считывает две строки (целые числа
    через пробел) и диапазон, выполняет
    преобразования и выводит результаты.
    """
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))

    start_index = int(input()) - 1
    end_index = int(input()) - 1

    # Извлекает срез в обратном порядке.
    extracted_slice = list1[start_index:end_index + 1][::-1]

    # Удаляет срез, заменяя его пустым.
    list1[start_index:end_index + 1] = []

    # Добавляет извлечённые элементы к list2.
    list2.extend(extracted_slice)

    print(list1)
    print(list2)


if __name__ == "__main__":
    main()
