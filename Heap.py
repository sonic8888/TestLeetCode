from heapq import heappush, heappop, heapify


def find_min_cost(ropes):
    print(ropes)
    heapify(ropes)
    cost = 0
    while len(ropes) > 1:
        summ = heappop(ropes) + heappop(ropes)
        heappush(ropes, summ)
        print(ropes)
        cost += summ
    print(cost)
