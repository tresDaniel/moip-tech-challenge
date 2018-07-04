import re
from random import randint
from src.common.card_validators import CardValidators

class Utils(object):

    @staticmethod
    def generate_boleto():
        boleto_number = Utils.__random_with_n_digits(5) + "." + Utils.__random_with_n_digits(5) + " " + Utils.__random_with_n_digits(5) + "." + \
                   Utils.__random_with_n_digits(6) + " " + Utils.__random_with_n_digits(5) + "." + Utils.__random_with_n_digits(6) + " " + \
                   Utils.__random_with_n_digits(1) + " " + Utils.__random_with_n_digits(15)

        return boleto_number

    @staticmethod
    def __random_with_n_digits(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return str(randint(range_start, range_end))

    @staticmethod
    def validate_cpf(cpf):
        cpf = ''.join(re.findall(r'\d', str(cpf)))

        if not cpf or len(cpf) != 11:
            return False

        buyer_cpf = [int(d) for d in cpf]

        verified_cpf = buyer_cpf[:9]

        while len(verified_cpf) < 11:
            verified_cpf = Utils.__append_cpf_residue(verified_cpf)

        if verified_cpf == buyer_cpf:
            return cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]
        else:
            cpf = False
            return cpf

    @staticmethod
    def __append_cpf_residue(verified_cpf):
        residue = Utils.__get_cpf_residue(verified_cpf)
        check_digit = 0 if residue <= 1 else 11 - residue
        verified_cpf.append(check_digit)
        return verified_cpf

    @staticmethod
    def __get_cpf_residue(verified_cpf):
        return sum([v * (len(verified_cpf) + 1 - i) for i, v in enumerate(verified_cpf)]) % 11

    @staticmethod
    def validate_email(email):
        email_re = re.compile('^[\w.-]+@([\w-]+\.)+[\w]+$')

        return email if email_re.match(email) else False



