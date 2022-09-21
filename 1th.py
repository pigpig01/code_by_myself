print("How many pencils would you like to use:")
p = int(input())
p1 = p * "|"
print("Who will be the first(John, Jack):")
name = input()
names = ["Jack","John"]
if name == names[0]:
  print(p1)
  print(name + "'s turn:")
  name = names[1]
else:
  print(p1)
  print(name + "'s turn!")
  name = names[0]
p2 = int(input())
p3 = p - p2
print(p3 * "|")
if name == names[0]:
  print(name + "'s turn:")
  name = names[1]
else:
  print(name + "'s turn!")
  name = names[0]
while p3 > 0:
  p2 = int(input())
  p3 = p3 - p2
  p4 = p3 * "|"
  if name == names[0] and p3 >= 1:
    print(p4)
    print(name + "'s turn:")
    name = names[1]
  elif name == names[1] and p3 >= 1:
    print(p4)
    print(name + "'s turn!")
    name = names[0]
  else:
    print(name +" won!")
