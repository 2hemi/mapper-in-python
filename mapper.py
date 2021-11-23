#f = open(r'purchases.txt')

import sys

for i in sys.stdin :
	data = i.strip().split('\t')

	if len(data) == 6:
		print('magasin = ',data[2],' price = ',data[4])
