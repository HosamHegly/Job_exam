
def longer_than_n(words_string, n):
    """Returns all the words that are longer than n in the given string of words."""
    if len(words_string) < 1:
        return []  # Return an empty list if the string is empty

    words_list = []
    word = ""
    for char in words_string:  # extract words from string
        if char != " ":
            word += char
        else:
            if len(word) > n:  # if word longer than n then append to list
                words_list.append(word)
            word = ""

    # Check the last word collected after the loop
    if len(word) > n:
        words_list.append(word)
    return  words_list

def is_palindrome(word):
    """Check whether the passed string is a palindrome. If yes, returns True; otherwise, returns False."""
    word_length = len(word)
    if word_length <= 1: # if word is empty or contains 1 charachter then it's a palindrome
        return word
    else:
        reverse_word = ""
        for char_index, char in enumerate(word):  # copy the characters from the original word in reverse. it's also enough to just check until half the string length
            reverse_word += word[word_length - char_index - 1]
        return reverse_word == word  # check if the word is equal to it's reverse

if __name__ == "__main__":
    input_string = input("Enter a string of words: ")
    length_threshold = int(input("Enter a number to filter words longer than it: "))

    long_words = longer_than_n(input_string, length_threshold)
    print("Words longer than", length_threshold, "characters:", long_words)

    word_list = input_string.split()

    for word in word_list:
        if is_palindrome(word):
            print(f"'{word}' is a palindrome.")
        else:
            print(f"'{word}' is not a palindrome.")