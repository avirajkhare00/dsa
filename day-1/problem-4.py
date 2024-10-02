# Check if a string is a palindrome, ignoring non-alphanumeric characters.

def is_palindrome(given_str):
  return given_str == ''.join(reversed(list(given_str)))

print(is_palindrome('naman'))
print(is_palindrome('aman'))
print(is_palindrome('madam'))
