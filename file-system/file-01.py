def count_words(path: str) -> int:
    lines = []
    with open(path, "r") as f:
        lines.extend([x.strip().split(" ") for x in f.readlines()])
    
    return sum(len(line) for line in lines)

print(count_words("challenge-questions/file-system/words-file.txt"))