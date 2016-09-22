cmake_minimum_required(VERSION 2.8.3)
project(wasp_custom_msgs)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
)

add_message_files(
  FILES
  object_loc.msg
)

generate_messages(
  DEPENDENCIES
  geometry_msgs
)

catkin_package(
)
