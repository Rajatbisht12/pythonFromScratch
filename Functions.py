from function import sum

def avg(a,b):
  summ = sum(a,b)
  avg = summ/2
  return avg

def fib(n):
  if n==1:
    print(n)
    return 1
  print(n)
  fib(n-1)

def print_list(lst, ind):
  if ind == len(lst):
    return
  print(lst[ind])
  print_list(lst, ind+1)