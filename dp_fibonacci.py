#!/usr/bin/env  python3
from utill.logger import exe_time_logger


# Common solution implementied by recursion
@exe_time_logger
def fibo_recursion(n):
  def _fibo_recursion(x):
    if x <= 2:  return 1
    return _fibo_recursion(x-1) + _fibo_recursion(x-2)

  return _fibo_recursion(n)
 

# DP Top-Down implementation
@exe_time_logger
def fibo_dp_top_down(n):
  m = [0]*(n+1)
  def _fibo_dp_top_down(x):  
    if x <= 2:  return 1
    if m[x] == 0:
      m[x] = _fibo_dp_top_down(x-2) + _fibo_dp_top_down(x-1)
    return m[x]

  return _fibo_dp_top_down(n) 
    

# DP Bottom-Up implementation
@exe_time_logger
def fibo_dp_bottom_up(n):
  m = [0]*(n+1)
  def _fibo_dp_bottom_up(x):
    m[1],m[2] = 1,1
    for i in range(3,x+1):
      m[i] = m[i-2] + m[i-1]
    return m[x] 

  return _fibo_dp_bottom_up(n)

if __name__ == '__main__':
  num = int(input("Enter number: "))
  print("Answer: {}".format(fibo_recursion(num)))
  print("Answer: {}".format(fibo_dp_top_down(num)))
  print("Answer: {}".format(fibo_dp_bottom_up(num)))
