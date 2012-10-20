import time
def heapsort(A):
  for start in range((len(A)-2)/2, -1, -1):
    siftdown(A, start, len(A)-1)
 
  for end in range(len(A)-1, 0, -1):
    A[end], A[0] = A[0], A[end]
    siftdown(A, 0, end - 1)
  return A
 
def siftdown(A, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and A[child] < A[child + 1]:
      child += 1
    if A[root] < A[child]:
      A[root], A[child] = A[child], A[root]
      root = child
    else:
      break

C = [13, 1, 4, 23, 44, 8, 14, 70, 42, 45, 30, 99, 44, 2, 10]

inicio = time.time()
heapsort(C)
fin = time.time()
print "el tiempo de ejecución es de ", fin - inicio
print C

raw_input ()


