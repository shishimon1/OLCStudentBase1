import random
# Game variables
tries = 0
guess = ''
code = ''

while i in range(4):
    temp = random.randint(1,8)
    code += temp

while tries <= 10:
    tries += 1
    guess = input(f"Try #{tries}, enter code: ")
    feedback = ''
    guess_pos = (False,False,False,False)
    code_pos = (False,False,False,False)
    if guess == code:
        print(f"Congratulations! You broke the code on try #(tries)")

    for i in guess:
        if code[i] == guess[i]:
            feedback += "R"
            guess_pos[i] = True 
            code_pos[i] = True 

    for i in range(4):
        if not guess_pos:
            for x in range[4]:
                if not code_pos and code[x] == guess[i]:
                    feedback += "W"
                    code_pos[x] = True
print(f"Feedback: {feedback}")

if tries == 10:
    print(f"The code is {guess}. Better luck next time!")