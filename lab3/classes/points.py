class Points():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        return self.x ,self.y
    def move(self,new_x,new_y):
        self.x+=new_x
        self.y+=new_y
    def dist(self):
        return abs(self.x-self.y)
coordinates=input().split()
x,y=int(coordinates[0]),int(coordinates[1])
points=Points(x,y)
while str!="exit":
    str=input()
    if str=="show":
        print(points.show())
    elif str=="move":
        new_coordinates=input().split()
        new_x,new_y=int(new_coordinates[0]),int(new_coordinates[1])
        new_points=points.move(new_x,new_y)
    elif str=="dist":
        print(points.dist())