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

            check_digit = 0 if residue <= 1 else 11 - residue

            verified_cpf.append(check_digit)

        if verified_cpf == buyer_cpf:
            return cpf

        return False

    @staticmethod
    def validate_email(email):
        email_re = re.compile('^[\w.-]+@([\w-]+\.)+[\w]+$')

        return email if email_re.match(email) else False

    @staticmethod
    def validate_card(card_number):
        card = Utils.treat_card_number(card_number)

        odd_card = card[:len(card) - 1]
        even_numbers = card[1::2]
        odd_numbers = odd_card[-1::-2]
        sum = 0

        for i in range(len(odd_numbers)):
            odd_number = odd_numbers[i] * 2

            if odd_number > 9:
                str_odd_number = str(odd_number)
                odd_number = int(str_odd_number[0]) + int(str_odd_number[1])
                sum += odd_number
            else:
                sum += odd_number

        for i in range(len(even_numbers)):
            sum += even_numbers[i]

        if sum % 10 == 0:
            return card_number
        else:
            return False

    @staticmethod
    def get_card_issuer(card_number):
        card = Utils.treat_card_number(card_number)

        if card[0] == 4:
            return 'Visa'
        elif card[0] == 5 and 0 < card[1] <= 5:
            return 'Mastercard'
        else:
            return 'Others'

    @staticmethod
    def treat_card_number(card_number):
        card_number = ''.join(re.findall(r'\d', str(card_number)))

        if not card_number or (len(card_number) < 12 or len(card_number) > 16):
            return False

        card = [int(d) for d in card_number]

        return card
