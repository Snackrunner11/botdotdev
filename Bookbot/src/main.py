import sys
from stats import *

def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        else:
            Filepath = sys.argv[1]
    except:
        sys.exit(1)

    file_contents = get_book_text(Filepath)
    num_words = words_in_book(file_contents)
    text = get_book_text(Filepath)
    letters = letter_count(text)
    list_with_dict = dict_to_list_with_dicts(letters)
    sorted_list = sort_biggest_to_smallest(list_with_dict)
    text_word_total = f"Found {num_words} total words"
    
    print (f"""
    ============ BOOKBOT ============
    Analyzing book found at {Filepath}...
    ----------- Word Count ----------
    {text_word_total}
    """)
    for item in sorted_list:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")
    print("""============= END ===============""")


main()