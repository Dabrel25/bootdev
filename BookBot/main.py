from stats import get_book_wordnum
import os 

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    length = get_book_wordnum(text)
    print(f"{length} words found in the document")

def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return book_content
    
main()