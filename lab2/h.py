def closest_point(x1,y1,x2,y2):
    return (((x2-x1)**2)+((y2-y1)**2))**0.5
x1,y1=map(int, input().split())
size=int(input())
coordinates=[]
for i in range(size):
    x2,y2=map(int,input().split())
    coordinates.append((closest_point(x1,y1,x2,y2),x2,y2))
coordinates=sorted(coordinates)
for i in coordinates:
    print(i[1],i[2])