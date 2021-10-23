alphabet = [
	'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ',
	'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص',
	'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق',
	'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي'
]

def get_index(char):
	for i in range(len(alphabet)):
		if(char == alphabet[i]):
			return i
	return 28

def encrypt(src_text, key):
	cipher_text = ''
	for i in range(len(src_text)):
		char = src_text[i].lower()
		if ord(char) >= 97 and ord(char) <= 122:
			cipher_text += chr((ord(char) + key - 97) % 26 + 97)
		elif ord(char) >= 1569 and ord(char) <= 1610:
			# cipher_text += chr((ord(char) + key - 1575) % 41 + 1575)
			idx = get_index(char)
			if idx != 28:
				cipher_text += alphabet[(idx + key) % 28]
			else:
				cipher_text += char
		else:
			cipher_text += char
	return cipher_text

def decrypt(cipher_text, key):
	src_text = ''
	for i in range(len(cipher_text)):
		char = cipher_text[i].lower()
		if ord(char) >= 97 and ord(char) <= 122:
			src_text += chr((ord(char) - key - 97) % 26 + 97)
		elif ord(char) >= 1569 and ord(char) <= 1610:
			# cipher_text += chr((ord(char) - key - 1575) % 41 + 1575)
			idx = get_index(char)
			if idx != 28:
				src_text += alphabet[(idx - key) % 28]
			else:
				src_text += char
		else:
			src_text += char
	return src_text

def break_cipher(cipher_text):
	src_text = [''] * 54
	for i in range(54):
		for j in range(len(cipher_text)):
			char = cipher_text[j].lower()
			if ord(char) >= 97 and ord(char) <= 122:
				src_text[i] += chr((ord(char) - (i + 1) - 97) % 26 + 97)
			elif ord(char) >= 1569 and ord(char) <= 1610:
				idx = get_index(char)
				if idx != 28:
					src_text[i] += alphabet[(idx - (i + 1)) % 28]
				else:
					src_text[i] += char
			else:
				src_text[i] += char
		src_text[i] = str(i + 1) + " => " + src_text[i]
	return src_text

text = input('Please type your message: ')

while True:
	op = input('1. Encrypt message\n2. Decrypt message\n3. Break cipher message\nPlease choose an option: ')
	try:
		op = int(op)
		if(op == 1 or op == 2 or op == 3):
			break
		else:
			print('\nPlease choose a valid option!')
	except:
		print('\nPlease type a number!')

if(op != 3):
	key = input('Please type the \'SHIFT KEY\': ')
	key = int(key)
	print('\nKey: ' + str(key))

if(op == 1):
	print('Source text: ' + text)
	print('Cipher text: ' + encrypt(text, key))
if(op == 2):
	print('Cipher text: ' + text)
	print('Source text: ' + decrypt(text, key))

if(op == 3):
	list = break_cipher(text)
	print('Cipher text: ' + text)
	print('Source text possibilities:\n' + '\n'.join(list))