#!/usr/bin/env python
import random,urllib2
from random import shuffle as randomize

present_word = ['acuh','amin','antah','']

def name_meaning_present(name):
	'''
	many parents confused to decide which name is used to his son/daughter's name
	and much affraid of these name is being used by another kids (in this case the parent who won't to be mainstream)
	this situation,pretty much simple in my head.

	another one situation is giving name to something like mountaint maybe,or for some unnamed storm out there ?

	name_meaning_present(name) --> checking whether the name has a mean or not
	generateName(list1, list2, num=5) --> generate random name from list with len(num)
	region_detector --> detect name region based on it signature (because i believe in fact that every name has it's own signature)
	'''
	pass #bugy,remove pass to know,if name mean is present
	global status
	status = ''
	url=urllib2.urlopen('http://www.morewords.com/word/'+name)
	read_data=url.read()
	if re.findall("No words found in this wordlist when searching for",read_data) != []:
		status = 'Present'
	else:
		status='Unpresent'
	print status
def generateName2(list1,list2,num=5):
	global final
	final = ''
	#randomize list
	new_list=randomize(list1)
	for a in new_list:
		if num == 5:
			INDEX1=random.choice([0,1,2,3,4,5,6,7])
			INDEX2=random.choice([0,1,2,3,4,])
			final=list2[INDEX2]+list1[INDEX1]+list1[INDEX2]+list2[INDEX2]+list1[INDEX1]
		elif num == 6:
			INDEX1=random.choice([0,1,2,3,4,5,6,7])
			INDEX2=random.choice([0,1,2,3,4])
			final=list2[INDEX2]+a+list2[INDEX2]+list1[INDEX2]+list2[INDEX2]+list1[INDEX2]
			#         o               r           o               g           o              k

		print final

def generateName(list1,list2,num=5):
	global final
	final = ''
	#randomize list
	for a in list1:
		for b in list2:
			if num == 5:
				INDEX1=random.choice([0,1,2,3,4,5,6,7])
				INDEX2=random.choice([0,1,2,3,4,])
				final=a+b+list1[INDEX2]+list2[INDEX2]+list1[INDEX1]
			elif num == 6:
				INDEX1=random.choice([0,1,2,3,4,5,6,7])
				INDEX2=random.choice([0,1,2,3,4])
				final=a+b+list1[INDEX2]+list2[INDEX2]+list1[INDEX1]+list2[INDEX2]
			print final

def region_detector(name):
	global region
	region = ''
	'''
	example :
	if name = 'sarkov'
	so it must be Russian name,because of there's "v" on the end of the name
	or name = 'suryo'
	it must be Javanese name,signed by "s" on the first and "o" on the last
	'''
	if name:
		if len(name) == 5:
			#start analyzing name
			if name[4] in 'zjv':
				region= 'Russian'
			elif name[0] == 's' and name[4] == '0':
				region='Java Island (Indonesia)'
			elif name[4] == 'y' and name[0] != 'v' and name[1] != 'i' and name[2] != 'c':
				region = 'Chile ('
			print region
		else:
			pass
	else:
		pass


def generate_first_name_len_5(list1,list2):
	pass
	'''generate random name with random alphabet
	'''
	#select random alphabet
	for a in list1:
		for b in list2:
			INDEX1=random.choice([0,1,2,3,4,5,6,7])
			INDEX2=random.choice([0,1,2,3,4,])
			final=a+b+list1[INDEX2]+list2[INDEX2]+list1[INDEX1]
			global detect_region
			detect_region = region_detector(final)
			if detect_region == '':
				res = 'unmatch with current database'
			else:
				res = 'match found'
			if final != None:
				print 'Current Name : {}'.format(final)
				print 'status : '+ res
				print '{} comes from --> '.format(final),region_detector(final)
			else:
				pass