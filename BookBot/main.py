from stats import get_book_wordnum
from stats import get_book_characternum
from stats import sort_charcounts
import sys 

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    length = get_book_wordnum(text)
    char_counts = get_book_characternum(text)
    sorted_chars = sort_charcounts(char_counts)
    format_textreport(filepath,length, sorted_chars)

    


def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
        return book_content

def format_textreport(filepath, length, sorted_chars):
    print(f"""
============ BOOKBOT ============ 
Analyzing book found at {filepath}...
----------- Word Count ----------
Found {length} total words
--------- Character Count -------""")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
main()