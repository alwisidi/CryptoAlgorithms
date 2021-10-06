def encrypt(src_text, key):
	cipher_text = ''
	for i in range(len(src_text)):
		char = src_text[i].upper()
		if(ord(char) >= 65 and ord(char) <= 90):
			cipher_text += chr((ord(char) + key - 65) % 26 + 65)
		else:
			cipher_text += char
	return cipher_text

def decrypt(cipher_text, key):
	src_text = ''
	for i in range(len(cipher_text)):
		char = cipher_text[i].upper()
		if(ord(char) >= 65 and ord(char) <= 90):
			src_text += chr((ord(char) - key - 65) % 26 + 65)
		else:
			src_text += char
	return src_text

def break_cipher(cipher_text):
	src_text = [''] * 25
	for i in range(25):
		for j in range(len(cipher_text)):
			char = cipher_text[j].upper()
			if(ord(char) >= 65 and ord(char) <= 90):
				src_text[i] += chr((ord(char) - (i + 1) - 65) % 26 + 65)
			else:
				src_text[i] += char
	return src_text

text = input('Please type your message: ')

while True:
	op = input('1. Encrypt message 2. Decrypt message 3. Break cipher message\nPlease choose an option: ')
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
	print('\n\nKey: ' + str(key))

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