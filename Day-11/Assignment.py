# Find elements that appear in exactly 2 out of the 4 sets
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {5, 6, 7, 8, 9}
D = {1, 3, 7, 9, 10}
print("Elements in exactly 2 sets:",((A & B) - (C | D)) |((A & C) - (B | D)) | ((A & D) - (B | C)) |((B & C) - (A | D)) |((B & D) - (A | C)) |((C & D) - (A | B)))