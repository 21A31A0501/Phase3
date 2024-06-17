def printBinaryNumbers(size,result,n):
    if size==n:
        print(result)
        return 
    printBinaryNumbers(size+1,result+'1',n)
    printBinaryNumbers(size+1,result+'0',n)
n=int(input())
printBinaryNumbers(0,'',n)