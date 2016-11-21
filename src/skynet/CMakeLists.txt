cmake_minimum_required(VERSION 2.8.3)
project(skynet)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  visualization_msgs
  actionlib_msgs
  move_base_msgs
  std_msgs
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

###########
## Build ##
###########
include_directories(include  ${catkin_INCLUDE_DIRS})
include_directories(
  ${Eigen_INCLUDE_DIRS}
  ${catkin_INCLUDE_DIRS}
)
