i = 1
while i<10:
    j = 1
    while j<(i+1):
        a = i*j
        print("%dx%d=%d "%(i,j,a),end="")
        j+=1
    i+=1
    print()