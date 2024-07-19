#Python version - 3.8
"""
Ploblem Statement :-

Given the dictionary of words:
albums
barely 
befoul
convex 
hereby 
jigsaw 
tailor 
weaver

And this collection of word “pieces”:
al
bums
bar
ely
be
foul
con
vex
here
by
jig
saw
tail
or
we
aver

Find all six letter words from the dictionary using the collection of pieces. In other words, iterate through the pieces to find the wholes:
al + bums => albums
bar + ely => barely
be + foul => befoul
etc …

Print the attempts used to find the whole:
albar != albums
alely != albums
albe != albums
etc …
"""

def find_six_letter_words(search_list, pieces):
    six_letter_words = []
    for search in search_list:
        for i in pieces:
            for j in pieces:
                if i + j == search:
                    six_letter_words.append(search)
                    print(f"{i} + {j} => {search}")
                else:
                    print(f"{i + j} != {search}")
    
    return six_letter_words

# Given data
search_list = [
    "albums", "barely", "befoul", "convex", 
    "hereby", "jigsaw", "tailor", "weaver"
]

pieces = [
    "al", "bums", "bar", "ely", "be", "foul", 
    "con", "vex", "here", "by", "jig", "saw", 
    "tail", "or", "we", "aver"
]

# Find all six-letter words using the pieces
six_letter_words = find_six_letter_words(search_list, pieces)

# Print the result
print("\nFound six-letter words:")
print(six_letter_words)