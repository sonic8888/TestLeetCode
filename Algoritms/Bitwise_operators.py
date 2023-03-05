# a = 8
# b = 1
# c = 7
# d = 9
# i = 6

# AND (&) (и)
# нахождение четных чисел
# a & b  # => False (0)
# c & b  # => True (1)
# нахождение степени '2'
# a & c  => (0) c = a - 1
# еще применение
# a & b  => при b от 0 -> 7  = 0, от 8 -> 15 = 8 и так дальше цикличность.

# OR (|) (или)
# a | b  # => a т.к b = 1

# XOR ^ (!или) применение => https://habr.com/ru/company/vdsina/blog/538298/
# XOR с одинаковыми аргументами: x ^ x = 0
# XOR и 0: x ^ 0 = x
# Коммутативность: x ^ y = y ^ x
#   a ^ b ^ c ^ a ^ b     # Commutativity
# = a ^ a ^ b ^ b ^ c     # Using x ^ x = 0
# = 0 ^ 0 ^ c             # Using x ^ 0 = x (and commutativity)
# = c

# Обмен значениями
# x ^= y
# y ^= x
# x ^= y
