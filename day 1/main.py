
class Phonenum:
    
    def __init__(self, number, is_spam) -> None:

        self.number = number

        self.is_spam = is_spam



    def answer_call(self):

        print(f"answered call from {self.number}")

    def reject_call(self):

        print(f"rejected call from {self.number}")



with open("input.txt", "r") as reader:

    for x in reader:

        x = x.strip()

        print(x)



        number = Phonenum(x, None)

        reverse_number = list(x)

        reverse_number.reverse()

        if reverse_number[0] in '89' and reverse_number[1] == reverse_number[2] and reverse_number[3] in '89':

            number.is_spam = True

            number.reject_call()

        
        else:

            number.is_spam = False

            number.answer_call()
