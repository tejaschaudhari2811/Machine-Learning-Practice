class Polygon:

    def render():
        print("rendering polygon")
    
class Square(Polygon):

    def render():
        print("rendering Square")

class Circle(Polygon):
    def render():
        print("Rendering circle")

Polygon.render()
Square.render()
Circle.render()