country = input('請問你是哪國人？')
age = input('請問你的年齡？')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照！')
	else:
		print('你還太小了！')