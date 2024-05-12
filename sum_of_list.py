def simpleArraySum(ar):
    sum_ = 0
    for i in ar:
        sum_ += i
    return sum_
        

if __name__ == '__main__':
    ar = [1,2,3,4,5,6,7,8,9,0]
    result = simpleArraySum(ar)
    print("total_sum",result)

    