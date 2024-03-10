alphabet= input().upper()
alphabets = list(set(alphabet))

english = []

for i in alphabets:
	words = alphabet.count(i)
	english.append(words)


if english.count(max(english))>=2:
	print("?")
else:
	print(alphabets[english.index(max(english))])