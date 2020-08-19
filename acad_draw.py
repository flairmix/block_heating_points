import acad_python
from acad_python import APoint 

acad = acad_python.Autocad()



def draw_valve(insert_point_x, insert_point_y, scale = 1):

    p1 = APoint(insert_point_x, insert_point_y + (3 * scale))
    p2 = APoint(p1.x, p1.y - (6 * scale))
    p3 = APoint(p1.x + (10 * scale), p1.y)
    p4 = APoint(p3.x, p3.y - (6 * scale))

    acad.model.AddLine(p1, p2)
    acad.model.AddLine(p3, p4)
    acad.model.AddLine(p1, p4)
    acad.model.AddLine(p2, p3)



draw_valve(0, 0)