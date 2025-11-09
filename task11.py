def main() -> None:
    """
    Считывает список и команду сдвига, выводит результат.
    """
    try:
        numbers_list = list(map(int, input().split()))
        command = input().strip()

        if not command or command[0] not in "RL" or not command[1:].isdigit():
            print("Некорректная команда.")
            return

        list_length = len(numbers_list)
        if list_length == 0:
            print([])
            return

        shift_amount = int(command[1:]) % list_length

        if command[0] == "R":
            result_list = (
                numbers_list[-shift_amount:] +
                numbers_list[:-shift_amount]
            )
        else:
            result_list = (
                numbers_list[shift_amount:] +
                numbers_list[:shift_amount]
            )

        print(result_list)
    except ValueError:
        print("Введены нецелые числа.")


if __name__ == "__main__":
    main()
