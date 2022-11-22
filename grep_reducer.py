def reducer(input):
  
  words = input
  reducer_output = {}

  for i in words:
    if i[0] in reducer_output:
      reducer_output[i[0]].append(i[1])
    else:
      reducer_output[i[0]] = [i[1]]  

  return reducer_output  