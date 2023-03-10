
#### General
1.  Create a function that accepts an array of integers and returns the sum of all the even numbers in the array.
2. Create a function that accepts two arrays and returns a new array that contains only the elements that are common between the two arrays.
3. Create a function that accepts an array of integers and returns the second smallest number in the array.
4. Write a program that accepts a string and returns true if the string is a palindrome, false otherwise.
5. Write a program that accepts two strings and returns true if they are anagrams of each other, false otherwise.

### File System
1. Write a program that accepts a file path and returns the number of words in the file.
2. Write a program that accepts a directory path and returns the total size of all files in the directory.
3. Write a program that accepts a directory path and returns the name of the file that has been modified most recently.

### Data Transformation

1.  Combine data from two data sources: Combine data from two different sources into a single data set based on a shared key.

#####  Example
#####  Input:

```json
[
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
]
```

##### Output:
```json
[
   {
      "id":1,
      "name":"John",
      "age":30
   },
   {
      "id":2,
      "name":"Mary",
      "age":25
   }
]
```

2.  Remove duplicates from data: Remove duplicates from a data set based on a specified key.

##### Input:
```json
[
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
]
```

##### Output:
```json
[
   {
      "id":1,
      "name":"John"
   },
   {
      "id":2,
      "name":"Mary"
   }
]
```

3. Calculate running totals: Calculate running totals for a specified key in a data set.

##### Input
```json
[
  { "date": "2022-01-01", "value": 100 },
  { "date": "2022-01-02", "value": 200 },
  { "date": "2022-01-03", "value": 150 },
  { "date": "2022-01-04", "value": 300 }
]

```
##### Output
```json
[
  { "date": "2022-01-01", "value": 100, "total": 100 },
  { "date": "2022-01-02", "value": 200, "total": 300 },
  { "date": "2022-01-03", "value": 150, "total": 450 },
  { "date": "2022-01-04", "value": 300, "total": 750 }
]
```

4. 3Convert data to hierarchical format: Transform a flat data set into a hierarchical format.

##### Input
```json
[
  { "name": "John", "parent": null },
  { "name": "Mary", "parent": "John" },
  { "name": "Bob", "parent": "John" },
  { "name": "Alice", "parent": "Mary" }
]
```
##### Output
```json
[
  {
    "name": "John",
    "children": [
      { "name": "Mary", "children": [{ "name": "Alice", "children": [] }] },
      { "name": "Bob", "children": [] }
    ]
  }
]
```
