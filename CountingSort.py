import time
def countingsort(A, c):

	B = [0 for el in A]
	D = [0 for el in xrange(0, c+1)]
 
	for i in xrange(0, c + 1):
		D[i] = 0
 
	for j in xrange(0, len(A)):
		D[A[j]] += 1
 
	for i in xrange(1, c + 1):
		D[i] += D[i - 1]
 
	for j in xrange(len(A)-1, 0 - 1, -1):
		aux = A[j]
		aux2= D[aux] -1
		B[aux2] = aux
		D[aux] -= 1
	return B
inicio = time.time()
countingsort([6,0,2,0,1,3,4,6,1,3,2], 6)
fin = time.time()
print "el tiempo de ejecución es de ", fin - inicio 
print countingsort([6,0,2,0,1,3,4,6,1,3,2], 6)

raw_input()
