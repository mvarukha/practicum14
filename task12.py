def is_valid_word(word: str) -> bool:
    """
    Проверяет, что слово состоит только из строчных букв.
    """
    return word.islower() and word.isalpha()


def count_holes(word: str) -> int:
    """
    Считает количество букв с отверстиями в слове.
    """
    return sum(char in "abdegopq" for char in word)


def main() -> None:
    """
    Считывает строку, выводит количество букв с отверстиями и без,
    а также список слов, в которых две и более буквы с отверстиями.
    """
    input_text = input()
    words = input_text.split()

    for word in words:
        if not is_valid_word(word):
            print("Ввод должен содержать только строчные буквы.")
            return

    word_holes = {word: count_holes(word) for word in words}

    all_holes = sum(word_holes[word] for word in words)
    all_no_holes = sum(len(word) - word_holes[word] for word in words)
    print(all_holes, all_no_holes)

    words_with_two_or_more_holes = [
        word for word in words if word_holes[word] >= 2
    ]

    print(words_with_two_or_more_holes)


if __name__ == "__main__":
    main()
