#Discussion 2: 1.4
y = "y"
h = y
def y(y):
  h = "h"
  if y == h:
      return y + "i"
  y = lambda y: y(h)
  return lambda h: y(h)
y = y(y)(y)
