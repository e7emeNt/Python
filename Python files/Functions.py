# -------------- recursion function ----------- #
def recurMul(a, b):
    if b == 1:
        return a
    else:
        return a + recurMul(a, b-1)


def recurFac(a):
    if a == 1:
        return a
    else:
        return a * recurFac(a-1)


def recurPower(a, b):
    if b == 0:
        return 1
    else:
        return a * recurPower(a, b-1)


def iterGcd(a, b): # iteritive solution
    guess = min(a, b)
    while a % guess != 0 or b % guess != 0 and guess > 1:
        guess -= 1
    return guess


def recurGcd(a, b): # recursive solution
    if b == 0:
        return a
    else:
        return recurGcd(b, a%b)



# ------------- Find element in list ------------- #
# iteritive solution
def search(list, element):
    for e in list:
        if e == element: 
            return True
    return False


# Recursive solution
def rSearch(list,element):
    if element == list[0]:
        return True
    if len(list) == 1:
        return False
    return rSearch(list[1:],element)


# Pythonic Binary Serch(Sorted List)
def rBinarySearch(list,element):
    if len(list) == 1:
        return element == list[0]
    mid = len(list)/2
    if list[mid] > element:
        return rBinarySearch( list[ : mid] , element )
    if list[mid] < element:
        return rBinarySearch( list[mid : ] , element)
    return True


# --------- Find element in increasing order list --------#

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False


# --------------- tower game! ----------------- #
def printMove(fr, to):
    print 'move from ' + str(fr) + ' to ' + str(to)

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)


# ------------------ fibonacci ! ---------------- #
def fib(n):
    assert type(x) == int and x >= 0
    if x == 0 or x == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#------------------- palindrome ! ---------------- #
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))



# -------------- semordnilap ! --------------- #
def semordnilapWrapper(str1, str2):
    if len(str1) == 1 or len(str2) == 1:
        return False

    if str1 == str2:
        return False

    return semordnilap(str1, str2)

def semordnilap(str1, str2):
    if len(str1) != len(str2):
        return False

    if len(str1) == 1:
        return str1 == str2

    if str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    else:
        return False

      
# -------------- Radiation Exposure!! -------------- 
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    result = 0
    i = int((stop - start) / step)
    for x in range(0, i):
        result += f(start + x * step) * step
    return result


# -------------- Merge Sort ! -------------- 
def mergeSort(lst):
    
    result = []
    if len(lst) < 2:
        return lst
    
    mid = int(len(lst)/2)
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1

    result += left[i:]
    result += right[j:]

    return result

# ------------ MIT way to do merge sort! ------------
import operator

# Merge complexity is O(len(L))
def merge(left, right, compare):
    result = []
    i, j = 0, 0
    # compare left list and right list from 1st element of them
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # add remaining elements of left list
    while (i < len(left)):
        result.append(left[i])
        i += 1
    # add remaining elements of right list
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


# Mergesort complexity is O(len(L) * log(len(L)))
def mergeSort(L, compare = operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)


# -------------- Quick Find !# -------------- 

# idd = []
# for i in range(0, n):
#     idd.append(i)


def connected(p, q):
    return idd[p] == idd[q]


def union(p, q):
    pidd = idd[p]
    qidd = idd[q]
    for i in range(0, len(idd)):
        if idd[i] == pidd:
            idd[i] = qidd



# -------------- Weighted Quick Union ! -------------- 

# n = 20

# idd = []
# sz = []
# for i in range(0, n):
#     idd.append(i)
#     sz.append(1)


def root(i):
    while i != idd[i]:
        idd[i] = idd[idd[i]]
        i = idd[i]
    return i


def connected2(p, q):
    return root(p) == root(q)


def union2(p, q):
    i = root(p)
    j = root(q)
    if i == j:
        return
    if sz[i] < sz[j]:
        idd[i] = j
        sz[j] += sz[i]
    else:
        idd[j] = i
        sz[i] += sz[j]



# ------------ Find All subsets (O(c**n))
def allSubsets(L):
    res = []
    if len(L) == 0:
        return [[]]

    # get all subsets without last element
    smaller = allSubsets(L[:-1])
    # create a list of just last element
    extra = L[-1:]   
    new = []
    # for all smaller solutions, add one with last element
    for small in smaller:
        new.append(small + extra)
    #combine those with last element and those without
    return smaller + new


# ----------- Selection Sort -------------

def selSort(L):
    for i in range(len(L) - 1):
        minIdx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIdx = j
                minVal = L[j]
            j += 1
        tmp = L[i]
        L[i] = L[minIdx]
        L[minIdx] = tmp


# ---------- Swap Sort!(why?) ------------

# sort list in increasing order
def swapSort(L): 
    """ L is a list on integers """
    print "Original List: ", L
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print L

    return L

# sort list in decresing order
def modSwapSort(L): 
    """ L is a list on integers """
    print "Original List: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print L
    return L


# ------------ Count Inversions -------------

# O(n log n)

def count_inversion(lst):
    return merge_count_inversion(lst)[1]

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count        


# Problem 3: Recursive String Reversal
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if aStr == "":
        return aStr
    else:
        return reverseString(aStr[1:]) + aStr[0]

print reverseString("123456789")


# Problem 4: X-ian
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    if x == "":
        return True
    elif word == "":
        return False
    elif x[0] == word[0]:
        return x_ian(x[1:], word[1:])
    else:
        return x_ian(x, word[1:])
