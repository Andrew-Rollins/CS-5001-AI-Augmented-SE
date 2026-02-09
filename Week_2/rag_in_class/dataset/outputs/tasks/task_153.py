def parabola_vertex(a, b, c):
    x_vertex = (-b) / (2 * a)
    y_vertex = ((4 * a * c) - (b * b)) / (4 * a)
    vertex = (x_vertex, y_vertex)
    return vertex
