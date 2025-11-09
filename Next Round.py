n, k = map(int, input().split())
scores = list(map(int, input().split()))
kth_score = scores[k - 1]
count = sum(1 for score in scores if score >= kth_score and score > 0)
print(count)