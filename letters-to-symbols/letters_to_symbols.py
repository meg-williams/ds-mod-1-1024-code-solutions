# -*- coding: utf-8 -*-
"""letters_to_symbols.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14kHIXq-a9qNG7uNrwyLgeA-O76tJIj2J

if elment[1] = element[n+1] continue
  print element+final index or len?
  append
"""

s = "AAAABBBCCDAAA"

def letters_to_sybomls(x):

  count = 1
  result = ""

  for i in range(len(x)):
    if i == (len(x) -1):
      result += str(count) + x[i]
      return result

    elif x[i] == x[i +1]:
      count = count + 1

    else:
      result += str(count) + x[i]
      count = 1

letters_to_sybomls(s)

