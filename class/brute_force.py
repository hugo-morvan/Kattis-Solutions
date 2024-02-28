"""
Short scrript to create a dictionary of followers for each word in the text
"""

from text_stats import *
from tqdm import tqdm

words_list = []
file = "shakespeare.txt"
with open(file, "r", encoding="utf-8") as f:
    text = f.read()
    words_list = raw_text_to_clean_list(text)

brute_force_dict = {}
for word in tqdm(words_list):
    if word not in brute_force_dict:
        followers = dict_of_following_words(words_list, word)
        brute_force_dict[word] = dict(followers)

with open("followers.txt", 'w', encoding='utf-8') as f:
    f.write(str(brute_force_dict))