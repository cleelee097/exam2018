def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    file = open(file_name, 'r')
    name_list=[]
    for name in file:
        name_list.append(name.split(','))
    return name_list


def total_births(year):
    """

    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """

    if int(year) > 1879 and int(year) <2011:
         names = process_file('babynames/yob' + str(year) + '.txt')
         totalbirths=0
         for i in names:
             totalbirths +=float(i[2])
         return totalbirths

    else:
        return ValueError
          

def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    names = process_file('babynames/yob'+str(year)+'.txt')
    totalbirth=total_births(year)
    for i in names:
        if name==i[0] and gender==i[1]:
            return (int(i[2])/totalbirth)
        else:
            return 0


def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    high_year=0
    high_proportion=0
    for year in list(range(1880,2012)):
        if proportion(name, gender, year) > high_proportion:
            high_year = year
            high_proportion = proportion(name, gender, year)


def main():
    pass  # delete this line and replace with your code here


if __name__ == '__main__':
    main()
