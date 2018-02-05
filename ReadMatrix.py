import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Robot import Robot
import traceback
from BackTracker import BackTracker

def load_matrix(file):
    matrix = []
    for i in open(file, "r"):
        line = i.split(",")
        l0 = []
        for l in line:
            l0.append(float(l))
        l0 = np.array(l0)
        matrix.append(l0)
    matrix = np.array(matrix)
    return matrix

def draw_arrow(x, y, direc):
    if direc == "down": ax.arrow(x, y, 0, 0.3, head_width=0.2, head_length=0.2, fc='k', ec='k')
    if direc == "up": ax.arrow(x, y, 0, -0.3, head_width=0.2, head_length=0.2, fc='k', ec='k')
    if direc == "right": ax.arrow(x, y, 0.3, 0, head_width=0.2, head_length=0.2, fc='k', ec='k')
    if direc == "left": ax.arrow(x, y, -0.3, 0, head_width=0.2, head_length=0.2, fc='k', ec='k')


def update(i, start_position, start_direction, robot, matrix, visited_nodes, back_tracker):
    global pose0, direc0, move_count
    try:
        if i == 0:
            pose0 = start_position
            direc0 = start_direction
            matrix[pose0["x"], pose0["y"]] = 0.5
            move_count = 1
        else:
            matrix[pose0["x"], pose0["y"]] = 0.1

            moved_pose, moved_direc = robot.real_move(pose0, direc0, visited_nodes, back_tracker, matrix)

            if moved_pose == None and moved_direc == None:
                moved_pose = pose0

            if moved_pose == "terminate":
                print "terminate"
                raise IndexError

            pose0 = moved_pose
            direc0 = moved_direc
            matrix[pose0["x"], pose0["y"]] = 0.5
            move_count += 1
    except IndexError, e:
        # for n in visited_nodes:
        #     print n
        # print traceback.format_exc()

        ani.event_source.stop()
        print matrix
        print "move count:", move_count
        exit()

    draw_arrow(pose0["y"], pose0["x"], direc0)
    matrice.set_array(matrix)



if __name__ == "__main__":
    matrix = load_matrix("matrix_2.txt")

    print "map size:", matrix.shape
    fig, ax = plt.subplots()
    matrice = ax.matshow(matrix)


    start_position = {"x":6, "y":7}
    start_direction = "down"
    robot = Robot()

    visited_nodes = set()
    back_tracker = BackTracker()

    ani = animation.FuncAnimation(fig, update, fargs=[start_position, start_direction, robot, matrix, visited_nodes, back_tracker], frames=10000, interval=100, repeat=False)

    plt.show()