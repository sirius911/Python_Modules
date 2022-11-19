class Evaluator:
    """Class to practice statics functions"""
    def __init__(self) -> None:
        pass

    @staticmethod
    def zip_evaluate(words, coefs):
        """ compute the sum of lengths of every words of the list 'words'\
            weighted by a list of coefficinents (coefs).
            using zip()
        """
        ret = -1
        if len(words) == len(coefs):
            ret = 0.0
            try:
                for word, coef in zip(words, coefs):
                    ret += len(word) * coef
            except:
                ret = -1
        print(ret)

    @staticmethod
    def enumerate_evaluate(words, coefs):
        """ compute the sum of lengths of every words of the list 'words'\
            weighted by a list of coefficinents (coefs).
            using enumerate()
        """
        ret = -1
        if len(words) == len(coefs):
            ret = 0.0
            try:
                for index, word in enumerate(words):
                    ret += len(word) * coefs[index]
            except:
                ret = -1
        print(ret)
