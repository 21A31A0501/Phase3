def moveAllDiscs(n,src,dest,extra):
    if n==1:
        print("Move 1st disc from",src,"to",dest)
        return
    # Moving all (n - 1) discs from src to extra 
    # using dest as extraSpace
    moveAllDiscs(n-1,src,dest,extra)
    print("Move", n, "th disc from", src, "to", dest)
    # Moving all (n - 1) discs from extra to dest
    # using src as extraSpace
    moveAllDiscs(n - 1, extra, src, dest)
 
moveAllDiscs(3, "source", "extraSpace", "destination")
print("\n\n\n\n\n")



class Solution:
    def toh(self, N, fromm, to, aux):
        result = [0]
        
        def solveIt(N, fromm, to, aux):
            if N == 1:
                print("move disk 1 from rod", fromm, "to rod", to)
                result[0] += 1
                return 
            solveIt(N - 1, fromm, aux, to)
            print("move disk", N, "from rod", fromm, "to rod", to)
            result[0] += 1
            solveIt(N - 1, aux, to, fromm)
            
        solveIt(N, fromm, to, aux)
        return result[0]