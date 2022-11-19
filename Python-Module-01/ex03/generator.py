import random

def shuffle(liste_to_shuffle):
    """suffle the liste"""
    return_liste = []
    while len(liste_to_shuffle) != 0:
        randomNumber = random.randint(0, len(liste_to_shuffle) - 1)
        return_liste.append(liste_to_shuffle[randomNumber])
        del liste_to_shuffle[randomNumber]
    return return_liste

def unique(liste):
    """returns a list where each word appears only once """
    return_list = []
    for word in liste:
        if word not in return_list:
            return_list.append(word)
    return return_list

def generator(text, sep=" ", option=None):
    '''Splits the text according to sep value and yield the substrings.
        option precise if a action is performed to the substrings before it is yielded.
    '''
    if type(text) != str or type(sep) != str:
        print("ERROR")
        return None
    else:
        word_list = text.split(sep)
        if option == "shuffle":
            word_list = shuffle(word_list)
        elif option == "ordered":
            word_list = sorted(word_list)
        elif option == "unique":
            word_list = unique(word_list)
        elif option != None:
            print("ERROR")
            return None
        for w in word_list:
            yield w