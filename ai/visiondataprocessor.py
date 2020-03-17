class VisionDataProcessor:
    def __init__(self):

        self.size_x = 320 # left and right
        self.size_y = 160 # up and down

        self.py_to_angle = 4        # pixel to angle
        self.px_to_angle = 2        # pixel to angle

        self.angle_to_turn = 20 # turn once - 20 degree


        self.ball_size = 500
        self.ball_dis_step = 20    # need to check



    def angle_to_turn_times(self, angle):
        return int(angle/ self.angle_to_turn)


    def get_difference_pxpy(self, input_coord):
        x_difference = input_coord[0] - self.size_x/2.0
        y_difference = input_coord[1] - self.size_y/2.0
        return [x_difference, y_difference]

    def get_ball_distance(self, area):
        ball_rate = area/self.ball_size
        dis = ball_rate * self.ball_dis_step

        return dis
