chars = [
"pb\\",
"\\gi",
"g\\Z",
"jdi",
"^io",
"aZp",
"\\ig",
"doj",
"ip^",
"nta",
"Zo_",
"jhn",
"`cZ",
"Zno",
"Z&d",
"^v&",
"O>A",
"HP?",
]

for c in chars[::-1]:
	three = ''.join(map(lambda x: chr(ord(x) + 5), c))
	tmp = three[1] + three[0] + three[2]
	print(tmp, end='')
print('ge}')
