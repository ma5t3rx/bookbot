import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
filepath = sys.argv[1]
def main(): 
    book_text = get_book_text(filepath)
    from stats import count_words, count_characters, sort_dict
    word_count = count_words(book_text)
    chars_dict = count_characters(book_text)
    sorted_chars = sort_dict(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)
def num_of_words(filepath):
    num_words = 0
    book = "Hello"
    with open(filepath) as f:
        book = f.read()
        return book
main()
