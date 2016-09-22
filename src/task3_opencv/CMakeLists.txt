cmake_minimum_required(VERSION 2.8.3)
project(task3_opencv)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  apriltags
  image_transport
  roscpp
  sensor_msgs
  geometry_msgs
  tf
  cv_bridge
  message_generation
  std_msgs
  cmake_modules
  nodelet
  wasp_custom_msgs
)

find_package(Eigen REQUIRED)

add_message_files(
  FILES
)

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)

catkin_package(
  INCLUDE_DIRS
  LIBRARIES apriltag_detector
  CATKIN_DEPENDS image_transport roscpp sensor_msgs geometry_msgs tf cv_bridge message_runtime std_msgs nodelet apriltags wasp_custom_msgs
  DEPENDS Eigen
)

###########
## Build ##
###########
include_directories(include  ${catkin_INCLUDE_DIRS})
include_directories(
  ${Eigen_INCLUDE_DIRS}
  ${catkin_INCLUDE_DIRS}
)


add_executable(april_tags src/april_tag_detection.cpp)
target_link_libraries(april_tags ${catkin_LIBRARIES})
add_dependencies(april_tags april_tags)

#############
## Install ##
#############


## Mark cpp header files for installation
install(DIRECTORY include/apriltags_ros
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
)

## Mark other files for installation (e.g. launch and bag files, etc.)
install(FILES nodelet_plugins.xml
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
