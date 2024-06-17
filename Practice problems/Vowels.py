#parent to child
''''
def countVowels1(word,index,n,result):
    if index==n:
        print("Vowel count is:",result)
        return
    vowels="aeiouAEIOU"
    if word[index] in vowels:
        result+=1
    countVowels1(word,index+1,n,result)
word="abcdefgIrE"
n=len(word)
countVowels1(word,0,n,0)
'''

#child to parent
def countVowels1(word,index,n):
    if index==n:
        return 0
    nextVowelCount=countVowels1(word,index+1,n)
    vowels="aeiouAEIOU"
    if word[index] in vowels:
        nextVowelCount+=1
    return nextVowelCount
word="abcdefgIrE"
n=len(word)
print(countVowels1(word,0,n))