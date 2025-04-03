from collections import Counter

def get_book_wordnum(book_content):
    split_book_content = book_content.split()
    return len(split_book_content)

def get_book_characternum(book_content):
    lower_book_content = book_content.lower()
    list_book_char = list(lower_book_content)
    char_counts = Counter(list_book_char)
    return char_counts

def sort_charcounts(char_counts):

    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "count": count})
        
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    
    return char_list