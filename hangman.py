word = "apple"
letters = list(word)

blank_letters = []
for letter in letters:
    blank_letters.append("_")


print(f"Your word is: {''.join(blank_letters)}")
entered_letter = input("Enter letter: ")

for letter in letters:
    if letter == entered_letter:
        print("True")
    else:
        print("False")