# solution 1
def isAnagram(s: str, t: str) -> bool:
   if len(s) == len(t):
        map1 = {}
        map2 = {}
        arrayOfTrue = []

        for x in s:
            num = map1.get(x) or 0
            map1[x] = num + 1

        for x in t:
            num = map2.get(x) or 0
            map2[x] = num + 1

        for key in map1.keys():
            if map1.get(key) == map2.get(key):
                arrayOfTrue.append(True)
            else:
                arrayOfTrue.append(False)

        for key in map2.keys():
            if map2.get(key) == map1.get(key):
                arrayOfTrue.append(True)
            else:
                arrayOfTrue.append(False)

        return not arrayOfTrue.__contains__(False)
   else:
       return False

# Example usages
print(isAnagram('sahil', 'shila'))  # Output: True
print(isAnagram('sahil', 'lisah'))  # Output: False
