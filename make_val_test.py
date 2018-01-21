# make_val_test.py
# makes the validation and test sets for a pair of parallel texts

# hardcoded files for now:

language = 'FR-EN'
language = 'EN-EN-u'
language = 'EN-FR'



# Note this works for EN-FR as well
if language =='FR-EN':

	decimation = 1
	monolang = False

	# Source files for all lines
	source1 = "/data/europarl-v7/europarl-v7.fr-en.en"
	source2 = "/data/europarl-v7/europarl-v7.fr-en.fr"

	# Renamed files containing splits
	train1 = "/data/europarl-v7/europarl-v7.fr-en.en.train"
	train2 = "/data/europarl-v7/europarl-v7.fr-en.fr.train"

	val1 = "/data/europarl-v7/europarl-v7.fr-en.en.val"
	val2 = "/data/europarl-v7/europarl-v7.fr-en.fr.val"

	test1 = "/data/europarl-v7/europarl-v7.fr-en.en.test"
	test2 = "/data/europarl-v7/europarl-v7.fr-en.fr.test"

if language == 'EN-EN-u':

	decimation = 10
	monolang = True

	source1 = "/data/europarl-v7/europarl-v7.fr-en.en"
	source2 = "/data/europarl-v7/europarl-v7.fr-en.en"

	train1 = "/data/europarl-v7/en-en.train"
	train2 = "/data/europarl-v7/en-en.train"

	val1 = "/data/europarl-v7/en-en.val"
	val2 = "/data/europarl-v7/en-en.val"

	test1 = "/data/europarl-v7/en-en.test"
	test2 = "/data/europarl-v7/en-en.test"

	print('Splitting for EN-EN-u using only English file, with decimation %d' % decimation)

# included for separation purposes
if language =='EN-FR':

	decimation = 50
	monolang = False

	# Source files for all lines
	source1 = "/data/europarl-v7/europarl-v7.fr-en.en"
	source2 = "/data/europarl-v7/europarl-v7.fr-en.fr"

	# Renamed files containing splits
	train1 = "/data/europarl-v7/en-fr.en.train"
	train2 = "/data/europarl-v7/en-fr.fr.train"

	val1 = "/data/europarl-v7/en-fr.en.val"
	val2 = "/data/europarl-v7/en-fr.fr.val"

	test1 = "/data/europarl-v7/en-fr.en.test"
	test2 = "/data/europarl-v7/en-fr.fr.test"

def main():

	ftrain1 = open(train1, 'w')
	fval1 = open(val1, 'w')
	ftest1 = open(test1, 'w')

	if not monolang:
		ftrain2 = open(train2, 'w')
		fval2 = open(val2, 'w')
		ftest2 = open(test2, 'w')

	ucount = 0
	line_count = 0
	with open(source1,'r') as fin:
		for line in fin:
			if line_count < 2000:
				fval1.write(line)
			elif line_count < 4000:
				ftest1.write(line)
			else:
				if line_count % decimation == 0:
					ftrain1.write(line)
			if not 'u' in line:
				ucount += 1
			line_count += 1

	print('Total line count: ', line_count)
	# print('Of which %d do not have u' % ucount)

	if not monolang:
		line_count = 0
		with open(source2,'r') as fin:
			for line in fin:
				if line_count < 2000:
					fval2.write(line)
				elif line_count < 4000:
					ftest2.write(line)
				else:
					if line_count % decimation == 0:
						ftrain2.write(line)
				line_count += 1

if __name__ == "__main__":
	main()