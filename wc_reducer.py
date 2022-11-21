def reducer(input):
  
  words = input
  mapper_output = []
  for i in words:
    mapper_output.append([i,1])

  reducer_output = {}

  for i in words:
    if i in reducer_output:
      reducer_output[i] += 1
    else:
      reducer_output[i] = 1

  for i in reducer_output:
    print(i,reducer_output[i])