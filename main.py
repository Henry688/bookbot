from stats import get_book_words_count, sort_dict
import sys


# book = "./books/frankenstein.txt"

def main():
    if len(sys.argv) > 1:
        book = sys.argv[1]
        word_count = get_book_words_count(book)
        character_count = sort_dict(book)
        print(
            "============ BOOKBOT ============\n"
            f"Analyzing book found at {book}\n"
            "----------- Word Count ----------\n"
            +word_count+"\n"
            "--------- Character Count -------\n"
        )
        for character in character_count:
            if character["character"].isalpha():
                print(f"{character["character"]}: {character["count"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
