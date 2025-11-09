def main() -> None:
    """
    Считывает два списка и диапазон, выполняет преобразования.
    Диапазон: start_index и end_index (включительно) от 1 до N.
    """
    try:
        list1 = list(map(int, input().split()))
        list2 = list(map(int, input().split()))
        
        start_index = int(input()) - 1
        end_index = int(input()) - 1
        
        # Проверка корректности диапазона.
        if start_index < 0 or end_index >= len(list1) or start_index > end_index:
            print("Некорректный диапазон индексов")
            return
        
        # Извлекаем срез в обратном порядке.
        extracted_slice = list1[start_index:end_index+1][::-1]
        
        # Удаляем срез из первого списка.
        list1[start_index:end_index+1] = []
        
        # Добавляем ко второму списку.
        list2.extend(extracted_slice)
        
        print(list1)
        print(list2)
        
    except (ValueError, IndexError):
        print("Ошибка ввода данных")

if __name__ == "__main__":
    main()
