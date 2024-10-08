def main():
    book = "./books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        print(file_contents)

        print("--------------------------------------------------------")
        print(f"------  Begin report of {book}  ------")

        # counting the words and chars in the file, then printing word count
        word_count = len(file_contents.split())
        print(f"{word_count} words found in the document")
        print()
        char_count(book)

def char_count(book):
    with open(book) as f:
        file_contents = f.read()
        char_dict = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
            'e': 0,
            'f': 0,
            'g': 0,
            'h': 0,
            'i': 0,
            'j': 0,
            'k': 0,
            'l': 0,
            'm': 0,
            'n': 0,
            'o': 0,
            'p': 0,
            'q': 0,
            'r': 0,
            's': 0,
            't': 0,
            'u': 0,
            'v': 0,
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0
        }

        # taking every char in the file and adding it to the dictionary for easy count
        for char in file_contents.lower():
            if char in char_dict:
                char_dict[char] += 1

        # ordering chars in the dictionary by the number of counts descending
        sorted_chars = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)

        # printing out the results in a loop
        for char, count in sorted_chars:
            print(f"The '{char}' character was found {count} times")
        print("-------------------- End report ------------------------")

main()