import time

def read_matrix_from_file(file_path):          #ф-ия для прочтения матрицы из файла
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(x) for x in line.strip().split()]
            matrix.append(row)
    return matrix

def get_degree(matrix, vertex):
    degree = 0
    for edge in matrix[vertex]:
        if edge == 1:
            degree += 1
    return degree

def get_vertices_with_odd_degree(matrix):
    vertices = []
    degrees = []
    num_vertices = len(matrix)
    for vertex in range(num_vertices):
        degree = get_degree(matrix, vertex)
        if degree % 2 != 0:
            vertices.append(vertex + 1)
            degrees.append(degree)
    return vertices, degrees

def counting_sort(vertices, degrees):
    max_degree = max(degrees) + 1
    count = [0] * max_degree
    sorted_vertices = [0] * len(vertices)

    for degree in degrees:
        count[degree] += 1

    for i in range(1, max_degree):
        count[i] += count[i-1]

    for j in reversed(range(len(vertices))):
        vertex = vertices[j]
        degree = degrees[j]
        sorted_vertices[count[degree]-1] = vertex
        count[degree] -= 1

    return sorted_vertices

# Ввод пути к файлу с матрицей инцидентности
file_path = input("Введите путь к файлу с матрицей инцидентности: ")
start_time = time.time()
matrix = read_matrix_from_file(file_path)
odd_degree_vertices, degrees = get_vertices_with_odd_degree(matrix)
sorted_vertices = counting_sort(odd_degree_vertices, degrees)
end_time = time.time()

print("Вершины с нечётными степенями по убыванию:")
print(*reversed(sorted_vertices))

execution_time = end_time - start_time
print("Время работы сортировки: {:.8f} секунд".format(execution_time))