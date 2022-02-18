class ShapeOfMyHeart():
    def __init__(self):
        pass
    def default_area(self):
        return 0
class Square(ShapeOfMyHeart):
    def __init__(self,length):
        ShapeOfMyHeart.__init__(self)
        self.lenght=length
    def area(self):
        return self.lenght**2
class Rectangle(ShapeOfMyHeart):
    def __init__(self,length,width):
        ShapeOfMyHeart.__init__(self)
        self.lenght=length
        self.width=width
    def rectangle_area(self):
        return (self.lenght)*(self.width)
sizes=input().split()
if len(sizes)==1:
    figure=Square(int(sizes[0]))
    print(figure.area())
    print(figure.default_area())
else:
    figure=Rectangle(int(sizes[0]),int(sizes[1]))
    print(figure.rectangle_area())