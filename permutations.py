

### determine permutations recursively

string = 'abcd'
out = ''
used = [0 for x in string]
def permute():
  global string, out, used
  if len(out) == len(string):
    print out
    break
  for x in range(len(string)):
    if used[x] == 1:
      continue
    out = out + string[x]
    used[x] = 1
    permute()
    used[x] = 0
    out = out[:-1]




### determine permutations iteratively

def permute_iter(string = 'abcd'):
  used = [0 for x in string]
  q = [-1]
  while q:
    if len(q) == len(string):
      print ''.join([string[i] for i in q])
    x = q.pop()
    used[x] = 0
    x+=1
    while x < len(string):
      if used[x] == 0:
        q.append(x)
        used[x] = 1
        x = 0
      else:
        x += 1
      if len(q) == len(string):
        break

