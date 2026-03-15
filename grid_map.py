import irsim
import numpy as np

env = irsim.make(save_ani=False, full=False)

for _i in range(1000):

    robot = env.robot

    lidar = robot.lidar
    scan = lidar.get_scan()

    ranges = np.array(scan["ranges"])

    n = len(ranges)

    # detect front sector dynamically
    center = n // 2
    front = ranges[center-5:center+5]

    min_dist = np.min(front)

    safe_distance = 6.0
    slow_distance = 9.0
    print("Front distance:", min_dist)

    if min_dist < safe_distance:
        # obstacle detected → rotate
        action = [[0.5, 1.0]]
    elif min_dist < slow_distance:
        action = [[0.5, 0.0]]
    else:
        # safe → move forward slowly
        action = [[7.0, 0.0]]

    env.step(action)
    env.render()

    if env.done():
        break

env.end(5)