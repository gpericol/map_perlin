import perlin
import math

def print_matrix(matrix):
    for y in range(len(matrix)):
        for x in range (len(matrix[0])):
            print(matrix[x][y], end='')
        print()

def generate_map(w, h, seed):
    p = perlin.Perlin(seed)
    return [[p.two_octave(x, y) for x in range(w)] for y in range(h)]

def generate_gradient(w, h):
    x_center = w / 2
    y_center = h / 2
    return [[int(math.sqrt(pow(x - x_center, 2) + pow(y - y_center, 2))) for x in range(w)] for y in range(h)]

def apply_gradient(world_map, gradient_map):
    new_map = [[0 for x in range(len(world_map))] for y in range(len(world_map[0]))]
    
    for y in range(len(gradient_map[0])):
        for x in range(len(gradient_map)):
            value = world_map[x][y] - gradient_map[x][y] 
            new_map[x][y] = value if value >= 0 else 0

    return new_map

def scale_matrix(matrix, level):
    min_value = min(map(min, matrix))
    max_value = max(map(max, matrix))
    return [[ int( level * ( (matrix[x][y] - min_value) / ( max_value - min_value ) ))  for x in range(len(matrix))] for y in range(len(matrix[0]))]


if __name__ == "__main__":
    seed = 31337
    height = 200
    width = 200
    
    world_map = generate_map(width, height, seed)
    scaled_world_map = scale_matrix(world_map, 8)
    
    #print_matrix(scaled_world_map)

    gradient_map = generate_gradient(width, height)
    scaled_gradient = scale_matrix(gradient_map, 8)
    #print_matrix(scaled_gradient)


    new_map = apply_gradient(scaled_world_map, scaled_gradient)

    print_matrix(new_map)
