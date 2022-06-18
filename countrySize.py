'''Potential To-Dos

--------------
- (((CURRENTLY IMPOSSIBLE TODO: ideally the 2nd choice would not include 
the country/entity of the first choice (currently when you choose the 
same country/entity twice, the program will just exit)
o I tried it by using blacklistRegex but it did not work because it did 
complain that "blacklistRegexes" is not defined: "result = 
pyip.inputStr('Favorite animal> ', blacklistRegexes=['moose'])"_30.4.22
o I also tried to create a list and let pyip make use of the list, 
which die not work either because it did not recognize the 
list_30.4.22)))
----------

'''

import pyinputplus as pyip

'''These are 15 countries and entities with their size in square 
kilometers. A Dictionary is used to transform user-inputs into the area 
of the countries or entities'''

size_dict = {"China": 9596961,
             "Egypt": 1002450,
             "Germany": 357114,
             "Japan": 377976,
             "Russia": 17098246,
             "USA": 9525067,
             "Vatican City": 0.49,
             "earth surface": 510072000,
             "earth land surface": 148940000,
             "earth water surface": 361132000,
             "moon surface": 37300000,
             "jupiter surface": 61469000000,
             "European Union": 4233262,
             "Greenland": 2166086,
             "sun surface": 6090000000000}

print(
    '''Did you ever wonder how often Germany fits into another country or even the surface of the moon?

This program enables you to compare the sizes of 15 countries and other entities! ''')


'''
TODO:
-Starting from here a while True loop can start.
- at the end of the while loop the user is asked "Do you want to make another
comparison? If yes choose "yes" if no choose "quit" (use pyInputPlus for this)
- as soon as "round > 1" (so before "round = 1" must be implemented)...


'''

print('''
Choose the 2 countries (or other entities) you want to compare.
Let's start with the first one.''')


'''
(((CURRENTLY IMPOSSIBLE TODO: Add a prompt like ">>>" to make sure the 
user sees where he/she needs to type. It does however unfortunately not 
work, because no matter where I put it, either it does not work, or the
">>> " is put only in in front of China. _30.4.22)))
'''
# The user choses the first country or entity to be compared.
choice_1_input = pyip.inputMenu(['China', 'Egypt', 'Germany', 'Japan',
                                 'Russia', 'USA', 'Vatican City',
                                 'earth surface', 'earth land surface',
                                 'earth water surface', 'moon surface',
                                 'jupiter surface', 'European Union',
                                 'Greenland', 'sun surface'], lettered=True,
                                numbered=False)  # input as a string

# Let user know what he/she chose
print("You have chosen", choice_1_input, ".")


# size of the first area
choice_1_area = size_dict[choice_1_input]

print("Now type in the country (or other entity) you want to compare the size with")

# The user choses country or entity the first country or entity should be
# compared with.
choice_2_input = pyip.inputMenu(['China', 'Egypt', 'Germany', 'Japan',
                                 'Russia', 'USA', 'Vatican City',
                                 'earth surface', 'earth land surface',
                                 'earth water surface', 'moon surface',
                                 'jupiter surface', 'European Union',
                                 'Greenland', 'sun surface'], lettered=True,
                                numbered=False)  # input as a string
# size of the second area
choice_2_area = size_dict[choice_2_input]


# Determining different variables for the following print statement to
# show the user the results
if choice_1_area > choice_2_area:
    bigger_entity = choice_1_input
    smaller_entity = choice_2_input

if choice_2_area > choice_1_area:
    bigger_entity = choice_2_input
    smaller_entity = choice_1_input

bigger_area = size_dict[bigger_entity]
smaller_area = size_dict[smaller_entity]

comparison_factor = size_dict[bigger_entity] / size_dict[smaller_entity]

# making sure that the grammar is correct in the following print statement
# to show the user the results
grammar_dict = {"China": 'China',
                "Egypt": 'Egypt',
                "Germany": 'Germany',
                "Japan": 'Japan',
                "Russia": 'Russia',
                "USA": 'USA',
                "Vatican City": 'Vatican City',
                "earth surface": 'the earth\'s surface',
                "earth land surface": 'the earth\'s land surface',
                "earth water surface": 'the earth\'s water surface',
                "moon surface": 'the moon\'s surface',
                "jupiter surface": 'Jupiter\'s surface',
                "European Union": 'the Euopean Union',
                "Greenland": 'Greenland',
                "sun surface": 'the sun\'s surface'}

# size_dict[choice_1_input]

# This gives the user the information he/she asked for.
print(
    "---RESULT:",
    grammar_dict[bigger_entity],
    "is",
    round(
        comparison_factor,
        2),
    "times bigger than",
    grammar_dict[smaller_entity],
    ", nameley",
    grammar_dict[bigger_entity],
    "is",
    f"{bigger_area:,}",
    "km² and",
    grammar_dict[smaller_entity],
    "is",
    f"{smaller_area:,}",
    "km² big.---")


'''
(((CURRENTLY IMPOSSIBLE-TODO: ideally the comparison factor would also 
have a "," in e.g. "1,000" instead of "1000"))) however it did not work 
out (see "v82_NOPE_TRYINGcomparisonFactorWithAcommaAfter3Digits_
UNFORTUNATELYnowThereAreNotOnly2DigitsAfterComma_2"
and the ca. 4 versions before. The problem was that either only the "," 
aspect works or only the 2 digits after comma aspect, even though I 
tried different options with the format etc._30.4.22
'''

'''TODO: adjust it into a while loop and make it possible to ask another 
question again and again. One option might be to ask the user at the end 
if he she/ wants to ask another question or quit the program. I did 
something similar in my loveletter-game so I can probably adjust the way
I did it there'''
