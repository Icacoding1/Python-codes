word_list = []

while True:
    word = input("Enter a word: ")
    words = word.split()

    word_list.extend(words)

    choice = input("Do you want to enter another word or sentence? (Y/N): ")
    if choice.lower() != 'y':
        break

print("Total number of words:", len(word_list))
print("Words you entered:", ", ".join(word_list))