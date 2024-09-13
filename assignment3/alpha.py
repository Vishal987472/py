alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def vowel(alpha):
    vowels = ['a','e','i','o','u']
    # if alpha == vowels:
    #     return True
    # else:
    #     return False
    return alpha in vowels

arr = filter(vowel, alphabets)
for i in arr:
    print(i)
# print(arr)
# result = list(arr)
# print(result)