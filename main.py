def encode (massage):
    encoded_massage = ""
    i = 0
    while ( i <= len(massage)-1):
        count = 1
        char = massage[i]
        j = 1
        while (j< len(message)-1):
            if(massage[j] == massage[j=1]):
                couny +=1
                j += 1
            else:
                break
        encoded_massage = encoded_massage + "*" + char + str (count)
        i=j+1
        return encoded_massage
    encoded_massage = encode("aaasddddssss")
    print(encoded_massage)