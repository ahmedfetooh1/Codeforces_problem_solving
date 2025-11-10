m , n = map(int ,input().split())
print(f'{int((m*n)/2)}' if (m*n)%2 ==0 else f'{int(((m*n)-1)/2)}')