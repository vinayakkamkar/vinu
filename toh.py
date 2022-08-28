def TowerOfHanoi(n, source, auxiliary, destination):
    if n==1:
        print("Move disk 1 from source",source,"to destination",destination)
        return
        TowerOfHanoi(n-1, source, auxiliary, destination)
        print("Move disk",n,"from source",source,"to destination",destination)
        TowerOfHanoi(n-1, auxiliary, destination, source)

n=int(input("Enter The Disk Number:"))
TowerOfHanoi(n,'a','b','c')
            
            
