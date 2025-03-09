from stats import get_word_count, character_count
def get_book_text(filepath):
    contents_of_file = []
    with open(filepath) as f:
        contents_of_file = f.read()
    return contents_of_file

def main():
   word_count = get_word_count(get_book_text("books/frankenstein.txt"))
   print(f"{word_count} words found in the document")
   print(character_count(get_book_text("books/frankenstein.txt")))

main()