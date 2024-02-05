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

        generated_text = []
           

        #4) print generated words.
        print("Generation took --- %s seconds ---" % (time.time() - start_time))
        print("Here is the generated text : ")
        print("------------------------")
        print(*[word for word in generated_text])
        print("------------------------")

    return 0

if __name__ == "__main__":
    print("generate_text.py called directly")
    main()
else:
    print("generate_text.py was imported")
    main()