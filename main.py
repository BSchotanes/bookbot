from stats import get_word_count, character_count, sort_dictonary

def get_book_text(filepath):
    contents_of_file = []
    with open(filepath) as f:
        contents_of_file = f.read()
    return contents_of_file

def main():
    path = "books/frankenstein.txt"
    booktext = get_book_text(path)
    word_count = get_word_count(booktext)
    counted_characters = character_count(booktext)
    chars_sorted = sort_dictonary(counted_characters)
    print(f"{word_count} words found in the document")

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print only alphabetical characters
    for char_dict in chars_sorted:
        char = char_dict["char"]
        if char.isalpha():  # Only print alphabetical characters
            count = char_dict["count"]
            print(f"{char}: {count}")
    
    print("============= END ===============")
main()