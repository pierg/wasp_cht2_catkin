# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/davidis/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/davidis/catkin_ws/build

# Utility rule file for wasp_custom_msgs_generate_messages_cpp.

# Include the progress variables for this target.
include wasp_custom_msgs/CMakeFiles/wasp_custom_msgs_generate_messages_cpp.dir/progress.make

wasp_custom_msgs/CMakeFiles/wasp_custom_msgs_generate_messages_cpp: /home/davidis/catkin_ws/devel/include/wasp_custom_msgs/image_point.h
wasp_custom_msgs/CMakeFiles/wasp_custom_msgs_generate_messages_cpp: /home/davidis/catkin_ws/devel/include/wasp_custom_msgs/object_loc.h

/home/davidis/catkin_ws/devel/include/wasp_custom_msgs/image_point.h: /opt/ros/indigo/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py
/home/davidis/catkin_ws/devel/include/wasp_custom_msgs/image_point.h: /home/davidis/catkin_ws/src/wasp_custom_msgs/msg/image_point.msg
/home/davidis/catkin_ws/devel/include/wasp_custom_msgs/image_point.h: /opt/ros/indigo/share/std_msgs/cmake/../msg/Int64.msg
/home/davidis/catkin_ws/devel/include/wasp_custom_msgs/image_point.h: /opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg
/home/davidis/catkin_ws/devel/include/wasp_custom_msgs/image_point.h: /opt/ros/indigo/share/gencpp/cmake/../msg.h.template
	$(CMAKE_COMMAND) -E cmake_progress_report /home/davidis/catkin_ws/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating C++ code from wasp_custom_msgs/image_point.msg"
	cd /home/davidis/catkin_ws/build/wasp_custom_msgs && ../catkin_generated/env_cached.sh /usr/bin/python /opt/ros/indigo/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/davidis/catkin_ws/src/wasp_custom_msgs/msg/image_point.msg -Iwasp_custom_msgs:/home/davidis/catkin_ws/src/wasp_custom_msgs/msg -Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg -p wasp_custom_msgs -o /home/davidis/catkin_ws/devel/include/wasp_custom_msgs -e /opt/ros/indigo/share/gencpp/cmake/..

/home/davidis/catkin_ws/devel/include/wasp_custom_msgs/object_loc.h: /opt/ros/indigo/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py
/home/davidis/catkin_ws/devel/include/wasp_custom_msgs/object_loc.h: /home/davidis/catkin_ws/src/wasp_custom_msgs/msg/object_loc.msg
/home/davidis/catkin_ws/devel/include/wasp_custom_msgs/object_loc.h: /opt/ros/indigo/share/geometry_msgs/cmake/../msg/Point.msg
/home/davidis/catkin_ws/devel/include/wasp_custom_msgs/object_loc.h: /opt/ros/indigo/share/gencpp/cmake/../msg.h.template
	$(CMAKE_COMMAND) -E cmake_progress_report /home/davidis/catkin_ws/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating C++ code from wasp_custom_msgs/object_loc.msg"
	cd /home/davidis/catkin_ws/build/wasp_custom_msgs && ../catkin_generated/env_cached.sh /usr/bin/python /opt/ros/indigo/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/davidis/catkin_ws/src/wasp_custom_msgs/msg/object_loc.msg -Iwasp_custom_msgs:/home/davidis/catkin_ws/src/wasp_custom_msgs/msg -Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg -Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg -p wasp_custom_msgs -o /home/davidis/catkin_ws/devel/include/wasp_custom_msgs -e /opt/ros/indigo/share/gencpp/cmake/..

wasp_custom_msgs_generate_messages_cpp: wasp_custom_msgs/CMakeFiles/wasp_custom_msgs_generate_messages_cpp
wasp_custom_msgs_generate_messages_cpp: /home/davidis/catkin_ws/devel/include/wasp_custom_msgs/image_point.h
wasp_custom_msgs_generate_messages_cpp: /home/davidis/catkin_ws/devel/include/wasp_custom_msgs/object_loc.h
wasp_custom_msgs_generate_messages_cpp: wasp_custom_msgs/CMakeFiles/wasp_custom_msgs_generate_messages_cpp.dir/build.make
.PHONY : wasp_custom_msgs_generate_messages_cpp

# Rule to build all files generated by this target.
wasp_custom_msgs/CMakeFiles/wasp_custom_msgs_generate_messages_cpp.dir/build: wasp_custom_msgs_generate_messages_cpp
.PHONY : wasp_custom_msgs/CMakeFiles/wasp_custom_msgs_generate_messages_cpp.dir/build

wasp_custom_msgs/CMakeFiles/wasp_custom_msgs_generate_messages_cpp.dir/clean:
	cd /home/davidis/catkin_ws/build/wasp_custom_msgs && $(CMAKE_COMMAND) -P CMakeFiles/wasp_custom_msgs_generate_messages_cpp.dir/cmake_clean.cmake
.PHONY : wasp_custom_msgs/CMakeFiles/wasp_custom_msgs_generate_messages_cpp.dir/clean

wasp_custom_msgs/CMakeFiles/wasp_custom_msgs_generate_messages_cpp.dir/depend:
	cd /home/davidis/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/davidis/catkin_ws/src /home/davidis/catkin_ws/src/wasp_custom_msgs /home/davidis/catkin_ws/build /home/davidis/catkin_ws/build/wasp_custom_msgs /home/davidis/catkin_ws/build/wasp_custom_msgs/CMakeFiles/wasp_custom_msgs_generate_messages_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : wasp_custom_msgs/CMakeFiles/wasp_custom_msgs_generate_messages_cpp.dir/depend

