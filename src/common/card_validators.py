import re


class CardValidators(object):
    
    @staticmethod
    def validate_card(card_number):
        card = CardValidators.__treat_card_number(card_number)

        if card is False:
            return card

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
            card_number = ''.join(str(e) for e in card)
            return card_number

        return False

    @staticmethod
    def __treat_card_number(card_number):
        card_number = ''.join(re.findall(r'\d', str(card_number)))

        if not card_number or (len(card_number) < 12 or len(card_number) > 16):
            return False

        card = [int(d) for d in card_number]

        return card

    @staticmethod
    def get_card_issuer(card_number):
        card = CardValidators.__treat_card_number(card_number)

        if card is False:
            return card

        if card[0] == 4:
            return 'Visa'
        elif card[0] == 5 and 0 < card[1] <= 5:
            return 'Mastercard'
        else:
            return 'Others'
