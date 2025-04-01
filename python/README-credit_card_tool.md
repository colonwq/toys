# Credit Card Validation and Generation Script

This script allows you to validate credit card numbers and generate valid credit card numbers.

## Features

* **Credit Card Validation:** Verifies if a credit card number is in a valid format using the Luhn algorithm.
* **Credit Card Generation:** Generates valid credit card numbers for Visa, MasterCard, and American Express.
* **Command-Line Interface:** Easy to use with command-line arguments.
* **Error Handling:** Provides informative error messages for invalid input.
* **IIN Support:** Uses valid Issuer Identification Numbers (IINs) from major banks for generation.

## Usage

### Prerequisites

* Python 3.6 or later

### Installation

1.  Save the Python script (e.g., `credit_card_tool.py`).
2.  Make the script executable (if necessary):

    ```bash
    chmod +x credit_card_tool.py
    ```

### Running the Script

#### Validation

To validate a credit card number, use the `-v` or `--verify` flag along with the `-n` or `--number` flag:

```bash
python credit_card_tool.py -v -n 4111111234567890
```
or

```bash

./credit_card_tool.py -v -n 4111111234567890
```

If the credit card number is valid, the script will output:

```Valid credit card number.```

If the credit card number is invalid, the script will output:

```Invalid credit card number.```

### Generation
To generate a credit card number, use the -g or --generate flag. You can optionally specify the card type using the -t or --type flag (visa, mastercard, amex):

```bash
python credit_card_tool.py -g -t visa
```

or

```bash
./credit_card_tool.py -g -t mastercard
```

If no card type is specified, a random card type will be used:

```Bash
python credit_card_tool.py -g
```

The script will output the generated credit card number with dashes:

```4111-1112-3456-7890```

or

```3411-111234-56789```

### Examples
#### Valid Examples

```bash
python credit_card_tool.py -v -n 4111111234567890 #(Visa)
python credit_card_tool.py -v -n 5111111234567890 #(MasterCard)
python credit_card_tool.py -v -n 341111123456789 (#American Express)
python credit_card_tool.py -g -t visa
python credit_card_tool.py -g -t mastercard
python credit_card_tool.py -g -t amex
python credit_card_tool.py -g
```

#### Invalid Examples

```bash
python credit_card_tool.py -v -n 1234567890 #(Invalid length)
python credit_card_tool.py -v -n 4111111234567891 #(Invalid Luhn checksum)
python credit_card_tool.py -v -n abcdefghijklmnop #(Non-numeric input)
python credit_card_tool.py -g -t invalid_type #(Invalid card type)
python credit_card_tool.py -v #(Missing credit card number)
```

#### Error Handling

The script will raise a CreditCardValidationError for invalid input or generation failures. It will also catch general exceptions to prevent crashes.
