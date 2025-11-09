def main() -> None:
    """
    Получает строку, формирует список слов 
    без знаков препинания и выводит его.
    """
    punct = ".,!?;:-()[]{}'\"...«»"
    result = [
        word.strip(punct)
        for word in input().split()
    ]
    print(result)


if __name__ == "__main__":
    main()
