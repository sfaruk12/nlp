#Parse a sentence and draw a tree using malt parsing.
#Note: 1) Java should be installed.
#2) maltparser-1.7.2 zip file should be copied in C:\Users\Beena
#Kapadia\AppData\Local\Programs\Python\Python39 folder and should be
#extracted in the same folder.
#3) engmalt.linear-1.7.mco file should be copied to C:\Users\Beena
#Kapadia\AppData\Local\Programs\Python\Python39 folder
#Source code:
# copy maltparser-1.7.2(unzipped version) and engmalt.linear-1.7.mco files to
#C:\Users\Beena Kapadia\AppData\Local\Programs\Python\Python39 folder
# java should be installed
# environment variables should be set - MALT_PARSER - C:\Users\Beena
#Kapadia\AppData\Local\Programs\Python\Python39\maltparser-1.7.2 and
#MALT_MODEL - C:\Users\Beena
#Kapadia\AppData\Local\Programs\Python\Python39\engmalt.linear-1.7.mco


from nltk.parse import malt
mp = malt.MaltParser('maltparser-1.7.2', 'engmalt.linear-1.7.mco')#file
t = mp.parse_one('I saw a bird from my window.'.split()).tree()
print(t)
t.draw()


#Output:
#(saw I (bird a (from (window. my))))
