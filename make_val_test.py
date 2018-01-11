# make_val_test.py
# makes the validation and test sets for a pair of parallel texts

# hardcoded files for now:
source1 = "/data/europarl-v7/europarl-v7.fr-en.en"
source2 = "/data/europarl-v7/europarl-v7.fr-en.fr"

train1 = "/data/europarl-v7/europarl-v7.fr-en.en.train"
train2 = "/data/europarl-v7/europarl-v7.fr-en.fr.train"

val1 = "/data/europarl-v7/europarl-v7.fr-en.en.val"
val2 = "/data/europarl-v7/europarl-v7.fr-en.fr.val"

test1 = "/data/europarl-v7/europarl-v7.fr-en.en.test"
test2 = "/data/europarl-v7/europarl-v7.fr-en.fr.test"


def main():

	ftrain1 = open(train1, 'w')
	ftrain2 = open(train2, 'w')

	fval1 = open(val1, 'w')
	fval2 = open(val2, 'w')

	ftest1 = open(test1, 'w')
	ftest2 = open(test2, 'w')



	line_count = 0
	with open(source1,'r') as fin:
		for line in fin:
			if line_count < 2000:
				fval1.write(line)
			elif line_count < 4000:
				ftest1.write(line)
			else:
				ftrain1.write(line)
			line_count += 1

	print('Total line count: ', line_count)

	line_count = 0
	with open(source2,'r') as fin:
		for line in fin:
			if line_count < 2000:
				fval2.write(line)
			elif line_count < 4000:
				ftest2.write(line)
			else:
				ftrain2.write(line)
			line_count += 1





if __name__ == "__main__":
	main()