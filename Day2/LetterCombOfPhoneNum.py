''''
store={}
store["2"]="abc"
store["3"]="def"
store["4"]="ghi"
store["5"]="jkl"
store["6"]="mno"
store["7"]="pqrs"
store["8"]="tuv"
store["9"]="wxyz"
def combinations(word,index,result):
    if index==len(word):
        print("".join(result))
        return
    ch=word[index]
    for val in store[ch]:
        result.append(val)
        combinations(word,index+1,result)
        result.pop()
word="5342"
result=[]
combinations(word,0,result)
'''

#leetcode--Letter combinations of a phone number
store = {}
store["1"] = ""
store["2"] = "abc"
store["3"] = "def"
store["4"] = "ghi"
store["5"] = "jkl"
store["6"] = "mno"
store["7"] = "pqrs"
store["8"] = "tuv"
store["9"] = "wxyz"
class Solution(object):
    def printLetter(self, word, index, result, bigResult):
        if index == len(word):
           bigResult.append("".join(result))
           return 
 
        ch = word[index]
        for val in store[ch]:
            result.append(val)
            self.printLetter(word, index + 1, result, bigResult)
            result.pop()
def letterCombinations(self, digits):
    bigResult = []
    if len(digits) == 0:
        return bigResult
        result = []
        self.printLetter(digits, 0, result, bigResult)
        return bigResult
word="7345"