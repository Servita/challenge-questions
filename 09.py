def _09(data, key_name):
    result = {}

    for source in data:
        for entry in source:
            entry_key = entry[key_name]
            if entry_key not in result:
                result[entry_key] = {}
            for k, v in entry.items():
                result[entry_key][k] = v
    
    return list(result.values())


print(_09([
   [
      {
         "id":1,
         "name":"John"
      },
      {
         "id":2,
         "name":"Mary"
      }
   ],
   [
      {
         "id":1,
         "age":30
      },
      {
         "id":2,
         "age":25
      }
   ]
], "id"))

        