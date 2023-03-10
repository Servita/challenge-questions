from turtle import st


def is_palindrome_01(inp_string: str) -> bool:
    return inp_string == "".join(reversed(inp_string))

def is_palindrome_02(inp_string: str) -> bool:
    stack = []
    middle_index = len(inp_string) // 2
    for i, character in enumerate(inp_string):
        if i < middle_index:
            stack.append(character)
        elif i != middle_index or len(inp_string) % 2 == 0:
            if (n:=stack.pop()) != character:
                return False
    return True
            
            
#0123456
print(is_palindrome_01("abccba"))
print(is_palindrome_01("abcdcba"))
print(is_palindrome_01("abcdcbad"))

print("-------")

print(is_palindrome_02("abccba"))
print(is_palindrome_02("abcdcba"))
print(is_palindrome_02("abcdcbad"))