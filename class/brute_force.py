from text_stats import *
from tqdm import tqdm
words_list = []
file = "shakespeare.txt"
with open(file, "r") as f:
    text = f.read()
    words_list = raw_text_to_clean_list(text)

unique_words = dict_count_words(words_list)
print(len(unique_words))
brute_force_dict = {}
for key,val in tqdm(unique_words):
    if key not in brute_force_dict:
        followers = dict_of_following_words(words_list, key)
        brute_force_dict[key] = dict(followers)

with open("followers.txt", 'w') as f:
    f.write(brute_force_dict)