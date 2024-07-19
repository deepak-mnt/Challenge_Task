#Python version - 3.8
"""
Ploblem Statement :-

In this problem, you will be given one or more integers in English. Your task is to translate these numbers into their integer representation. The numbers can range from negative 999,999,999 to positive 999,999,999. The following is an exhaustive list of English words that your program must account for:

negative, zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, hundred, thousand, million


INPUT AND OUTPUT


Notes on input:

Negative numbers will be preceded by the word negative.
The word “hundred” is not used when “thousand” could be. For example, 1500 is written “one thousand five hundred”, not “fifteen hundred”.


SAMPLE INPUT

six, negative seven hundred twenty nine, one million one hundred one
 

SAMPLE OUTPUT

6, -729, 1000101
"""

def convert_to_number(words):
    # Dictionaries for mapping words to numbers
    basic_numbers = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
        'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
        'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
        'eighty': 80, 'ninety': 90
    }
    
    other_numbers = {
        'hundred': 100, 'thousand': 1000, 'million': 1000000
    }
    
    # Initialize variables
    result = 0
    temp_result = 0
    is_negative = False
    multiplier = 1
    
    # Handle negative number
    if words[0] == 'negative':
        is_negative = True
        words = words[1:]
    
    # Process each word in the list
    for word in words:
        if word == 'negative':
            continue
        elif word in basic_numbers:
            temp_result += basic_numbers[word]
        elif word in other_numbers:
            if word == 'hundred':
                temp_result *= other_numbers[word]
            else:
                multiplier *= other_numbers[word]
                result += temp_result * multiplier
                temp_result = 0
        else:
            raise ValueError(f"Invalid word: {word}")
    
    result += temp_result
    
    if is_negative:
        result = -result
    
    return result

def convert_to_integer(english_number):
    # Split input by commas and trim whitespace
    number_word_list = english_number.split(',')
    numbers_list = []
    
    for number_word in number_word_list:
        words_list = number_word.strip().split()
        number = convert_to_number(words_list)
        numbers_list.append(str(number))
    
    return ', '.join(numbers_list)

# Example usage:
english_number = "six, negative seven hundred twenty nine, one million one hundred one"
integer_representation = convert_to_integer(english_number)
print(integer_representation)
