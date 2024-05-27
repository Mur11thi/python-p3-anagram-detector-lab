# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word =word
        

    def match(self,word,ana_list=[]):
        matches = []
        sorted_word = sorted(self.word)
        for character in  ana_list :
            characters = sorted([char for char in word])
            # sorted_candidate =sorted(candidate)
        #    sorted_characters = sorted(characters)
        #    if sorted_characters == characters and word != self.word:
            if characters == sorted_word and character != self.word:
               matches.append(word)

        return matches    
            

listen =Anagram("listen")
# anagram.match(['enlists', 'google', 'inlets', 'banana'])    
# listen.match(["listen", "silent", "hippopotamus"])
print(listen.match(["listen", "silent", "hippopotamus"]))  





# class Anagram:
#     def __init__(self, word):
#         self.word = word

#     def match(self, ana_list=[]):
#         matches = []
#         sorted_word = sorted(self.word)
        
#         for candidate in ana_list:
#             sorted_candidate = sorted(candidate)
#             if sorted_candidate == sorted_word and candidate != self.word:
#                 matches.append(candidate)

#         return matches

# listen = Anagram("listen")
# print(listen.match(["listen", "silent", "hippopotamus"]))