cmake_minimum_required(VERSION 2.8)
project(drone)

find_package(catkin REQUIRED)
catkin_package()

#catkin_python_setup()


install(PROGRAMS src/pid2plant.py
		 src/plant2pid.py
		 src/uiscript.py
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)