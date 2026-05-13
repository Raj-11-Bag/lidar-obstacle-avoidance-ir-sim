# LiDAR Based Reactive Obstacle Avoidance (IR-Sim)

This project demonstrates a simple LiDAR-based obstacle avoidance
algorithm implemented in the IR-SIM robotics simulator.

The robot dynamically adjusts its speed and steering based on the
distance measurements from a 2D LiDAR sensor.

## Demo

[![Watch the video](https://img.youtube.com/vi/HA-RiKA5YAU/0.jpg)](https://youtu.be/HA-RiKA5YAU)


## Features

• LiDAR based obstacle detection  
• Multi-speed navigation behavior  
• Reactive steering to avoid collisions  
• Configurable simulation environment

## Architecture

Simulation Environment → LiDAR Sensor → Obstacle Detection → Motion Control

           +------------------+
           |   LiDAR Sensor   |
           +------------------+
                    |
                    v
          +--------------------+
          | Distance Analysis  |
          |  (Front Sector)    |
          +--------------------+
                    |
                    v
         +----------------------+
         | Decision Logic       |
         |----------------------|
         | < 6m   -> Turn       |
         | 6-9m   -> Slow       |
         | > 9m   -> Fast       |
         +----------------------+
                    |
                    v
            +--------------+
            | Robot Motion |
            +--------------+

## Behavior Logic

If obstacle distance < 6m
   → turn to avoid collision

If obstacle distance between 6m and 9m
   → slow down

If obstacle distance > 9m
   → move forward at high speed


## Example Output

Front distance: 6.92
Front distance: 6.32
Front distance: 5.72
Front distance: 5.72
Robot turning to avoid obstacle


## Installation

1. Install IR-Sim
2. Run the script

python grid_map_custom.py

## Acknowledgement

This project uses the IR-Sim robotics simulator developed by
Hanrui Hua.

Original repository:
https://github.com/hanruihua/ir-sim
