
def load_first_website():
    """ In this function we are able to read the
     first link
    """
    with open('web_links.csv') as file:
        f_link = [line.strip() for line in file]

        return f_link[0]


def load_second_website():
    """ In this function we are able to read the
    second link
    """
    with open('web_links.csv') as file:
        s_link = [line.strip() for line in file]

        return s_link[1]

#print(load_second_website())


def load_third_website():
    """ In this function we are able to read the
    third link
    """
    with open('web_links.csv') as file:
        t_link = [line.strip() for line in file]
        return t_link[2]


def load_fourth_website():
    with open('web_links.csv') as file:
        fo_link = [line.strip() for line in file]
        return fo_link[3]

