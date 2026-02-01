l = ["Rahul", "Meena", "Sharun", "Shaurya", "Mohit"]

def rem(l,word):
    n = []
    for items in l:
        if items != word:
            n.append(items.strip(word))
    return n        
    
print(rem(l,"a"))