from pathlib import Path

def _08(path_string):

    p = Path(path_string)
    return most_recently_modified(p)[0]


# returns filename, time
def most_recently_modified(p):
    # print(p)
    if p.is_dir():
        most_recent_name = None
        most_recent_time = 0
        for child in p.iterdir():
            child_recent_name, child_recent_time = most_recently_modified(child)
            if child_recent_time > most_recent_time:
                most_recent_time = child_recent_time
                most_recent_name = child_recent_name
        return most_recent_name, most_recent_time
    else:
        return p.name, p.stat().st_mtime
    

print(_08("C:\\Users\\georg\\Documents\\Programming\\_2023\\ServitaChallenge"))
