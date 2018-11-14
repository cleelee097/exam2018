def get_value(name):
    letter_dict = {'a': 1, 'b':2, 'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
    'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,
    'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26
    }

    namevalue = sum([ord(letter.lower())-96 for char in letter_dict])
      
    return namevalue

def get_name_list(filename):
    fp = open(filename).read()splitlines()
    first_name_list = [fp(' ')[0] for full_name in fp]
    name_list = [name.lower() for name in first_name_list]
    return name_list

def who_has_the_highest_value(name_list):
    i = 0
    highest_name = name_list[0]
    highest_name_value = get_value(name_list[0])
    name = name_list[i]
    for name in name_list:
    name_value = get_value(name)
        if name_value > highest_name_value:
            highest_name_value = name_value
            highest_name = name
        i += 1
    print(highest_name, highest_name_value)

def include_positive_words():
    file=open("./positive-words.txt")


def main():


if __name__ == '__main__':
    main()