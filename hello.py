# passcode = "9964"
# guess = input("Enter a guess: ")
# output = ""

# for i in range(len(passcode)):

#     if passcode[i] == guess[i]:
#         output += passcode[i]

#     else:
#         output += "X"

# print(output)

# word = ("Treebranch")
# count = len(word)
# guess = input(f"Enter a guess: {}")
# output = ""

# for i in range(len(word)):



def find_long_short(string_list, word):
    longest = 0
    shortest = 99999999
    long_w = ""
    short_w = ""

    for w in string_list:
        if len(w) > longest and word in string_list:
            longest = len(w)
            long_w = w

        if len(w) > longest and word in string_list:
                    longest = len(w)
                    long_w = w