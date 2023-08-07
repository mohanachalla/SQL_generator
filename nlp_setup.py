#nlp= Natural language processing 
#Tokenization of the user input into words or phrases.
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

user_input = input("Enter your natural language query: ")
tokens = word_tokenize(user_input)
