l = []
ch = 1
print("Enter the values for list(enter finish when your done):")
while 1:
	ch = input()
	if ch == 'finish':
		break
	l.append(ch)

print(l)

while 1:
	print("Enter the operation:")
	str = input()
	print(str)
	a = str.split()
	if a[1] == '':
		cmd1 = str(a[0])
		print(cmd1)
	break
