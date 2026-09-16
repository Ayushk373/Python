import heapq

h = []

heapq.heappush(h, 30)
heapq.heappush(h, 10)
heapq.heappush(h, 20)
heapq.heappush(h, 5)

print(h)

print("Smallest:", heapq.heappop(h))
print("Next:", heapq.heappop(h))
