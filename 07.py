from pathlib import Path

def _07(path_string):

    p = Path(path_string)
    return size(p)


def size(p):
    print(p)
    if p.is_dir():
        total = 0
        for child in p.iterdir():
            total += size(child)
        return total
    else:
        return p.stat().st_size

print(_07("C:\\Users\\georg\\Documents\\Programming\\_2022\\OpenGL"))