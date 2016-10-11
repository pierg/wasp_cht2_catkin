# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(WARNING "Invoking generate_messages() without having added any message or service file before.
You should either add add_message_files() and/or add_service_files() calls or remove the invocation of generate_messages().")
message(STATUS "task3_opencv: 0 messages, 0 services")

set(MSG_I_FLAGS "-Itask3_opencv:/home/davidis/catkin_ws/src/task3_opencv/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/indigo/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(task3_opencv_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services

### Generating Module File
_generate_module_cpp(task3_opencv
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/task3_opencv
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(task3_opencv_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(task3_opencv_generate_messages task3_opencv_generate_messages_cpp)

# add dependencies to all check dependencies targets

# target for backward compatibility
add_custom_target(task3_opencv_gencpp)
add_dependencies(task3_opencv_gencpp task3_opencv_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS task3_opencv_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services

### Generating Module File
_generate_module_lisp(task3_opencv
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/task3_opencv
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(task3_opencv_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(task3_opencv_generate_messages task3_opencv_generate_messages_lisp)

# add dependencies to all check dependencies targets

# target for backward compatibility
add_custom_target(task3_opencv_genlisp)
add_dependencies(task3_opencv_genlisp task3_opencv_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS task3_opencv_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages

### Generating Services

### Generating Module File
_generate_module_py(task3_opencv
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/task3_opencv
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(task3_opencv_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(task3_opencv_generate_messages task3_opencv_generate_messages_py)

# add dependencies to all check dependencies targets

# target for backward compatibility
add_custom_target(task3_opencv_genpy)
add_dependencies(task3_opencv_genpy task3_opencv_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS task3_opencv_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/task3_opencv)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/task3_opencv
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(task3_opencv_generate_messages_cpp std_msgs_generate_messages_cpp)
add_dependencies(task3_opencv_generate_messages_cpp geometry_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/task3_opencv)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/task3_opencv
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(task3_opencv_generate_messages_lisp std_msgs_generate_messages_lisp)
add_dependencies(task3_opencv_generate_messages_lisp geometry_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/task3_opencv)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/task3_opencv\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/task3_opencv
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(task3_opencv_generate_messages_py std_msgs_generate_messages_py)
add_dependencies(task3_opencv_generate_messages_py geometry_msgs_generate_messages_py)
