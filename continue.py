l=[1,5,7]
for n in range(1,11):
    if n in l:
        continue #break breakes out of the entire loop whereas continue skips the cuurent loop iteration only
    print(n)
    print("The above number is not in the list")
