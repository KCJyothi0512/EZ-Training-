#check whether string is palindrome or not using loops(Time complexity->O(n/2))
s=input()
i=0
j=len(s)-1
while i<j:
    if s[i]!=s[j]:
        print('Not palindrome')
        break
    i=i+1
    j=j-1
else:
    print('Palindrome')
