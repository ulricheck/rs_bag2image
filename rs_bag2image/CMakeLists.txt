cmake_minimum_required( VERSION 3.6 )

# Require C++17 (or later)
set( CMAKE_CXX_STANDARD 17 )
set( CMAKE_CXX_STANDARD_REQUIRED ON )
set( CMAKE_CXX_EXTENSIONS OFF )

# Create Project
project( rs_bag2image )

if(EXISTS ${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
  include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
  conan_basic_setup(TARGETS)
else()
  message(WARNING "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
endif()


add_executable( rs_bag2image version.h realsense.h realsense.cpp main.cpp )

# Set StartUp Project
set_property( DIRECTORY PROPERTY VS_STARTUP_PROJECT "rs_bag2image" )

# Additional Dependencies
target_link_libraries( rs_bag2image CONAN_PKG::librealsense )
target_link_libraries( rs_bag2image CONAN_PKG::opencv )
if( NOT WIN32 )
  target_link_libraries( rs_bag2image stdc++fs )
endif()
