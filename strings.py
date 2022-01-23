## can change these values as you want

original = ['one', 'two', 'three', 'seven']
add = ['one', 'two', 'five', 'six', 'nine', 'rat']
delete = ['two', 'five']

def func(original, add, delete) -> list:

    ## using sets just to get rid of the potential duplicate problem

    sOG = set()
    sADD = set()
    sDEL = set()
    sResult = set()

    for i in original:
        sResult.add(i)
    for i in add:
        sResult.add(i)
    
    for i in delete:
        if i in sResult:
            sResult.discard(i)

    ## get a list from the set
    
    result = list(sResult)

    ## define a function to be used in sorting

    def compare(string1, string2) -> bool:
        if len(string1) < len(string2):
            return False
        elif len(string1) > len(string2):
            return True
        else:
            if string1 < string2:
                return False
            return True
        
    
    ## implement merge sort with the function listed above
    
    def sort(result) -> list:
        if len(result) > 1:

            mid = len(result)//2

            L = result[:mid]

            R = result[mid:]

            sort(L)

            sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if compare(L[i], R[j]):
                    result[k] = L[i]
                    i += 1
                else:
                    result[k] = R[j]
                    j += 1
                k += 1
            
            while i < len(L):
                result[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                result[k] = R[j]
                j += 1
                k += 1
        
        return result
    
    return sort(result)

print(func(original, add, delete))
                    
            

    