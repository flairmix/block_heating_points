from pyautocad import Autocad, APoint


acad = Autocad()
acad.prompt("Hello, Autocad from Python\n")
print (acad.doc.Name)

# p1 = APoint(0, 0)
# p2 = APoint(50, 25)
# for i in range(5):
#     text = acad.model.AddText('Hi %s!' % i, p1, 2.5)
#     acad.model.AddLine(p1, p2)
#     acad.model.AddCircle(p1, 10)
#     p1.y += 10

p3 = APoint(5, 0)
p4 = APoint(10, 0)
p5 = APoint(5, 10)
p6 = APoint(10, 10)

# def draw_valve()

acad.model.AddLine(p3, p4)
acad.model.AddLine(p3, p6)
acad.model.AddLine(p5, p6)
acad.model.AddLine(p4, p5)

p6 = APoint(10, 10, 15)