#Write a program to reverse a given string.
#Type-1: Using slicing
def reverse_string(s):
    return s[::-1]

input_str = input("Enter a string: ")
print("Reversed string:", reverse_string(input_str))

# Type-2: In-place reversal
def reverse_string_in_place(s):
    s = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

print("Reversed string (in-place):", reverse_string_in_place(input_str))

#Type-3: Using recursion
def reverse_string_recursion(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_string_recursion(s[:-1])

print("Reversed string (recursion):", reverse_string_recursion(input_str))

#Type-4: Using a stack
def reverse_string_stack(s):
    stack = list(s)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str

print("Reversed string (stack):", reverse_string_stack(input_str))