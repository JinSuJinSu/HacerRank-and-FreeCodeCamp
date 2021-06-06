# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

set_A = list(map(float, input().split()))
set_B = list(map(float, input().split()))


A_rank_list = sorted(set_A)
B_rank_list = sorted(set_B)


total_distance = 0

for i in range(len(set_A)):
    rank_A = A_rank_list.index(set_A[i])+1
    rank_B = B_rank_list.index(set_B[i])+1
    
    distance = rank_A-rank_B
    
    total_distance+=distance**2
    
result = 1-(6*total_distance)/(N*(N**2-1))

print(result)
