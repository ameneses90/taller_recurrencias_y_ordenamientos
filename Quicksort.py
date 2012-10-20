import time
def particion(A,p,q):
	x = A[p]
	i = p
	for j in range (p+1,q):
		if A[j] <= x:
			i = i + 1
			aux = A[i]
			A[i] = A[j]
			A[j] = aux
	aux = A[p]
	A[p] = A[i]
	A[i] = aux
	return i

def quicksort(A,p,r):
	if p < r:
		q = particion(A,p,r)
		quicksort(A,p,q-1)
		quicksort(A,q+1,r)


a = []
for b in range (1000,0,-1):
        a.append (b)

inicio = time.time()
quicksort(a,0,1000)
fin = time.time()
print "el tiempo de ejecución es de ", fin - inicio
raw_input ()
