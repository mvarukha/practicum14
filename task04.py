def main() -> None:
    """
    Получает строку, формирует список уникальных
    слов без знаков препинания и выводит его.
    """
    punct = ".,!?;:-()[]{}'\"...«»"
    words = [
        ''.join(char for char in word if char not in punct)
        for word in input().split()
    ]
    # Убираем пустые строки и сохраняем порядок.
    unique_words = list(dict.fromkeys(word for word in words if word))
    print(unique_words)


if __name__ == "__main__":
    main()
