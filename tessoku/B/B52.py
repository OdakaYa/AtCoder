import queue

N, X = map(int, input().split())
A = list(input())

q = queue.Queue()
q.put(X-1)
A[X-1] = "@"
while not q.empty():
  pos = q.get()
  if pos > 0:
    if A[pos-1] == ".":
      A[pos-1] = "@"
      q.put(pos-1)
  if pos < N-1:
    if A[pos+1] == ".":
      A[pos+1] = "@"
      q.put(pos+1)

print("".join(A))