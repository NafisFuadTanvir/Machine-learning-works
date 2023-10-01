string= input("enter the string:-")
result=""

for i in string:
  count=0

  if i not in result:
    for j in string:
      if i==j:
        count+=1

    result+= f"'{i}': {count} "

print(result)