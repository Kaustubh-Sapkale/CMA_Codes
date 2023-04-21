import random
import sys

###  Exception ###
class InvalidStartWord(Exception):
    #exception when the first word given as argument is not available in sample text .
    pass

class TextGenerator:
    def __init__(self):
        self.prefix_dict = {}
    
    def assimilateText(self, FileName):             #basically assimilate test will create a dictionary of tuple-to-list of words where tuple is key for the list of words.
        with open(FileName, 'r') as file:
            text = file.read()
            words = text.split()
            for i in range(len(words) - 2):
                prefix = (words[i], words[i+1])
                if prefix in self.prefix_dict:                          #This will check if the current tuple of words is already present in dictionary or not. if present then append the next word in the list else make a new key 
                    self.prefix_dict[prefix].append(words[i+2])
                else:
                    self.prefix_dict[prefix] = [words[i+2]]
    
    def generateText(self, numWord, startword = None ):
        Text = ""
        if self.prefix_dict is {}:
            print("Waiting to assimilate Text")

        try:
            if startword is not None and startword not in [i[0] for i in self.prefix_dict.keys()]:                  
                raise InvalidStartWord  
        except InvalidStartWord:
            print("<class 'Exception'>\nUnable to produce text with the specified start word.")
            sys.exit()

        if startword is None:                                                   #if start word is not given in arguement then picking any random word from the sample text ( which is dictionary available in dictionary)
            CurrWord = random.choice(list(self.prefix_dict))
            Text = Text + CurrWord[0] + " " + CurrWord[1]
        else:
            temp_list = []                                                         #temporary list to pick all the tuples in keys of dictionaru where the first part of tuple is the given sample word 
            for i in self.prefix_dict.keys():                                      
                    temp_list.append(i)

            CurrWord = random.choice(temp_list)                                      #picking one random tuple from the temporary list 
            Text = Text + startword + " " + CurrWord[1]

        for i in range(numWord - 2):
            NextWord = random.choice(self.prefix_dict[CurrWord])                      #chosing one random word from the list assigned to curr tuple *which consist last two word in the generated text
            Text = Text + ' ' + str(NextWord)
            CurrWord = (CurrWord[1] ,NextWord)
        print(Text)


#main code   

t = TextGenerator()
t.assimilateText('sherlock.txt')
t.generateText(100  , "palakkad")