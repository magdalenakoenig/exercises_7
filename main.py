import nltk
from nltk.corpus import wordnet
from nltk.corpus import names

#nltk.download('wordnet')
#nltk.download('names')
#nltk.download("omw-1.4")                   # pycharm raised an error and told me to download this; not really sure what it does tho

import random                               # importing random so i can use the shuffle function later

def generate_names(char, num):
    if isinstance(char, str):
        if char.isalpha == False:           # wordnet found names for every letter of the alphabet, so i implemented it this way instead of checking the length
            print("no names were found")
        else:
            female_names = names.words('female.txt')
            female_names_list = []
            for name in female_names:
                if name.startswith(char):   # appending to the list of names if the name starts with the char argument
                    female_names_list.append(name)
            random.shuffle(female_names_list)

            male_names = names.words("male.txt")
            male_names_list = []
            for name in male_names:         # same code as for the female names
                if name.startswith(char):
                    male_names_list.append(name)
            random.shuffle(male_names_list)

            print("Female and male names in the names corpus that start with " + char + ":")
            print("female: {}".format(female_names_list[0:num]))
            print("male: {}".format(male_names_list[0:num]))    # formatting the output

    else:
        raise TypeError("The input is not a string.")           # raising a type error if a different data type than string is typed in as an argument

    with open("female_names.txt", "w") as female:
        for name in female_names_list[0:num]:                   # creating output files for both female and male name lists
            female.write(name + "\n")

    with open("male_names.txt", "w") as male:
        for name in male_names_list[0:num]:
            male.write(name + "\n")


print(generate_names("J", 7))


class SynAnt:
    def __init__(self, wordlist):
        self.wordlist = wordlist

    def find_synonyms(self):
        for word in self.wordlist:
            if isinstance(word, str):                   # checking if input is string
                synonyms = []
                for syn in wordnet.synsets(word):       # appending synonyms to list like in example code
                    for l in syn.lemmas():
                        synonyms.append(l.name())
                if len(synonyms) == 0:                  # if there are no synonyms, the list just says "no synonyms found"
                    synonyms.append("No synonyms found")
                else:
                    print("synonyms of {}: {}".format(word, set(synonyms)))   # if there are synonyms, they are printed
            else:
                raise TypeError("One or more inputs is/are not a string.")  # if input is not a string, a type error is raised


    def find_antonyms(self):                                # using a similar code to the find_synonyms function; also based on example code
        for word in self.wordlist:
            if isinstance(word, str):
                antonyms = []
                for syn in wordnet.synsets(word):
                    for l in syn.lemmas():
                        if l.antonyms():
                            antonyms.append(l.antonyms()[0].name())
                if len(antonyms) == 0:
                    antonyms.append("No antonyms found")
                else:
                    print("antonyms of {}: {}".format(word, set(antonyms)))
            else:
                raise TypeError("One or more inputs is/are not a string.")



word1 = SynAnt(["dry", "wet"])
print(word1.find_synonyms())
print(word1.find_antonyms())