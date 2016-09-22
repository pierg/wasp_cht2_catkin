cmake_minimum_required(VERSION 2.8.3)
project(task3_pcl)

find_package(catkin REQUIRED COMPONENTS
  pcl_msgs
  roscpp
  sensor_msgs
  std_msgs
  geometry_msgs
  pcl_ros
  tf
  wasp_custom_msgs
)


catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(PCL_subsampler src/PCL_subsampler.cpp)
target_link_libraries(PCL_subsampler ${catkin_LIBRARIES})

add_executable(PCL_transform src/PCL_transform.cpp)
target_link_libraries(PCL_transform ${catkin_LIBRARIES})

add_executable(PCL_ground_removal src/PCL_ground_removal.cpp)
target_link_libraries(PCL_ground_removal ${catkin_LIBRARIES})

add_executable(PCL_object_clustering src/PCL_object_clustering.cpp)
add_dependencies(PCL_object_clustering wasp_custom_msgs)
target_link_libraries(PCL_object_clustering ${catkin_LIBRARIES})
