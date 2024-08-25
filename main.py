def main():
    path = "books/frankenstein.txt"
    text = None
    with open(path, "r") as f:
        text = f.read()

    print("--- Begin report of {path} ---")

    word_total = count_words(text)
    print(f"This book has {word_total} words.")

    letter_index = count_letters(text)
    sorted_by_frequency = sort_character_index_by_frequency(letter_index)
    print("List of letters sorted by frequency:")

    for position in sorted_by_frequency:
        print(f"  {position['letter']} - {position['count']}")

    print("--- End report ---")


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letter_index = {}
    lowered = text.lower()

    for letter in lowered:
        if not letter.isalpha():
            continue
        elif letter in letter_index:
            letter_index[letter] += 1
        else:
            letter_index[letter] = 1

    return letter_index


def sort_character_index_by_frequency(letter_index):
    listed = []

    for letter, count in letter_index.items():
        listed.append({"count": count, "letter": letter})

    listed.sort(key=lambda x: x["count"], reverse=True)

    return listed


main()
