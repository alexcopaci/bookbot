import sys
from stats import word_count, char_count, chars_dict_to_sorted_list

def get_book_text(filepath): 
    with open(filepath) as f: 
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    # Get the book's text
    book_text = get_book_text(book_path)

    # Count the words 
    how_many_words = word_count(book_text)
    char_counts = char_count(book_text)
    sorted_chars = chars_dict_to_sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {how_many_words} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
