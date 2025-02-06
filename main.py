def main():
    # put your file reading code here
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)

        # counting characters
        character_count = {}
        string_lower = file_contents.lower()
        for char in string_lower:
            character_count[char] = character_count.get(char, 0) + 1

        # converting the list of dictionaries
        char_list = list(character_count.items())
        alpha_chars = []
        for letter in char_list:
            if letter[0].isalpha():
                char_dict = {"name": letter[0], "num": letter[1]}
                alpha_chars.append(char_dict)

        def sort_on(alpha_chars):
            return alpha_chars["num"]
        
        alpha_chars.sort(reverse=True, key=sort_on)


    


    
    # after reading the file, print the contents
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char_dict in alpha_chars:
        print(f"The '{char_dict['name']}' character was found {char_dict['num']} times")

    print("--- End report ---")
# This line calls your main function when the program runs
main()