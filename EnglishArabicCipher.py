# # alphabet = [
# #   'a', 'b', 'c', 'd', 'e', 'f',
# #   'g', 'h', 'i', 'j', 'k', 'l',
# #   'm', 'n', 'o', 'p', 'q', 'r',
# #   's', 't', 'u', 'v', 'w', 'x',
# #   'y', 'z', 'ا', 'ب', 'ت', 'ث',
# #   'ج', 'ح', 'خ', 'د', 'ذ', 'ر',
# #   'ز', 'س', 'ش', 'ص', 'ض', 'ط',
# #   'ظ', 'ع', 'غ', 'ف', 'ق', 'ك',
# #   'ل', 'م', 'ن', 'ه', 'و', 'ي'
# # ]

# alphabet = [
# 	'ا', 'a', 'ب', 'b', 'ت', 'c',
# 	'ث', 'd', 'ج', 'e', 'ح', 'f',
# 	'خ', 'g', 'د', 'h', 'ذ', 'i',
# 	'ر', 'j', 'ز', 'k', 'س', 'l',
# 	'ش', 'm', 'ص', 'n', 'ض', 'o',
# 	'ط', 'p', 'ظ', 'q', 'ع', 'r',
# 	'غ', 's', 'ف', 't', 'ق', 'u',
# 	'ك', 'v', 'ل', 'w', 'م', 'x',
# 	'ن', 'y', 'ه', 'z', 'و', 'ي'
# ]

# def get_index(char):
# 	for i in range(len(alphabet)):
# 		x = bool(char == alphabet[i])
# 		if(x):
# 			print(alphabet[i])
# 			print(x)
# 			return i
# 	return 54

# def encrypt(src_text, key):
# 	cipher_text = ''
# 	for i in range(len(src_text)):
# 		char = src_text[i].lower()
# 		# print(char)
# 		idx = get_index(char)
# 		print(idx)
# 		if(idx == 54):
# 			cipher_text += char
# 		else:
# 			print(char + ": " + str((idx + key) % 54))
# 			cipher_text += alphabet[(idx + key) % 54]
# 	return cipher_text
# text = "AbCD EFاب"
# # print("Cipher text: " + encrypt(text, 2))
# # print("Source text: " + text)

def encrypt(src_text, key):
	cipher_text = ''
	for i in range(len(src_text)):
		char = src_text[i].lower()
		if ord(char) >= 97 and ord(char) <= 122:
			cipher_text += chr((ord(char) + key - 97) % 26 + 97)
		elif ord(char) >= 1569 and ord(char) <= 1610:
			cipher_text += "x"
			# cipher_text += chr((ord(char) + key - 1575) % 41 + 1575)
		else:
			cipher_text += char
	return cipher_text

print(ord("ا"))
print(ord("ي"))
for i in range(35):
	print(chr(1575+i))