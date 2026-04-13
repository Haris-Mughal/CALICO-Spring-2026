import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A = input().strip()
    B = input().strip()
    
    jwab = list('#' * len(A))
    j = 0
    for i in range(len(A)):
        if j < len(B) and A[i] == B[j]:
            jwab[i] = A[i]
            j += 1
    print(''.join(jwab))