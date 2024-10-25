def main():
    # Call to functions
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    sorted_chars = sort_characters_by_count(num_char)

    # Print statements
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    print_sorted_characters(sorted_chars)
    print("--- End of report ---")


# Function that is going to return a list of chars and count each letter
def get_num_char(text):
    chars = {}
    for c in text:
        # makes sure only letters in the alphabet are being counted
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                # If lowered is already in the dictionary it will add 1 to the count
                chars[lowered] += 1
            else:
                # This sets the initial count for each character identified
                chars[lowered] = 1
    return chars

# Function to sort the dictionary by the count of characters in descending order
def sort_characters_by_count(char_dict):
    # sorted returns a list of tuples, where each tuple is (key, value) sorted by the value
    sorted_chars = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_chars

# Function to print the sorted characters in a vertical list
def print_sorted_characters(sorted_chars):
    for char, count in sorted_chars.items():
        print(f"The '{char}' character was found {count} times")
        

# Function that is counting the number of words
def get_num_words(text):
    # this is creating a variable that will count the "words" while omitting whitespace
    words = text.split()
    return len(words)

# Function that is used to read the book file
def get_book_text(path_to_file):
    with open(path_to_file) as t:
        return t.read()

main()
