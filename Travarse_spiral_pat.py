matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
n=len(matrix)
n=len(matrix[0])
top,left=0,0
bottom,right=n-1,n-1

while top<=bottom and left<=right:
    for i in range(left,right+1):
        print(matrix[top][i],end=' ')
    top+=1
    for i in range(top,bottom+1):
        print(matrix[i][right],end=' ')
    right-=1
    for i in range(right,left-1,-1):
        print(matrix[bottom][i],end=' ')
    bottom-=1
    for i in range(bottom,top-1,-1):
        print(matrix[i][left],end=' ')
    left+1
