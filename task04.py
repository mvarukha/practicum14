def main() -> None:
    """
    Получает строку, формирует список уникальных
    слов без знаков препинания и выводит его.
    """
    punct = ".,!?;:-()[]{}'\"...«»"
    words = [word.strip(punct) for word in input().split()]
    seen_words = set()
    unique_list = []
    for word in words:
        if word and word not in seen_words:
            unique_list.append(word)
            seen_words.add(word)
    print(unique_list)


if __name__ == "__main__":
    main()
