from collections import deque

q = deque([])
q.append(1)
q.append(2)
q.append(3)
q.popleft()

print(q)
if not q:
    print('empty')

