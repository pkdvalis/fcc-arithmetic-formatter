def arithmetic_arranger(problems, *answers):

  num_of_problems = len(problems)
  if num_of_problems > 5: return "Error: Too many problems."

  
  if answers:
    num_of_lines = 5
  else: num_of_lines = 4
    
  arranged_problems = []
  
  # break up the numbers
  for prob in problems:
    arranged_problems.append(prob.split())
    #print(arranged_problems)

  #checks
  for prob in arranged_problems:
    #check operator
    if prob[1] != '+' and prob[1] != '-': return "Error: Operator must be '+' or '-'."
    
    #check digits
    if str(prob[0]).isdigit() and str(prob[2]).isdigit():
      pass
    else:
      return "Error: Numbers must only contain digits."
    
    #check number of digits
    if len(str(prob[0])) < 5 and len(str(prob[2])) < 5:
      pass
    else:
      return "Error: Numbers cannot be more than four digits."
    
  #add the lines
  ans = 0
  for prob in arranged_problems:
    arranged_problems[ans].append('-')
    if len(prob[0]) > len(prob[2]): 
      for x in range(len(prob[0]) + 1):
        prob[3] = prob[3] + '-'
    else:
        for x in range(len(prob[2]) + 1):
          prob[3] = prob[3] + '-'
       
    ans = ans + 1
    
  # print(arranged_problems)

     
  #fill in the answers
  ans = 0
  for prob in arranged_problems:
    
    if prob[1] == '+':
      arranged_problems[ans].append(str(int(prob[0]) + int(prob[2])))

    if prob[1] == '-':
      arranged_problems[ans].append(str(int(prob[0]) - int(prob[2])))
      
    ans = ans + 1
  
  #add spaces, operators and lengths of the 2nd line
  for prob in arranged_problems:
    if len(prob[0]) > len(prob[2]): 
      for x in range(len(prob[0]) - len(prob[2])):
        prob[2] = " " + prob[2]
            
    prob[2] = prob[1] + " " + prob[2]
    prob.append(len(prob[2]))

  width = 4
  result = str()

  # format the final string
  for x in range(num_of_lines):
    if x != 1:
      current_problem = 0
      for col in arranged_problems:
        current_problem += 1
        if current_problem < num_of_problems:
          result += (str(f"{col[x]:>{col[5]}}    "))
        else:
          result += (str(f"{col[x]:>{col[5]}}\n"))
        
  
    
  print(repr(result))
  arranged_problems = result.rstrip("\n")
  
  return arranged_problems

