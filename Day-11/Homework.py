x = 5  # Binary: 0101
y = 3  # Binary: 0011
result = x & y
result1=x and y
print(result)
print(result1)

AND
OR
XOR
NOT(~)
LEFT SHIFT
RIGHT SHIFT

EXAMPLE:
Bitwise AND (5 & 3)
  0101
& 0011
= 0001 → 1

Bitwise OR (5 | 3)
 0101
| 0011
= 0111 → 7

Bitwise XOR (5 ^ 3)
 0101
^ 0011
= 0110 → 6

Left Shift (<<)
5 << 1 = 10
(Binary: 0101 << 1 = 1010)

Right Shift (>>)
Example: 5 >> 1 = 2
(Binary: 0101 >> 1 = 0010)


One’s Complement

5-00000101-->8bits
(-5)-11111010-->8bits


Two’s Complement
5-00000101
  11111010-->1's complement
+        1-->2's complement
---------------
  11111011