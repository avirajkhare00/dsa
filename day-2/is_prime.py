import math

def is_odd(num):
  return num % 2 != 0

def is_prime(num):
  if is_odd(num):
    max_divisor = int(math.sqrt(num)) + 1
    for i in range(3, max_divisor, 2):
      if num % i == 0:
        return False
    return True
  else:
    return False


print(is_prime(64))
print(is_prime(63))
print(is_prime(8))
print(is_prime(7))
print(is_prime(13))
print(is_prime(79))
