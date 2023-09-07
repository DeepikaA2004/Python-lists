L = [int(i) for i in input().split()]
def prime(n):
  f=1
  i=2
  while(i<n):
    if n%i==0:
      f+=1
      break
    i+=1
  return(f==1 and n>1)
for i in L:
  if prime(i)==True:
    print(i,end="")
    break