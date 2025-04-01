## Functional Requirements:

- Credit Card Validation:

   - Implement the Luhn algorithm.

   - Validate card number length (13-19 digits).

   - Validate that input is numeric.

- Credit Card Generation:

   - Generate valid Visa, MasterCard, and American Express numbers.

   - Use valid Issuer Identification Numbers (IINs).

   - Format output with dashes.

   - Randomly choose card type if no type is provided.

- Command-Line Interface:

   - Use argparse for argument parsing.

   - Support -v (verify), -g (generate), -n (number), and -t (type) flags.

   - Mutually exclusive verify and generate commands.

- Error Handling:

   - Create a custom CreditCardValidationError exception.

   - Handle invalid input and generation errors gracefully.

   - Exit with 0 on success, and 1 on error.

## Python Coding Standards:

- Adhere to Pylint conventions.
- Include a shebang line.
- Use a class to encapsulate the credit card functions.
- Robust error handling.

## Data:

- A list of valid IINs from major banks.
- A list of valid card types.

## Implicit Requirements:

- Use the re module for input sanitization.
- Use the random module for number generation.
- Use the sys module for exiting the program.
