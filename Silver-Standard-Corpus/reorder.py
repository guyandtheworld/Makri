from random import shuffle

def mix_files():
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

def test_train_split():

    with open("silverCorp") as f:
        fresh = f.read()

    lines = fresh.split("\n")

    train = ""

    test = ""

    list_length = len(lines)
    cut = int(list_length * .8)
    
    train_list = lines[0:cut]

    test_list = lines[cut:list_length]

    for line in train_list:
        train = train + "\n" + line

    for line in test_list:
        test = test + "\n" + line

    with open("silverTrain", "w") as text_file:
        text_file.write(train)

    with open("silverTest", "w") as text_file:
        text_file.write(test)

test_train_split()