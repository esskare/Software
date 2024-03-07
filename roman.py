#convert roman numbers to integers
import pytest
def rom_to_int(roman):
    rom_num = {
        'I': 1, 
        'V': 5,  
        'X': 10, 
        'L': 50,
        'C': 100, 
        'D': 500, 
        'M': 1000
        }
    
    result = 0
    prev_value = 0
    
    for numeral in reversed(roman):
        current_value = rom_num[numeral]
        
        if current_value < prev_value:
            result -= current_value
        else:
            result += current_value
        
        prev_value = current_value
    
    return result


def main():
    while True:
        input = input("Enter a Roman numeral: ").lower()
        
        try:
            result = rom_to_int(input)
            print(f"The integer equivalent of {input} is: {result}")
            break 
        
        except KeyError:
            raise ValueError("Invalid Roman numeral input. Please provide a valid Roman numeral. Try again.")


#testcases
#Single letters
def test_single_letters():
    assert rom_to_int("II") == 2
    assert rom_to_int("V") == 5
    assert rom_to_int("XI") == 11

#Many letters
def test_many_letters():
    assert rom_to_int("III") == 3
    assert rom_to_int("V") == 5
    assert rom_to_int("LXXVIII") == 78

#Subtractive notation(SN)
def test_subtractive_notation():
    assert rom_to_int("IV") == 4

#With and without SN
def test_specific_numeral_XIV():
    assert rom_to_int("XIV") == 14

#Repetition
def test_repeated_letters():
    assert rom_to_int("II") == 2

#Invalid letters
def test_invalid_letters():
    with pytest.raises(ValueError):
        rom_to_int("III")
    with pytest.raises(ValueError):
        rom_to_int("VV")
    with pytest.raises(ValueError):
        rom_to_int("LL")

#First number is I
def test_start_with_I():
    assert rom_to_int("I") == 1
    assert rom_to_int("II") == 2
    assert rom_to_int("III") == 3

#Invalid and valid letter
def test_invalid_and_valid_letters():
    with pytest.raises(ValueError):
       rom_to_int("XB")  

    assert rom_to_int("XII") == 12  

#Null input
def test_null_input():
    assert rom_to_int("") == 0

if __name__ == "__main__":
    test_single_letters()
    test_many_letters()
    test_subtractive_notation()
    test_specific_numeral_XIV()
    test_repeated_letters()
    test_invalid_letters()
    test_start_with_I()  
    test_invalid_and_valid_letters() 
    test_null_input()