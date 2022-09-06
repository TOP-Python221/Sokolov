for c in input():
  ascii_val = ord(c)
  upper = range(65, 91)
  lower = range(97, 123)
  if ord(c) not in upper and ord(c) not in lower:
    print("NON-ALPHABETICAL CHARACTER FOUND!")
    break
  else:
      print("THE CHARACTER IS A STRING")
      break