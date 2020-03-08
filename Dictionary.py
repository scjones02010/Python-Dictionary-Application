import json #import json to read data
from difflib import get_close_matches #used to compare like words

data=json.load(open('./data/dictionary.json'))#loads the data into the script

print(type(data)) #checks the data type

def define_word(word): #instantiates the definition function
    word = word.lower() #makes the word lower case in order to 
    if word not in data: #checks if the word is in the data dictionary
        if len(get_close_matches(word, data.keys(), n=1, cutoff=0.8)):
            yn= input(f"Try {get_close_matches(word,data.keys())[0]}? Yes or No. ") #tells you the guess of the word
            if yn == 'Yes' or 'yes': #asks for confirmation of the word guess
                return data[get_close_matches(word,data.keys())[0]] #provides the definition of close word
            else:
                return f"Try different spelling or syntax." #informs you to check syntax
        else:
            return "Word is not in dictionary." #tells that the word is not in dictionary
    else:
        data[word] #provides the definition of the word

word = input('Enter word: ') #allows user to enter the word

print(define_word(word)) #returns the definitin of the word