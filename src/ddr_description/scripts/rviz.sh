#!/bin/bash

source /opt/ros/humble/setup.bash
source ~/robot_description_ws/install/setup.bash

rviz2 -d ~/robot_description_ws/src/ddr_description/rviz/ddr_robot_description.rviz