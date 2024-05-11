#! python3
# Ch9Prob2.py reads a text file containing a madlibs game and allows
# the user to input their own words for any ADJECIVE, NOUN, ADVERB, or VERB prompt.
# the program will then write the new text with the users answers to a txt file

import re
import pyinputplus as pyip

#TODO open text file and identify the prompts for user input by iterating
# through the string

madlibs = open('C:\PythonCode\madlibs.txt')
madlibs_content = madlibs.read()
part_of_speech_regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
replacements = part_of_speech_regex.findall(madlibs_content)
final = madlibs_content
madlibs.close()

for i in replacements:
    art = 'a'
    if i == 'ADJECTIVE':
        art = 'an'
    user_input = pyip.inputStr(f'Enter {art} {i}:\n')
    final = re.sub(i, user_input, final, count=1)

madlibs_result = open('C:\pythoncode\madlibs_result.txt', 'w')
madlibs_result.write(final)
madlibs_result.close()
print(final)







#TODO print prompt for user to enter input depending on the part of speech
# required and insert user input into string

#TODO create new file with completed string and print to screen




