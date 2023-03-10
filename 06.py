def _06(path):
    word_count = 0
    with open(path, "r") as f:
        for line in f:
            word_count += len(line.split(" "))

    return word_count


print(_06("C:\\Users\\georg\\Documents\\york accomodation.txt"))