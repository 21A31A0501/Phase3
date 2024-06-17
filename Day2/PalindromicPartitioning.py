#Given a string(word) s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
def printAllPartitions(index, word, result, path):
    if index == len(word):
        result.append(path[:])
        return
    currentWord = ""
    for position in range(index, len(word)):
        currentWord += word[position]
        # Below we are trying to check whether the substring is a palindrome or not
        if currentWord == currentWord[::-1]:
            path.append(currentWord)
            printAllPartitions(position + 1, word, result, path)
            path.pop()
word="aab"
result = []
path = []
printAllPartitions(0, word, result, path)
print(result)