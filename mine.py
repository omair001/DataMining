""" Created by Alex """ 
import csv
import re
import string

""" open file """
file = open('train.csv')
reader = csv.reader(file)
data = list(reader)
outputFile = open('output1.csv', 'w')
outputWriter = csv.writer(outputFile)

""" clean """
counter = 0
lst = open('stop_words.lst')
stopword = lst.readlines()
for row in data:
    row[0] = row[0].lower()


    counter = counter + 1
    print counter

    """ remove punctuation and numbers"""

    """ semantic punctuation should not be removed """
    row[0] = row[0].replace(':)',' happyface ')
    row[0] = row[0].replace('=)',' happyface ')
    row[0] = row[0].replace(';)',' winkyface ')
    row[0] = row[0].replace(':(',' sadface ')
    row[0] = row[0].replace('=(',' sadface ')
    row[0] = row[0].replace(': (',' sadface ')
    row[0] = row[0].replace('= (',' sadface ')
    row[0] = row[0].replace(': )',' happyface ')
    row[0] = row[0].replace('= )',' happyface ')

    """ convert text numbers to numeric representation """
    row[0] = re.sub(r'ten',' 0 ', row[0])
    row[0] = re.sub(r'one',' 1 ', row[0])
    row[0] = re.sub(r'two',' 2 ', row[0])
    row[0] = re.sub(r'three',' 3 ', row[0])
    row[0] = re.sub(r'four',' 4 ', row[0])
    row[0] = re.sub(r'five',' 5 ', row[0])
    row[0] = re.sub(r'six',' 6 ', row[0])
    row[0] = re.sub(r'seven',' 7 ', row[0])
    row[0] = re.sub(r'eight',' 8 ', row[0])
    row[0] = re.sub(r'nine',' 9 ', row[0])
    row[0] = re.sub(r'ten',' 10 ', row[0])

    """ special case for percentages """
    row[0] = row[0].replace('% off ','discount')
    ''' 100 % '''

    """ special case for numeric values """
    row[0] = row[0].replace(' 1/2','.5')
    row[0] = row[0].replace('/5','/5stars ')
    row[0] = row[0].replace('/5','/5stars ')
    row[0] = row[0].replace(' out of 5', '/5stars ')
    row[0] = row[0].replace(' out of 10', '/10stars ')
    row[0] = re.sub(r'\s*stars\s*\/5','/5stars', row[0])
    row[0] = re.sub(r'\s*stars\s*\/10','/10stars', row[0])
    row[0] = re.sub(r'(\s|-)+stars\s*','/5stars ', row[0])
    row[0] = re.sub(r'(\s|-)+star\s*','/5stars ', row[0])
    row[0] = row[0].replace('/5stars/5stars','/5stars ')





    """ times """
    row[0] = re.sub(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):[0-5][0-9]$',' ', row[0])

    """ dates """
    regex = r"\d{1-4}\\\d{1-4}\\\d{1-4}"
    result = re.sub(regex, ' ', row[0])

    """ punctuation special cases have been treated, remove remaining punctuation """
    row[0] = row[0].replace("'",'')
    row[0] = re.sub(r'(?<!\d)\.(?!\d)',' ',row[0])
    row[0] = row[0].replace('.','')

    ''' '$', '''

    punct = ['"','#','!','&','$','*','+',',','-','<','=','>','?','@','^','\\','_','`','{','|',
            '}','~',')','(',']','[',':']

    for p in punct:
        row[0] = row[0].replace(p,' ')

    """remove stop words"""
    for wrd in stopword:
        pattern = '\s+' + (wrd.strip()) + '\s+'
        row[0] = re.sub(r'%s' % pattern,' ',row[0])

    """ stem """

    outputWriter.writerow(row)
outputFile.close()