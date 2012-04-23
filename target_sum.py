"""
The file contains 100,000 integers all randomly chosen between 1 and 1,000,000
(there might be some repetitions).This is your array of integers: the ith row of
the file gives you the ith entry of the array.

Here are 9 "target sums", in increasing order:
  231552,234756,596873,648219,726312,981237,988331,1277361,1283379. Your task is
  to implement the hash table-based algorithm explained in the video lectures
  and determine, for each of the 9 target sums x, whether or not x can be formed
  as the sum of two entries in the given array.

  Your answer should be in the form of a 9-bit string, with a 1 indicating "yes"
  for the corresponding target sum and 0 indicating "no". For example, if you
  discover that all of the target sums except for the 5th and the 7th one (i.e.,
  except for 726312 and 988331) can be formed from pairs from the input file,
  then your answer should be "111101011" (without the quotes). We reiterate that
  the answer should be in the same order as the target sums listed above (i.e.,
  in increasing order of the target).
"""
targets = [231552,234756,596873,648219,726312,981237,988331,1277361,1283379]
f = open('HashInt.txt')
d={} # key=a input int, value=frequency
for line in f:
  num = int(line)
  d[num] = d.get(num, 0) + 1
result = ''
for target in targets:
  found = False
  for key in d:
    other = target - key
    # check the existence of 'other'
    if (key == other and d[key] > 1) or (key != other and d.has_key(other)):
      found = True
      break
  if found:
    result += '1'
  else:
    result += '0'
print result
