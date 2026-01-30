# def caesar(text, shift):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     shifted_alphabet = alphabet[shift:] + alphabet[:shift]
#     translation_table = str.maketrans(alphabet, shifted_alphabet)
#     text = 'hello world'
#     encrypted_text = text.translate(translation_table)
#     print(encrypted_text)

# caesar('Hello word', 5)


# def caesar(text, shift):
    
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     shifted_alphabet = alphabet[shift:] + alphabet[:shift]
#     translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
#     return text.translate(translation_table)


# encrypted_text = caesar('freeCodeCamp', 3)
# print(encrypted_text)


def caesar(text, shift):
    # Check if shift is an integer
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    
    # Check if shift is out of range (less than 1 or greater than 25)
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)


# Example usage
encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)  # Output: iuhhFrghFdps
