def join(givenData):
    source1 = givenData[0]
    source2 = givenData[1]
    print(source1)

data1 = [
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

print(join(data1))