cmake_minimum_required(VERSION 2.8.3)
project(drone_tf)

if(CMAKE_COMPILER_IS_GNUCXX) 
	add_definitions(-std=gnu++0x) 
endif()

find_package(catkin REQUIRED COMPONENTS
  apriltags
  image_transport
  roscpp
  rospy
  sensor_msgs
  geometry_msgs
  visualization_msgs
  tf
  cv_bridge
  message_generation
  std_msgs
  nav_msgs
  cmake_modules
  nodelet
  move_base_msgs
  actionlib
  OpenCV
)

find_package(Eigen REQUIRED)

#add_service_files(DIRECTORY srv
#  FILES
#)

#add_message_files(DIRECTORY msg
#  FILES
#)

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
  move_base_msgs
)

catkin_package(
  INCLUDE_DIRS
  LIBRARIES apriltag_detector 
  CATKIN_DEPENDS image_transport roscpp sensor_msgs geometry_msgs tf cv_bridge message_runtime std_msgs nav_msgs nodelet apriltags using_markers visualization_msgs move_base_msgs actionlib 
  DEPENDS Eigen OpenCV
)

###########
## Build ##
###########
include_directories(include  ${catkin_INCLUDE_DIRS})
include_directories(
  ${Eigen_INCLUDE_DIRS}
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)


#install(PROGRAMS pynodes/voice_feedback.py
#  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

add_executable(apriltag_tf_broadcaster src/apriltag_tf_broadcaster.cpp)
target_link_libraries(apriltag_tf_broadcaster ${catkin_LIBRARIES})
add_dependencies(apriltag_tf_broadcaster apriltag_tf_broadcaster ${${PROJECT_NAME}_EXPORTED_TARGETS})

add_executable(apriltag_tf_listener src/apriltag_tf_listener.cpp)
target_link_libraries(apriltag_tf_listener ${catkin_LIBRARIES})
add_dependencies(apriltag_tf_listener apriltag_tf_listener ${${PROJECT_NAME}_EXPORTED_TARGETS})

add_executable(slam_tf_broadcaster src/slam_tf_broadcaster.cpp)
target_link_libraries(slam_tf_broadcaster ${catkin_LIBRARIES})
add_dependencies(slam_tf_broadcaster slam_tf_broadcaster ${${PROJECT_NAME}_EXPORTED_TARGETS})

add_executable(slam_tf_listener src/slam_tf_listener.cpp)
target_link_libraries(slam_tf_listener ${catkin_LIBRARIES})
add_dependencies(slam_tf_listener slam_tf_listener ${${PROJECT_NAME}_EXPORTED_TARGETS})

add_executable(drone2slam_tf_broadcaster src/drone2slam_tf_broadcaster.cpp)
target_link_libraries(drone2slam_tf_broadcaster ${catkin_LIBRARIES})
add_dependencies(drone2slam_tf_broadcaster drone2slam_tf_broadcaster ${${PROJECT_NAME}_EXPORTED_TARGETS})

add_executable(drone_rviz_markers src/drone_rviz_markers.cpp)
target_link_libraries(drone_rviz_markers ${catkin_LIBRARIES})
add_dependencies(drone_rviz_markers drone_rviz_markers ${${PROJECT_NAME}_EXPORTED_TARGETS})


