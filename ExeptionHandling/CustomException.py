class InvalidAgeException(Exception):
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

number = 18

try:
    input_number = int(input("Enter a number: "))

    if input_number < number:
        raise InvalidAgeException("You are not eligible to vote", 101)
    else: 
        print("You are eligible to vote")
except InvalidAgeException as e:
    print(f"Error: {e}, Error Code: {e.error_code}")