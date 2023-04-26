def solution(N):
    # Implement your solution here
    binary=bin(N)
    binary=binary[2:]
    # print(binary)
    count=0
    maxcount=0
    while len(binary)!=0:
        # print("----------------------------")
        # print(binary)
        # print("inside first while")
        if(binary[-1]=="1"):
            # print("inside first if binary is",binary)
            count=0;
            binary=binary.rstrip(binary[-1])
            # print("after last character deleted, binary is",binary)
            if(len(binary)==0):
                # print("inside second if")
                # print(maxcount)
                continue
            while binary[-1]=="0":
                # print("inside second while")
                count=count+1
                # print("binary before operation is ",binary)
                x=list(binary)
                x.pop()
                binary=str(''.join(x))
                # print("binary is after operation is",binary,"  count is ",count)
        else:
            x=list(binary)
            x.pop()
            binary=str(''.join(x))
        if(count>maxcount):
            # print("inside third if")
            maxcount=count
            count=0
    return(maxcount)

if __name__ == '__main__':
    N=12 
    # print(bin(N))
    print(solution(N))
    
    