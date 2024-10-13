def fun(var):
  n = var
  while n < 10:
    print("hello")
    n += 1
  print(n)

def mul(var):
  n = 1
  while n <=10:
    print(n*var)
    n += 1

def search(var):
  i = 0
  while i < len(var):
    print(var[i])
    i += 1

def search_num(tup, ele):
  i = 0
  while i < len(tup):
    if tup[i] == ele:
      return i
    else:
       print("Finding...")
    i += 1
  return -1

def char(var):
  for char in var:
    if(char == 'a'):
      print(f"Found a at {var.index(char)}")
      break
    print(char)
    print("Not found")
  print("END")

def empty():
  for i in range(5):
    pass
  print("END")