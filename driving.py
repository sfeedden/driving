country = input('請問你是哪國人？')
age = input('請問你的年齡？')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照！')
	else:
		print('你還太小了！')
elif country == '美國':
	if age >= 16:
		print('你可以考駕照！')
	else:
		print('你還太小了！')
else:
	print('你只能輸入台灣or美國！')