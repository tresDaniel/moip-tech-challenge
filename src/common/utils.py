from random import randint


class Utils(object):

    @staticmethod
    def random_with_n_digits(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return str(randint(range_start, range_end))

    @staticmethod
    def generate_boleto():
        boleto_number = Utils.random_with_n_digits(5) + "." + Utils.random_with_n_digits(5) + " " + Utils.random_with_n_digits(5) + "." + \
               Utils.random_with_n_digits(6) + " " + Utils.random_with_n_digits(5) + "." + Utils.random_with_n_digits(6) + " " + \
               Utils.random_with_n_digits(1) + " " + Utils.random_with_n_digits(15)

        return boleto_number
