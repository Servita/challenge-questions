with open("file.txt", "r") as file:
    text = file.read()
    total = 0
    for char in text:
        if char == " ":
            total += 1

    print("The number of the words in this file is: ", total)
