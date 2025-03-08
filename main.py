def get_book_text(filepath):
    contents_of_file = []
    with open(filepath) as f:
        contents_of_file = f.read()
    return contents_of_file

def main():
   print(get_book_text("books/frankenstein.txt"))



main()