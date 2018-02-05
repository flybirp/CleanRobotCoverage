from Robot import Robot

class BackTracker:
    def __init__(self):
        self.stack = []


    def push_pose(self, pose, matrix):
        l = self.get_free_adjacent(pose, matrix)
        for ll in l:
            self.stack.append(ll)


    def update_still_free(self, matrix):
        remove_list = []

        for i in self.stack:
            index = i[1]
            direct = i[0]
            if direct == "down" and self._can_move_(index["x"] + 1, index["y"], matrix):
                pass
            elif direct == "right" and self._can_move_(index["x"], index["y"] + 1, matrix):
                pass
            elif direct == "up" and self._can_move_(index["x"] -1, index["y"], matrix):
                pass
            elif direct == "left" and self._can_move_(index["x"], index["y"] - 1, matrix):
                pass
            else:
                not_free = (direct, index)
                remove_list.append(not_free)
        for r in remove_list:
            self.stack.remove(r)

    def remove_duplicate(self):
        l2 = []
        [l2.append(i) for i in self.stack if not i in l2]
        self.stack = l2

    def get_free_adjacent(self, index, matrix):
        l = []
        if self._can_move_(index["x"] + 1, index["y"], matrix):
            free = ("down", index)
            l.append(free)
        if self._can_move_(index["x"], index["y"] + 1, matrix):
            free = ("right", index)
            l.append(free)
        if self._can_move_(index["x"] -1, index["y"], matrix):
            free = ("up", index)
            l.append(free)
        if self._can_move_(index["x"], index["y"] - 1, matrix):
            free = ("left", index)
            l.append(free)
        return l

    def _can_move_(self, next_pos_x, next_pos_y, matrix):
        if next_pos_x < 0 or next_pos_y < 0:
            return False
        if next_pos_x >= matrix.shape[0]:
            return False
        if next_pos_y >= matrix.shape[1]:
            return False
        return matrix[next_pos_x][next_pos_y] == 0


    def pop(self):
        if len(self.stack) == 0: return False
        return self.stack[len(self.stack)-1]