import os 

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    print(text)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
main()