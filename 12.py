# not finished

def _12(data):
    result = []
    # find root
    for entry in data:
        if entry["parent"] == None:
            root = entry
            result.append(root)

        