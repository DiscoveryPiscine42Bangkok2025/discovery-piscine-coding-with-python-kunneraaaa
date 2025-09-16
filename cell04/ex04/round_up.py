user_input = input("Give me a number: ")
number = float(user_input)
rounded_down_number = round(number)

if number > rounded_down_number:
    print(rounded_down_number + 1)
else:
    print(int(number))