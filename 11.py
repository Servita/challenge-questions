def _11(data, key_name):
    total = 0
    result = []
    for entry in data:
        total += entry[key_name]
        result.append({**entry, "total": total})

    return result


print(_11([
  { "date": "2022-01-01", "value": 100 },
  { "date": "2022-01-02", "value": 200 },
  { "date": "2022-01-03", "value": 150 },
  { "date": "2022-01-04", "value": 300 }
], "value"))