cmake_minimum_required(VERSION 3.22)

project(video_proc LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)
#头文件搜索路径，让代码可以 #include "transform.hpp"
include_directories(${PROJECT_SOURCE_DIR}/include)
include_directories("/usr/include/eigen3")

#所有cpp源码的相对路径！两个文件都要写上
add_executable(video_process
    src/main.cpp
    src/transform.cpp
)

target_link_libraries(video_process PRIVATE ${OpenCV_LIBS})
