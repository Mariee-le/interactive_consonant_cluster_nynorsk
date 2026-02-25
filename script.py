import nltk, re

from nltk.corpus import udhr
nltk.download('udhr')
from nltk.corpus import words


'''find the vocabulary of Norwegian_Norsk-Nynorsk-Latin1 from the 
corpus udhr'''

nynorsk_words = sorted(set(udhr.words('Norwegian_Norsk-Nynorsk-Latin1')))



'''find words with consonant clusters using regex and make it into a list'''

cc  = [(c, w) for w in nynorsk_words for c in 
re.findall(r'[QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjklzxcvbnm]{2}', w)]
ccc= [(c, w) for w in nynorsk_words for c in 
re.findall(r'[QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjklzxcvbnm]{3}', w)]
cccc = [(c, w) for w in nynorsk_words for c in 
re.findall(r'[QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjklzxcvbnm]{4}', w)]
ccccc = [(c, w) for w in nynorsk_words for c in 
re.findall(r'[QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjklzxcvbnm]{5}', w)]


'''interekative, write number of wanted 
consonantcluster'''


if __name__ == "__main__":
    while True:
        text = input("\n'c' represents the consecutive number of a consonant.\nWrite 'cc', 'ccc', 'cccc' or 'ccccc' and see what happens (write exit to exit) ").strip()

        if text.lower() == "exit":
           print("Goodbye")
           break
   
        if text.lower() == "cc":
            print(f"\nYou wrote 'cc', which represents two consecutive consonats in a 
word.\nThere are {len(cc)} occurences of this type of cluster in the text\n", cc)
        elif text.lower() == "ccc":
            print(f"\nYou wrote 'ccc', which represents three consecutive consonats in a 
word.\nThere are {len(ccc)} occurences of this type of cluster in the text\n", ccc)
        elif text.lower() == "cccc":
            print(f"\nYou wrote 'cccc', which represents four consecutive consonats in a 
word.\nThere are {len(cccc)} occurences of this type of cluster in the text\n", cccc)
        elif text.lower() == "ccccc":
            print(f"\nYou wrote 'ccccc', which represents five consecutive consonats in 
a word.\nThere is only  {len(ccccc)} occurence of this type of cluster in the text\n", 
ccccc)
        else:
           print("Your number is out of range:(")
