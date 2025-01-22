def get_book():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()
    return file_contents

def get_word_count(file_contents) :
        words = file_contents.split()
        word_count = len(words) 
        return word_count 

def get_character_count(book_text):
    character_count = {}
    for character in book_text :
        lowered = character.lower()
        if lowered in character_count :
            character_count[lowered] +=1
        else:
            character_count[lowered] = 1
    return character_count

def print_report(character_count,word_count,) :
    pass
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    for character in character_count :
        print(f"The '{character}' character was found {character_count[character]} times")
    print("")
    print("--- End report ---")

def main():
    get_book()
    get_word_count(file_contents=get_book())
    get_character_count(book_text=get_book())
    print_report(character_count=get_character_count(book_text=get_book()),word_count=get_word_count(file_contents=get_book()))
    
main()

