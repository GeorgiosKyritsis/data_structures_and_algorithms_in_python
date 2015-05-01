__author__ = 'inamoto21'

import heapq

heap = []

heapq.heappush(heap, (1, 'one'))
heapq.heappush(heap, (0, 'zero'))
heapq.heappush(heap, (-1, 'minus-one'))
heapq.heappush(heap, (10, 'ten'))
heapq.heappush(heap, (7, 'even'))
print('------Print the elements of heap---------')
for j in heap:
    print(j)

heap2 = [(1, 'one'), (2, 'two'), (0, 'zero'), (10, 'ten'), (8, 'eight'), (7, 'seven')]
heapq.heapify(heap2)
print('------Print the elements of heap2---------')
for j in heap2:
    print(j)
print('------Popping element from heap2---------')
heapq.heappop(heap2)
for j in heap2:
    print(j)
print('------Push-popping element from heap2 and pushing (9, nine)---------')
heapq.heappushpop(heap2, (9, 'nine'))
for j in heap2:
    print(j)