#!/usr/bin/env python3
"""Credit card validation and generation script."""
import sys
import re
import random
import argparse

class CreditCardValidationError(ValueError):
    """Custom exception for credit card validation errors."""

class CreditCard:
    """Class for credit card validation and generation."""

    VALID_IINS = [
        "411111", "422228", "433333", "444449", "455551", "466663", "477775", "488887",
        "499999", "511111", "522228", "533333", "544449", "555551", "341111", "372228",
        "601100", "601101", "601102", "601103"
    ]

    CARD_TYPES = ["visa", "mastercard", "amex"]

    @staticmethod
    def verify_credit_card(card_number):
        """Verifies if a credit card number is in a valid format."""
        card_number = re.sub(r'[\s-]', '', card_number)
        if not card_number.isdigit():
            raise CreditCardValidationError("Error: Credit card number must contain only digits.")

        if not (13 <= len(card_number) <= 19):
            raise CreditCardValidationError("Error: Credit card number must be between 13 and 19 digits.")

        try:
            digits = [int(digit) for digit in card_number]
            odd_digits = digits[-1::-2]
            even_digits = digits[-2::-2]
            checksum = 0
            checksum += sum(odd_digits)
            for digit in even_digits:
                checksum += sum(divmod(digit * 2, 10))
            return checksum % 10 == 0
        except ValueError as exc:
            raise CreditCardValidationError("Error: Invalid credit card number format.") from exc

    @staticmethod
    def generate_credit_card(iin, length):
        """Generates a random credit card number with a given IIN."""
        remaining_length = length - len(iin) - 1  # -1 for the check digit
        digits = [random.randint(0, 9) for _ in range(remaining_length)]
        card_number = iin + "".join(map(str, digits))
        checksum = 0
        for i, digit in enumerate(card_number[::-1]):
            digit = int(digit)
            if i % 2 == 0:
                checksum += digit
            else:
                checksum += sum(divmod(digit * 2, 10))
        check_digit = (10 - (checksum % 10)) % 10
        return card_number + str(check_digit)

    @classmethod
    def generate_valid_credit_card(cls, length):
        """Generates a valid credit card number."""
        iin = random.choice(cls.VALID_IINS)
        return cls.generate_credit_card(iin, length)

    @classmethod
    def generate_card_by_type(cls, card_type):
        """Generates a credit card number by type."""
        if card_type == "visa":
            generated_card = cls.generate_valid_credit_card(16)
            return "-".join([generated_card[i:i + 4] for i in range(0, 16, 4)])
        elif card_type == "mastercard":
            generated_card = cls.generate_valid_credit_card(16)
            return "-".join([generated_card[i:i + 4] for i in range(0, 16, 4)])
        elif card_type == "amex":
            generated_card = cls.generate_valid_credit_card(15)
            return "-".join([generated_card[0:4], generated_card[4:10], generated_card[10:15]])
        else:
            raise CreditCardValidationError(f"Error: Invalid card type '{card_type}'. Supported types are {', '.join(cls.CARD_TYPES)}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Credit card validation and generation script.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-v", "--verify", action="store_true", help="Verify a credit card number.")
    group.add_argument("-g", "--generate", action="store_true", help="Generate a credit card number.")
    parser.add_argument("-n", "--number", help="Credit card number to verify.")
    parser.add_argument("-t", "--type", choices=CreditCard.CARD_TYPES, help="Card type to generate.")

    args = parser.parse_args()

    try:
        if args.verify:
            if args.number:
                if CreditCard.verify_credit_card(args.number):
                    print("Valid credit card number.")
                    sys.exit(0)
                else:
                    print("Invalid credit card number.")
                    sys.exit(1)
            else:
                parser.error("Credit card number is required for verification.")
        elif args.generate:
            try:
                if args.type:
                    generated_card = CreditCard.generate_card_by_type(args.type.lower())
                else:
                    card_type = random.choice(CreditCard.CARD_TYPES)
                    generated_card = CreditCard.generate_card_by_type(card_type)
                print(generated_card)
                sys.exit(0)
            except CreditCardValidationError as e:
                print(e)
                sys.exit(1)

    except SystemExit as e:
        if e.code != 0:
            sys.exit(e.code)
    except Exception as exc:
        print(f"An unexpected error occurred: {exc}")
        sys.exit(1)
