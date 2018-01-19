from random import shuffle

files = ['Agriculture', 'Auto', 'Books', 'Careers', 'Education-Malayalam',
         'Features', 'Food', 'Health', 'Money', 'Movies & Music', 'MyHome',
         'News', 'Social', 'Sponsored Content', 'Sports', 'Technology', 'Travel', 'Women', 'Youth']

mixed = ""

for file in files:
    with open(file) as f:
        fresh = f.read()
        mixed = mixed + fresh

tagged_list = mixed.split("\n")

shuffle(tagged_list)

final_string = ""

for count, word in enumerate(tagged_list):
    if count%12 == 0:
        final_string = final_string + " " + word + "\n"
        print count
    elif count%13 == 0:
        final_string = final_string + word
    else:
        final_string = final_string + " " + word

with open("Output", "w") as text_file:
    text_file.write(final_string)

print len(final_string.split("\n"))