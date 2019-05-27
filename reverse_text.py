# 1. read file
with open('mulcam.txt', 'r') as f:
  lines = f.read(lines()) # list

# 2. reverse
lines.reverse()

# 3. write files
with open('mulcam.txt', 'w') as f:
  f.writelines(lines)

# for
for i in range(10):
  print(i)

print(i) # => 9