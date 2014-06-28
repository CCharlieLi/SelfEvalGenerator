#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,random

Appellation = u"同学 "

def Generator(NameList,EList):
	names = open(NameList)
	sentences = open(EList)
	Savefile = open("result.txt",'w')

	sentenceList = []
	sentenceslines = sentences.readlines()
	for each in sentenceslines:
		each = each.replace('\n','')
		each = each.strip()
		sentenceList.append(each)
		#Savefile.write(each+"...")

	nameslines = names.readlines()
	for each in nameslines:
		each = each.replace('\n','')
		each = each.strip()
		Savefile.write(each + Appellation+ ','.join(random.sample(sentenceList,15)) + u'。' +'\n\n')


	names.close() 
	sentences.close()
	Savefile.close()


if __name__ == "__main__":
	reload(sys) 
	sys.setdefaultencoding('gbk')
	sys.exit(Generator("NameList.txt","EVAList.txt"))