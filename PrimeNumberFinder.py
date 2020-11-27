## Find the prime numbers from 1 - 20

primeCheck = 0
for index in range(2,21):
    # print("index values are",index)
    for num in range(2,index):
        # print("----> num is ",num)
        if index%num == 0:
            primeCheck = 0
            print("Number ",index," not a prime")
            break
        else:
            primeCheck = 1
            #print("This is a prime number ",index)

    if primeCheck == 1:
        print("This is a prime number ",index)