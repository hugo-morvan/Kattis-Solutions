#!/usr/bin/env python3

from text_stats import *
import sys
import random
import time
from tqdm import tqdm

def main():
    if (len(sys.argv) < 4):
        print("Missing 1 or more arguments")
        print("Try ./text_stats.py <filename> <starting word> <max number of words>")
    else:
        file = sys.argv[1]
        start_word = sys.argv[2]
        max_token = int(sys.argv[3])
        print(f"Using file '{file}' to generate {max_token} words, starting from the word '{start_word}'.")
        start_time = time.time()

        #1) Get text and process it
        words_list = []
        with open(file, "r") as f:
            text = f.read()
            words_list = raw_text_to_clean_list(text)
        
        #Idea : use memoization to speedup the generation of the text.
        last_word = start_word
        seen_words = {}
        token = 0
        memo_count = 0
        while token < max_token:
            last_word_followers = {}

            #Memoization :
            if last_word not in seen_words.keys():
                last_word_followers = dict_of_following_words(words_list, last_word)
                seen_words[last_word] = last_word_followers
                memo_count += 1
            else:
                last_word_followers = seen_words[last_word]

            last_word_followers = dict(last_word_followers)
            num_followers = sum([val for val in last_word_followers.values()])
            tup = list(last_word_followers.items())
            pop, wei = zip(*tup)
            next_word = random.choices(population = pop, weights = wei)[0]
            print(next_word, end=' ')
            last_word = next_word
            token += 1
        print()
        print("Generation took --- %s seconds ---" % (time.time() - start_time))
        print(f"Memoization dict used {memo_count} times")
    return 0

if __name__ == "__main__":
    print("generate_text.py called directly")
    main()
else:
    print("generate_text.py was imported")
    main()