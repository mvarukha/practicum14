import string


def main() -> None:
    """
    Считывает текст до пустой строки, выводит
    слова по частоте и по их порядку.
    """
    input_lines = []
    while True:
        line = input()
        if not line:
            break
        input_lines.append(line)

    words = " ".join(input_lines).split()
    cleaned_words = [
        word.strip(string.punctuation).lower()
        for word in words
        if word.strip(string.punctuation)
    ]

    word_order = []
    word_count = {}
    word_index = {}  # Сохраняем индекс первого появления.
    index_counter = 0

    for word in cleaned_words:
        if word not in word_count:
            word_order.append(word)
            word_count[word] = 0
            word_index[word] = index_counter
            index_counter += 1
        word_count[word] += 1

    sorted_words = sorted(
        word_order,
        key=lambda word: (-word_count[word], word_index[word])
    )

    for word in sorted_words:
        print(word)


if __name__ == "__main__":
    main()
