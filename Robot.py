from Astar.search import get_path


class Robot(object):

    def __init__(self):
        self.up = "up"
        self.left = "left"
        self.right = "right"
        self.down = "down"
        self.tracing_back = False
        self.tracing_path_index = None
        self.tracing_path = None
        self.tracing_goal_pose = None
        self.tracing_goal_direct = None


    def real_move(self, position, direction, visited, backTracker, matrix):
        visited.add((position['x'], position['y']))

        backTracker.update_still_free(matrix)
        backTracker.push_pose(position, matrix)

        if self.tracing_back == True:
            return self.trace_back_pop_pose( matrix)

        moved, moved_pose, moved_direc = self.move(position, direction, matrix)
        if moved:
            return moved_pose, moved_direc
        else:
            pop = backTracker.pop()
            if pop == False: return "terminate", None

            if position != pop[1]:
                self.tracing_back = True
                self.tracing_path = get_path(visited, start = position, goal = pop[1])
                self.tracing_goal_pose = pop[1]
                self.tracing_goal_direct = pop[0]
                self.tracing_path_index = 0
                return self.trace_back_pop_pose( matrix)

            position = pop[1]
            direction = pop[0]
            moved, moved_pose, moved_direc = self.move(position, direction, matrix)
            if moved:
                return moved_pose, moved_direc
        return None, None



    def trace_back_pop_pose(self, matrix):

        pose = self.tracing_path[self.tracing_path_index][1]
        direct = self.tracing_path[self.tracing_path_index][0]

        moved, moved_pose, moved_direc = self.move(pose, direct, matrix, limit=0.1) # able to step back to covered field
        if moved_pose["x"] == self.tracing_goal_pose["x"] and moved_pose["y"] == self.tracing_goal_pose["y"]:
            self.tracing_back = False
            self.tracing_path = None
            self.tracing_goal_pose = None
            self.tracing_goal_direct = None
            self.tracing_path_index = None
            return moved_pose, self.tracing_goal_direct

        self.tracing_path_index += 1
        return moved_pose, moved_direc

    def move(self, position, direction, matrix, limit=0):
        moved, pose, direc = self.move_forward_with_current_direction(position, direction, matrix, limit)
        return moved, pose, direc


    def move_forward_with_current_direction(self, position, direction, matrix, limit=0):
        if direction == self.down:
            next_x = position['x'] + 1
            next_y = position['y']
            if self.__can_move(next_x, next_y, matrix, limit):
                return True, {"x": next_x, "y": next_y}, direction

        elif direction == self.right:
            next_x = position['x']
            next_y = position['y'] + 1
            if self.__can_move(next_x, next_y, matrix, limit):
                return True, {"x": next_x, "y": next_y}, direction

        elif direction == self.left:
            next_x = position['x']
            next_y = position['y'] - 1
            if self.__can_move(next_x, next_y, matrix, limit):
                return True, {"x": next_x, "y": next_y}, direction

        elif direction == self.up:
            next_x = position['x'] - 1
            next_y = position['y']
            if self.__can_move(next_x, next_y, matrix, limit):
                return True, {"x": next_x, "y": next_y}, direction

        return False, position, direction



    def __can_move(self, next_pos_x, next_pos_y, matrix, limit=0):
        if next_pos_x < 0 or next_pos_y < 0:
            return False
        if next_pos_x >= matrix.shape[0]:
            return False
        if next_pos_y >= matrix.shape[1]:
            return False

        return matrix[next_pos_x][next_pos_y] <= limit