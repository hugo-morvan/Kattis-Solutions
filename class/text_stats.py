#!/usr/bin/env python3

# To run the script : chmod u+x text_stats.py shakespeare.txt
def raw_text_to_clean_list(text):
    """Converts a string of text to a list of words, without upper case letters, punctuation or line breaks."""
    cleaned_text = text.lower()
    cleaned_text = cleaned_text.replace("\n", " ")
    cleaned_text = cleaned_text.replace(",", "")
    cleaned_text = cleaned_text.replace(".", "")
    cleaned_text = cleaned_text.replace(";", "")
    cleaned_text = cleaned_text.replace(":", "")
    cleaned_text = cleaned_text.replace("?", "")
    cleaned_text = cleaned_text.replace("!", "")
    cleaned_text = cleaned_text.split(" ")
    cleaned_text = list(filter(lambda x: x != "", cleaned_text))
    return cleaned_text

#Letters stats
def count_total_letters(letter_dict):
    """returns the total number of (alpha only) letters in a letter_count dict"""
    count = 0
    for key, val in letter_dict:
        if str(key).isalpha():
            count += val
    return count

def dict_count_letters(list_of_words):
    """Given a (cleaned) list of words, returns a dictionary with letter count, ordered by count."""
    letter_frequencies = {}
    for word in list_of_words:
        for letter in word:
            if str(letter).isalpha():
                if letter in letter_frequencies:
                    letter_frequencies[letter] += 1
                else:
                    letter_frequencies[letter] = 1

    letter_frequencies = sorted(letter_frequencies.items(), key=lambda x: x[1], reverse=True)
    return letter_frequencies

def print_letter_count_data(dict, num_rows):
    """Given a dict of letter frequencies, present the first num_rows of data into a nice looking print"""
    num_letters = count_total_letters(dict)
    for row in range(num_rows):
        k, val = dict[row]
        freq = val/num_letters
        print(f"rank: {row+1}, letter: {k}, frequency: {freq:.3}")

#Words stats
def count_total_words(word_dict):
    """returns the total number of (alpha only) words in a word_count dict"""
    count = 0
    for key, val in word_dict:
        if key.isalpha():
            count += val
    return count

def dict_count_words(list_of_words):
    """Given a (cleaned) list of words, returns a dictionary with word count, ordered by count."""
    word_frequencies = {}
    for word in list_of_words:
        if word.isalpha():
            if word in word_frequencies:
                word_frequencies[word] += 1
            else:
                word_frequencies[word] = 1

    word_frequencies = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)
    return word_frequencies

def count_unique_words(list_of_words):
    return len(dict_count_words(list_of_words))

def print_word_count_data(dict, words_list, num_rows):
    """Given a dict of word frequencies, present the first num_rows of data into a nice looking print"""
    num_words = count_total_words(dict)
    for row in range(num_rows):
        k, val = dict[row]
        freq = val/num_words
        print(f"rank: {row+1}, word: {k}, frequency: {freq:.3}")
        followers_dict = dict_of_following_words(words_list, my_word = k)
        for fol in range(3):
            follower, occ = followers_dict[fol]
            print(f"----------------- {follower}, occurences: {occ}")
        

def dict_of_following_words(words_list, my_word):
    """Given a word and a list of words, return a dict of the words most commonly following the input word, and the number of occurences"""
    count=0
    followers_frequencies = {}
    indices = [i for i, x in enumerate(words_list) if x == my_word]
    for index in indices:
        follower = words_list[index+1]
        if follower in followers_frequencies:
            followers_frequencies[follower] += 1
        else:
            followers_frequencies[follower] = 1
    
    followers_frequencies = sorted(followers_frequencies.items(), key=lambda x: x[1], reverse=True)
    return followers_frequencies

#-----------Main---------------
def main():
    import sys
    print(sys.argv)
    if (len(sys.argv) <= 1):
        print("Missing file location.")
        print("Try ./text_stats.py <filename>")
    else:
        file = sys.argv[1]
        print(f"Analysing file {file}.")

        #### Script logic starts here ###

        with open(file, "r") as f:
            # Opening the file
            text = f.read()

            # Converting raw tax into a cleaned list of words (all lowercase)
            words_list = raw_text_to_clean_list(text)

            print("\nLetter frequencies:")
            print_letter_count_data(dict = dict_count_letters(words_list), num_rows = 26)

            print("\nWord count:")
            print(f"Found {count_total_words(dict_count_words(words_list))} words in {file}")

            print("\nUnique words count")
            print(f"There are {count_unique_words(words_list)} uniques words in {file}")

            print("\nMost common words:")
            print_word_count_data(dict = dict_count_words(words_list), words_list=words_list, num_rows = 5)

        ###############################
    return 0

if __name__ == "__main__":
    print("Script called directly")
    main()
else:
    print("I was imported")
    main()