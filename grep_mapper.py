def mapper(input_word, files):

	mapper_output=[]
	
	for file in files:
		count=1
		fp=open(file,"r")
		for line in fp:
			# print("hello")
			# result = re.match(input_word,line)
			# print(line)
			if input_word in line:
				# print("hello",mapper_output)
				mapper_output.append([file,count])
			count+=1
		fp.close()
	return mapper_output		



  # file = open(files)
  # words = []

  # for line in file:
  #   string = [c for c in line.lower() if c.isalpha() or c == ' ']
  #   words += ''.join(string).strip().split(' ')

  # words = sorted(words)

  # return words