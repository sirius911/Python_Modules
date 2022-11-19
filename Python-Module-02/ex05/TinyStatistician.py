import functools
import math


def noneValue(func):
    """ return None if Args is empty
    otherwise the result of function"""

    @functools.wraps(func)
    def function(*args, **kwargs):
        if not args or len(args[1]) == 0:
            return None
        else:
            return func(*args, **kwargs)
    return function


class TinyStatistician:
    """ Initiation to vey basic statistic operation"""

    def __init__(self):
        """ initialisation"""
        pass

    @noneValue
    def mean(self, array):
        """Computes the mean of a given non-empty list or array
            return the mean as a float or None if x is empty
        """
        sum = 0
        for x in array:
            sum += x
        mean = float(sum / len(array))
        return mean

    def median(self, array):
        """ computes the median of a given non-empty list or array
            return the median as a float
            or None if the list or array is empty
        """
        array_sorted = sorted(array)
        n = len(array_sorted)
        if n % 2 == 0:
            rang1 = int(n/2)
            rang2 = int((n / 2) + 1)
            valeur1 = array_sorted[rang1 - 1]
            valeur2 = array_sorted[rang2 - 1]
            valeur = (valeur1 + valeur2) / 2
        else:
            rang = int((n + 1) / 2)
            valeur = array_sorted[rang - 1]
        return float(valeur)

    def quartiles(self, array):
        """computes the 1st and 3th quartiles of a given
        non-empty list or array
        return tuple of float or None if list or array empty
        """
        result = [0.0, 0.0]
        array_sorted = sorted(array)
        n = len(array_sorted)
        rang_q1 = ((n + 3) / 4)
        if int(rang_q1) == rang_q1:
            result[0] = float(array_sorted[int(rang_q1 - 1)])
        else:
            coef = rang_q1 - int(rang_q1)
            r_inf = array_sorted[int(rang_q1 - 1)]
            r_sup = array_sorted[int(rang_q1)]
            if coef == 0.25:
                result[0] = ((r_inf * 3) + r_sup) / 4
            elif coef == 0.75:
                result[0] = (r_inf + (r_sup * 3)) / 4
            else:
                result[0] = (r_inf + r_sup) / 2
        rang_q3 = ((3 * n) + 1) / 4
        if int(rang_q3) == rang_q3:
            result[1] = float(array_sorted[int(rang_q3 - 1)])
        else:
            coef = rang_q3 - int(rang_q3)
            r_inf = array_sorted[int(rang_q3 - 1)]
            r_sup = array_sorted[int(rang_q3)]
            if coef == 0.25:
                result[1] = ((r_inf * 3) + r_sup) / 4
            elif coef == 0.75:
                result[1] = (r_inf + (r_sup * 3)) / 4
            else:
                result[1] = (r_inf + r_sup) / 4
        return result

    def var(self, array):
        """computes the variance of a given non-empty list or array"""
        mu = self.mean(array)
        m = len(array)
        sum = 0
        for x in array:
            sum += (x - mu) * (x - mu)
        return (sum / m)

    def std(self, array):
        """ computes the standard deviation of a given non-empty list pr array"""
        return math.sqrt(self.var(array))
