def mapper(input_file):
  
  file = open(input_file)
  words = []

  for line in file:
    string = [c for c in line.lower() if c.isalpha() or c == ' ']
    words += ''.join(string).strip().split(' ')

  words = sorted(words)

  return words