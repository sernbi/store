i = 9
while i>=1:
    j = 1
    while j<=i:
        a = j*i
        print("%dx%d=%d "%(i,j,a),end="")
        j+=1
    i-=1
    print()