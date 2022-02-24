import csv

def setup():
    
    size(1080, 1080)
    background(255)
    
    center = [540, 540]
    
    #iso_grid = isometric_grid(center, 150, 150, 150)
    
    color_schemes_list = import_csv()
    
    scheme_keys = color_schemes_list.keys()
    
    #super_grid = [[200, 200], [540, 200], [880, 200], [200, 540], [540, 540], [880, 540], [200, 880], [540, 880], [880, 880]]
    
    #super_grid_2 = [[288, 288], [795, 288], [288, 795], [795, 795]]
    
    super_grid_3 = [center]
    
    for element in super_grid_3:
        
        color_scheme_choice = scheme_keys.pop(int(random(0, len(scheme_keys)-1)))
        
        color_scheme = color_schemes_list[str(color_scheme_choice)]
        
        iso_grid = isometric_gridv2(element, 3, 150, color_scheme, 0, 2)
        
    save("iso_cubes_1x1.png")
    
class isometric_cube:
    
    def __init__(self, center, length, width, height, shade):
        
        self.stroke_color = [shade[0] * 0.50, shade[1] * 0.50, shade[2] * 0.50]
        
        self.shade = shade
        
        self.center = center
        
        self.length = length
        
        self.width = width
        
        self. height = height
        
        self.point_7 = [center[0] - (cos(radians(30)) * (length * 0.5)) - (cos(radians(150)) * (width * 0.5)), center[1] + ((sin(radians(30)) * (length * 0.5)) + (sin(radians(150)) * (width * 0.5)) - (height * 0.5))]
        
        self.point_1 = [self.point_7[0] + (cos(radians(30)) * self.length), self.point_7[1] - (sin(radians(30)) * self.length)] 
        
        self.point_3 = [self.point_7[0], self.point_7[1] + self.height]
        
        self.point_5 = [self.point_7[0] + (cos(radians(150)) * self.width), self.point_7[1] - (sin(radians(30)) * self.width)]
        
        self.point_2 = [self.point_1[0], self.point_1[1] + self.height]
        
        self.point_4 = [self.point_5[0], self.point_5[1] + self.height]
        
        self.point_6 = [self.point_5[0] + (self.point_1[0] - self.point_7[0]), self.point_5[1] + (self.point_1[1] - self.point_7[1])]
        
        self.draw_iso()
        
    def draw_iso(self):
        
        strokeWeight(1)
        
        stroke(self.stroke_color[0], self.stroke_color[1], self.stroke_color[2])
        
        fill(self.shade[0], self.shade[1], self.shade[2])
        
        quad(self.point_7[0], self.point_7[1], self.point_5[0], self.point_5[1], self.point_6[0], self.point_6[1], self.point_1[0], self.point_1[1])
        
        fill(self.shade[0]*0.8, self.shade[1]*0.8, self.shade[2]*0.9)
        
        quad(self.point_7[0], self.point_7[1], self.point_1[0], self.point_1[1], self.point_2[0], self.point_2[1], self.point_3[0], self.point_3[1])
        
        fill(self.shade[0]*0.7, self.shade[1]*0.7, self.shade[2]*0.8)
        
        quad(self.point_7[0], self.point_7[1], self.point_3[0], self.point_3[1], self.point_4[0], self.point_4[1], self.point_5[0], self.point_5[1])
        
        stroke(10, 10, 10)
    
        strokeWeight(2)
        
        strokeJoin(ROUND)
        
        line(self.point_1[0], self.point_1[1], self.point_2[0], self.point_2[1])
        
        line(self.point_2[0], self.point_2[1], self.point_3[0], self.point_3[1])
        
        line(self.point_3[0], self.point_3[1], self.point_4[0], self.point_4[1])
        
        line(self.point_4[0], self.point_4[1], self.point_5[0], self.point_5[1])
        
        line(self.point_5[0], self.point_5[1], self.point_6[0], self.point_6[1])
        
        line(self.point_6[0], self.point_6[1], self.point_1[0], self.point_1[1])
        
class isometric_gridv2:
    
    def __init__(self, center, dimension, spacing, color_scheme, current_depth, depth_limit):
        
        self.center = center
        
        self.dimension = dimension
        
        self.spacing = spacing
        
        self.color_scheme = color_scheme
        
        self.current_depth = current_depth
        
        self.depth_limit = depth_limit
        
        self.slices = []
        
        self.build_grid_points()
        
        self.draw_iso_cubes()
        
    def build_grid_points(self):
        
        for i in range(self.dimension - 1, 0, -1):
            
            temp_slice = slice()
            
            center_grid_point =  grid_point(self.center[0], self.center[1] + (i * self.spacing))
            
            for j in range(self.dimension - 1, 0, -1):
                
                temp_right_x_coord = center_grid_point.x + (cos(radians(30)) * (j * self.spacing))
                
                temp_right_y_coord = center_grid_point.y - (sin(radians(30)) * (j * self.spacing))
                
                temp_slice.grid_point_array.append(grid_point(temp_right_x_coord, temp_right_y_coord))
                
                temp_left_x_coord = center_grid_point.x + (cos(radians(150)) * (j * self.spacing))
                
                temp_left_y_coord = center_grid_point.y - (sin(radians(150)) * (j * self.spacing))
                
                temp_slice.grid_point_array.append(grid_point(temp_left_x_coord, temp_left_y_coord))
                
            temp_slice.grid_point_array.append(center_grid_point)
            
            self.slices.append(temp_slice)

        for i in range(self.dimension - 1, 0, -1):
            
            temp_slice = slice()
            
            center_grid_point =  grid_point(self.center[0], self.center[1] - (i * self.spacing))
            
            temp_slice.grid_point_array.append(center_grid_point)
            
            for j in range(1, i + 1, 1):
                                                
                temp_right_x_coord = center_grid_point.x + (cos(radians(330)) * (j * self.spacing))
                
                temp_right_y_coord = center_grid_point.y - (sin(radians(330)) * (j * self.spacing))
                
                temp_slice.grid_point_array.append(grid_point(temp_right_x_coord, temp_right_y_coord))
                
                temp_left_x_coord = center_grid_point.x + (cos(radians(210)) * (j * self.spacing))
                
                temp_left_y_coord = center_grid_point.y - (sin(radians(210)) * (j * self.spacing))
                
                temp_slice.grid_point_array.append(grid_point(temp_left_x_coord, temp_left_y_coord))
            
            self.slices.append(temp_slice)
            
        temp_slice = slice()
        
        temp_grid_point = grid_point(self.center[0], self.center[1])
        
        temp_slice.grid_point_array.append(temp_grid_point)
        
        self.slices.append(temp_slice)
                              
    def draw_grid_points(self):
        
        for slice in self.slices:
            
            for grid_point in slice.grid_point_array:
    
                fill(0)
                circle(grid_point.x, grid_point.y, 5)
                
    def draw_iso_cubes(self):
        
        if self.current_depth >= self.depth_limit:
            
            pass
            
        else:
            
            for i in self.slices:
                
                for j in i.grid_point_array:
            
                    if random(0, 1) >= 0.5:
                
                        length = int(random(self.spacing/3, self.spacing))
                        
                        width = int(random(self.spacing/3, self.spacing))
                        
                        height = int(random(self.spacing/3, self.spacing))
                        
                        len_color_scheme = len(self.color_scheme['colors'])
                        
                        color_choice_num = int(random(1,len_color_scheme+1)) - 1
                        
                        color_choice = self.color_scheme['colors'][color_choice_num]
                        
                        color_choice = [int(x) for x in color_choice]
                        
                        iso = isometric_cube([j.x, j.y], length, width, height, color_choice)
                        
                    else:
                        
                        iso = isometric_gridv2([j.x, j.y], 3, self.spacing/3, self.color_scheme, self.current_depth + 1, self.depth_limit)

class grid_point:
    
    def __init__(self, x, y):
        
        self.x = x
        
        self.y = y
        
        
class slice:
    
    def __init__(self):
        
        self.grid_point_array = []
        
        
    def sort_grid_points(self):
        
        self.grid_point_array.sort(key=attrgetter('y'))

def import_csv():
    
    color_schemes = {}
    
    with open('csv_name.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        for row in csv_reader:
            
            if row[0] not in color_schemes.keys():
                
                color_schemes[row[0]] = {"colors" : [[row[1], row[2], row[3]]]}
                                                   
            else:
                
                color_schemes[row[0]]['colors'].append([row[1], row[2], row[3]])
                
    del color_schemes['Scheme']
                
    return color_schemes
