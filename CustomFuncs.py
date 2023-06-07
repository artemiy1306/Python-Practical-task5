def exponentiation(a, b):
  if b == 0: return 1
  return exponentiation(a, b - 1) * a

def sum(a,b):
    if b == 0:
        return a
    return sum(a,b-1) + 1