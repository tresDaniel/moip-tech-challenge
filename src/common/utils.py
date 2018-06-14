import re
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

    @staticmethod
    def validate_cpf(cpf):
        cpf = ''.join(re.findall(r'\d', str(cpf)))

        if not cpf or len(cpf) < 11:
            return False

        buyer_cpf = [int(d) for d in cpf]

        verified_cpf = buyer_cpf[:9]
        while len(verified_cpf) < 11:
            residue = sum([v * (len(verified_cpf) + 1 - i) for i, v in enumerate(verified_cpf)]) % 11

            verifying_digit = 0 if residue <= 1 else 11 - residue

            verified_cpf.append(verifying_digit)

        if verified_cpf == buyer_cpf:
            return cpf

        return False

    @staticmethod
    def validate_email(email):
        email_re = re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')

        return email if email_re.match(email) else False
