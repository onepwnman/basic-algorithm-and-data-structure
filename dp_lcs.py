#!/usr/bin/env  python3
from utill.logger import exe_time_logger
from random import choice
from string import ascii_uppercase

# Longest Common Subsequence(LCS) solved by recursion
@exe_time_logger
def lcs_recursion(S1,S2):
  def _lcs_recursion(s1,s2):
    if s1 == '' or s2 == '':  return 0
    if s1[-1] == s2[-1]:  return 1 + _lcs_recursion(s1[:-1],s2[:-1])
    else:  return max(_lcs_recursion(s1[:-1],s2), _lcs_recursion(s1,s2[:-1]))

  return _lcs_recursion(S1,S2) 


# Longest Common Subsequence(LCS) solved by Top-Down DP
@exe_time_logger
def lcs_dp_top_down(S1,S2):
  m = [[None]*(len(S1)+1) for _ in range((len(S2)+1))]

  def _lcs_dp_top_down(s1,s2):
    if s1 == '' or s2 == '':  return 0
    len1,len2 = len(s1),len(s2) 
    if m[len1][len2] == None:
      if s1[-1] == s2[-1]:
        m[len1][len2] = 1 + _lcs_dp_top_down(s1[:-1],s2[:-1])
      else:
        m[len1-1][len2] = _lcs_dp_top_down(s1[:-1],s2) 
        m[len1][len2-1] = _lcs_dp_top_down(s1,s2[:-1])
        return max(m[len1-1][len2], m[len1][len2-1])

    return m[len1][len2] 

  return _lcs_dp_top_down(S1,S2)


# Longest Common Subsequence(LCS) solved by Bottom-Up DP
# We can get the count of LCS and also exact LCS because unlike recursion
# Dynamic Programming has Memorization feature   
@exe_time_logger
def lcs_dp_bottom_up(S1,S2):
  len1,len2 = len(S1),len(S2)
  m = [[0]*(len1+1) for _ in range(len2+1)]
  s = ''

  # Map the LCS count
  for i in range(len1):
    for j in range(len2):
      if S1[i] == S2[j]:
        m[i+1][j+1] = m[i][j] + 1
      else:
        m[i+1][j+1] = max(m[i+1][j], m[i][j+1])

  # Get the LCS
  while len1 != 0 and len2 != 0:
    if m[len1][len2] > m[len1-1][len2] and m[len1][len2] > m[len1][len2-1]:
      s += S1[len1-1]
      len1,len2 = len1-1,len2-1
    elif m[len1-1][len2] > m[len1][len2-1]:
      len1 -= 1
    else:
      len2 -= 1

  return m[-1][-1], s[::-1]




if __name__ == '__main__':
  f = lambda : ''.join([choice(ascii_uppercase[:4]) for _ in range(6)])
  S1,S2 = f(),f()
  print("S1: {}, S2: {}\n".format(S1,S2))
  print("Answer: {}".format(lcs_dp_top_down(S1,S2)))
  print("Answer: {}, Answer Subsequence: {}".format(*lcs_dp_bottom_up(S1,S2)))
  print("Answer: {}".format(lcs_recursion(S1,S2)))
  

