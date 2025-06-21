import random
total_choice = ['yes','no']
length_of_password = int(input("Enter the length of password:"))
small_char_choice = input("Enter 'yes' for using small character and 'no' for not using:").lower()
capital_char_choice = input("Enter 'yes'for using capital character and 'no' for not using:").lower()
number_char_choice = input("Enter 'yes'for using number character and 'no' for not using:").lower()
symbol_char_choice = input("Enter 'yes'for using symbol character and 'no' for not using:").lower()
if small_char_choice == 'no' and capital_char_choice == 'no' and number_char_choice == 'no' and symbol_char_choice == 'no':
    print("Please select atleast one of the above")
    exit()
if small_char_choice not in total_choice or capital_char_choice not in total_choice or number_char_choice not in total_choice or symbol_char_choice not in total_choice:
    print("Entered option is not available please check again")
    exit()
def small_char_generate():
    g = random.randint(97,122)
    return (chr(g))

def capital_char_generate():
    g = random.randint(65,90)
    return (chr(g))

def number_char_generate():
    g = random.randint(48,57)
    return (chr(g))

def symbol_char_generate():
    g = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    return random.choice(g)


def password_generator(num):
    list1 = []
    while len(list1) < num:
        x = random.randint(1,4)
        if x == 1:
            if small_char_choice == 'yes':
                new_char = small_char_generate()
                list1.append(new_char)
            else:
                pass
        elif x == 2:
            if capital_char_choice == 'yes':
                new_char = capital_char_generate()
                list1.append(new_char)
            else:
                pass
        elif x == 3:
            if number_char_choice == 'yes':
                new_char = number_char_generate()
                list1.append(new_char)
            else:
                pass
        else:
            if symbol_char_choice == 'yes':
                new_char = symbol_char_generate()
                list1.append(new_char)
            else:
                pass
    print("".join(list1))
   
password_generator(length_of_password)