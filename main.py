from stats import get_num_words, character_map_builder
import sys

def get_book_text(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        return data

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book_data = get_book_text(sys.argv[1])
    num_of_words = get_num_words(book_data)
    char_dict = character_map_builder(book_data)
    
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    
    for char in char_dict.keys():
        print(f"{char}: {char_dict[char]}")
    print("============= END ===============")
main()