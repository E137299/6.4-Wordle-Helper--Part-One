def print_wordbank(wordbank):
    for i in range(0, len(wordbank),10):
        print('   '.join(wordbank[i:i+10]))

'''
Import New York Times' wordbank
'''
words = open("wordbank.txt","r") #opens text file for reading
wordbank = words.read() #stores contents of txt file in variable
wordbank = wordbank.split() #place words into a list.

print_wordbank(wordbank)
