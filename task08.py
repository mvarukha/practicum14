def sort_string_characters(input_string: str) -> str:
    """
    Преобразует строку в список символов,
    сортирует его и возвращает строку.
    """
    return "".join(sorted(input_string))


def main() -> None:
    """
    Считывает строку и выводит её с
    отсортированными символами.
    """
    print(sort_string_characters(input()))


if __name__ == "__main__":
    main()
