def _10(data, key_name):
    result = []
    taken_keys = []
    for entry in data:
        if entry[key_name] not in taken_keys:
            taken_keys.append(entry[key_name])
            result.append(entry)

    return result


print(_10([
   {
      "id":1,
      "name":"John"
   },
   {
      "id":2,
      "name":"Mary"
   },
   {
      "id":1,
      "name":"Johnny"
   }
], "id"))