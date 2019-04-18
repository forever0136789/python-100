score=int(input('输入分数：'))
grade=(score>=90) and 'A' or((score>=60) and 'B' or 'C')
print(grade)
