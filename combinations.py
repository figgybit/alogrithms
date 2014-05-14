
# determine combinations iteratively

def combos_iter(string = 'abcdefghij', num = 5):
  q=[-1]
  while q:
    if len(q) == num:
      print ''.join([string[i] for i in q])
    x = q.pop()
    x+=1
    while x < len(string):
      q.append(x)
      x+=1
      if len(q) == num:
        break

# determine combinations recursively

string = 'abcdefghijklmnopqrstuvwxyz'
num = 5
used = [0 for x in range(len(string))]
out = ''
def combos():
  global string, num, used, out
  if len(out) == num:
    print out
    return
  count=0
  for x in range(len(string)):
    if used[x] == 1:
      count += 1
    # if len(out) == num:
    #   break
    if count == len(out) and used[x] == 0:
      out = out+string[x]
      used[x] = 1
      combos()
      used[x] = 0
      out = out[:-1]
