# processs_wit3.py

import os.path
import xml.etree.ElementTree as ET
import re

def dump_sentences(file_in, file_out):

	datum = re.compile('\<seg id="\d+"\> (.*) \<\/seg\>')

	flag = False
	counter = 0
	fout = open(file_out,'w', encoding='utf-8')
	with open(file_in, 'r', encoding='utf-8') as fin:
		for line in fin:
			res = datum.match(line)
			try:
				if res:
					# print(res.group(1))
					fout.write(res.group(1)+"\n")
					counter += 1
			except: 
				print('Error:', line)
				flag = True

	if flag:	
		print('Error dumping from %s to %s' % (file_in, file_out))

	return counter

def main():

	file_in = "wit3/en-de/IWSLT15.TED.tst2012.en-de.de.xml"
	file_out = "wit3/en-de/IWSLT15.TED.tst2012.en-de.de.txt"
	dump_sentences(file_in, file_out)

	file_in = "wit3/en-de/IWSLT15.TED.tst2012.en-de.en.xml"
	file_out = "wit3/en-de/IWSLT15.TED.tst2012.en-de.en.txt"
	dump_sentences(file_in, file_out)

	file_in = "wit3/en-de/IWSLT15.TED.tst2013.en-de.de.xml"
	file_out = "wit3/en-de/IWSLT15.TED.tst2013.en-de.de.txt"
	dump_sentences(file_in, file_out)

	file_in = "wit3/en-de/IWSLT15.TED.tst2013.en-de.en.xml"
	file_out = "wit3/en-de/IWSLT15.TED.tst2013.en-de.en.txt"
	dump_sentences(file_in, file_out)

	print('Done')


def main_old():
	print('hello world')

	datum = re.compile('\<seg id="\d+"\> (.*) \<\/seg\>')

	with open('wit3/en-de/IWSLT15.TED.tst2012.en-de.de.xml', encoding='utf-8') as file:
		# foo = [datum.match(line).group(0) for line in file]
		# print('Lines: ', len(foo), 'example: ', foo[-20])

		counter = 0
		for line in file:
			res = datum.match(line)
			try:
				if res:
					# print(res.group(1))
					counter += 1
			except: 
				print('Error')

		print('total: ', counter)
		# print(foo[10])
		# print(datum.match(foo[10]).group(1))
		# return


	with open('wit3/en-de/IWSLT15.TED.tst2012.en-de.en.xml', encoding='utf-8') as file:
		counter = 0
		for line in file:
			res = datum.match(line)
			try:
				if res:
					# print(res.group(1))
					counter += 1
			except: 
				print('Error')

		print('total: ', counter)
		
	with open('wit3/en-de/IWSLT15.TED.tst2013.en-de.de.xml', encoding='utf-8') as file:
		foo = [line for line in file]
		print('Lines: ', len(foo))

	tree = ET.parse('wit3/en-de/IWSLT15.TED.tst2012.en-de.de.xml')
	root = tree.getroot()
	print('Parsed?', tree, root)
	print([_ for _ in root])



		
if __name__ == '__main__':
	main()