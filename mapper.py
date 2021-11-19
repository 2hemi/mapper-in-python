f = open(r'purchases.txt')

for i in f :
	data = i.strip().split('\t')

	if len(data) == 6:
		print('magasin = ',data[2],' price = ',data[4])
