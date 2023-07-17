# Import openai and regex libraries
import tiktoken
import openai
import os
import regex as re
# Get API_KEY
api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

# Open and read the file, then close the file. 
list_content = ["a","b","c", "d","e","f", "g","h", "i","j","k","l","m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
list_consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
quick_fox = "a quick brown fox jumps over the lazy dog"
vowel = "a e i o u"
consonants = "b c d f g h j k l m n p q r s t v w x y z"

encoding = tiktoken.encoding_for_model("davinci")
encoded_vowel = encoding.encode(vowel)
decoded_vowel = encoding.decode(encoded_vowel)
num_vow_tokens = len(encoded_vowel)
encoded_consonants = encoding.encode(consonants)
decoded_consonants = encoding.decode(encoded_consonants)
num_cons_tokens = len(encoded_consonants)
encoded_sentence = encoding.encode(quick_fox)
num_sent_tokens = len(encoded_sentence)
decoded_sentence = encoding.decode(encoded_sentence)

print(f"""\n
      Here are the vowels:\t {decoded_vowel}\n
      Here they are encoded:\t {encoded_vowel}\n
      Here are the number of tokens: \t {num_vow_tokens}\n
      Here are the consonants:\t {decoded_consonants}\n
      Here are the number of tokens: \t {num_cons_tokens}\n
      Here they are encoded:\t {encoded_consonants}\n
      Here is the sentence:\t {decoded_sentence}\n
      Here it is encoded:\t {encoded_sentence}\n
      Here are the # of tokens: \t {num_sent_tokens}\n
      """)
screen_input = input("Enter a lettter, word, or a sentence:")
print(screen_input)
encoded_screen_input = encoding.encode(screen_input)
decoded_screen_input = encoding.decode(encoded_screen_input)
num_screen_tokens = len(screen_input)
print(f"""\n{encoded_screen_input}\n{decoded_screen_input}\n{num_screen_tokens}\n""")










for index, alphabets in enumerate(list_content):
    encoded_list = encoding.encode(alphabets)
    # print(index, alphabets,encoded_list)
 
for index, consonants in enumerate(list_consonant):
    encoded_list_consonant = encoding.encode(consonants)
    # print(index, consonants, encoded_list_consonant)