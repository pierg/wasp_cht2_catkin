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

# Include any dependencies generated for this target.
include task3_opencv/CMakeFiles/tag_filter.dir/depend.make

# Include the progress variables for this target.
include task3_opencv/CMakeFiles/tag_filter.dir/progress.make

# Include the compile flags for this target's objects.
include task3_opencv/CMakeFiles/tag_filter.dir/flags.make

task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o: task3_opencv/CMakeFiles/tag_filter.dir/flags.make
task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o: /home/davidis/catkin_ws/src/task3_opencv/src/tag_filter.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/davidis/catkin_ws/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o"
	cd /home/davidis/catkin_ws/build/task3_opencv && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o -c /home/davidis/catkin_ws/src/task3_opencv/src/tag_filter.cpp

task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/tag_filter.dir/src/tag_filter.cpp.i"
	cd /home/davidis/catkin_ws/build/task3_opencv && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/davidis/catkin_ws/src/task3_opencv/src/tag_filter.cpp > CMakeFiles/tag_filter.dir/src/tag_filter.cpp.i

task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/tag_filter.dir/src/tag_filter.cpp.s"
	cd /home/davidis/catkin_ws/build/task3_opencv && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/davidis/catkin_ws/src/task3_opencv/src/tag_filter.cpp -o CMakeFiles/tag_filter.dir/src/tag_filter.cpp.s

task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o.requires:
.PHONY : task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o.requires

task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o.provides: task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o.requires
	$(MAKE) -f task3_opencv/CMakeFiles/tag_filter.dir/build.make task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o.provides.build
.PHONY : task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o.provides

task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o.provides.build: task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o

# Object files for target tag_filter
tag_filter_OBJECTS = \
"CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o"

# External object files for target tag_filter
tag_filter_EXTERNAL_OBJECTS =

/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: task3_opencv/CMakeFiles/tag_filter.dir/build.make
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /home/davidis/catkin_ws/devel/lib/libapriltags.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libimage_transport.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libtf.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libtf2_ros.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libactionlib.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libmessage_filters.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libtf2.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libcv_bridge.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libnodeletlib.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libbondcpp.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libuuid.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libtinyxml.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libclass_loader.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/libPocoFoundation.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libdl.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libroslib.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libroscpp.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libboost_signals.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/librosconsole.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/librosconsole_log4cxx.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/librosconsole_backend_interface.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/liblog4cxx.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libboost_regex.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libxmlrpcpp.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libroscpp_serialization.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/librostime.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /opt/ros/indigo/lib/libcpp_common.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libboost_system.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libboost_thread.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_videostab.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_superres.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_stitching.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_ocl.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_gpu.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_photo.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_legacy.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_contrib.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_video.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_objdetect.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_ml.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_calib3d.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_features2d.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_flann.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: /usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4.8
/home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter: task3_opencv/CMakeFiles/tag_filter.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable /home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter"
	cd /home/davidis/catkin_ws/build/task3_opencv && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/tag_filter.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
task3_opencv/CMakeFiles/tag_filter.dir/build: /home/davidis/catkin_ws/devel/lib/task3_opencv/tag_filter
.PHONY : task3_opencv/CMakeFiles/tag_filter.dir/build

task3_opencv/CMakeFiles/tag_filter.dir/requires: task3_opencv/CMakeFiles/tag_filter.dir/src/tag_filter.cpp.o.requires
.PHONY : task3_opencv/CMakeFiles/tag_filter.dir/requires

task3_opencv/CMakeFiles/tag_filter.dir/clean:
	cd /home/davidis/catkin_ws/build/task3_opencv && $(CMAKE_COMMAND) -P CMakeFiles/tag_filter.dir/cmake_clean.cmake
.PHONY : task3_opencv/CMakeFiles/tag_filter.dir/clean

task3_opencv/CMakeFiles/tag_filter.dir/depend:
	cd /home/davidis/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/davidis/catkin_ws/src /home/davidis/catkin_ws/src/task3_opencv /home/davidis/catkin_ws/build /home/davidis/catkin_ws/build/task3_opencv /home/davidis/catkin_ws/build/task3_opencv/CMakeFiles/tag_filter.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : task3_opencv/CMakeFiles/tag_filter.dir/depend
