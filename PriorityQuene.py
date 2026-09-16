import heapq

pq = []

heapq.heappush(pq, (2, "Normal"))
heapq.heappush(pq, (1, "High"))
heapq.heappush(pq, (3, "Low"))

while pq:
    priority, item = heapq.heappop(pq)
    print(priority, item)
