# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, 
# determine how many pairs of socks with matching colors there are.
# input example: , 
# n = 9 ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# output: 3 for 3 pairs found


def sockMerchant(n, ar):
      ar.sort()
      print(ar)
      pairs = 0
      count = 0
      temp = []
      for i in range(n - 1):
            if ar[i] == ar[i+1]:
                  count+=1
  
            else:
                  temp.append(count + 1)
                  count = 0
      temp.append(count+1)
      for i in temp:
            pairs += i // 2

      return pairs


if __name__ == '__main__':
      ar = [1,1, 1, 1]
      n = 4
      print(sockMerchant(n, ar))
