import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]  #if user entered correct word.
    elif word.title() in data:
        return data[word.title()]  #if user entered "texas" this will check for "Texas" as well.
    elif word.upper() in data:
        return data[word.upper()]  #in case user enters words like USA or NATO
    elif len(get_close_matches(word, data.keys())) > 0:  #if get closest word.
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return "Word does not exist. Please double check it"
        else:
            return "I don't understand your input."
    else:
        return "Word does not exist. Please double check it."

word = input("Enter word : ")

output = translate(word)

if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)