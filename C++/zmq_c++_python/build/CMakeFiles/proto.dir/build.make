# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
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
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python/build"

# Include any dependencies generated for this target.
include CMakeFiles/proto.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/proto.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/proto.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/proto.dir/flags.make

msg.pb.h: ../msg.proto
msg.pb.h: /usr/bin/protoc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir="/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Running cpp protocol buffer compiler on msg.proto"
	/usr/bin/protoc --cpp_out "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python/build" -I "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python" "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python/msg.proto"

msg.pb.cc: msg.pb.h
	@$(CMAKE_COMMAND) -E touch_nocreate msg.pb.cc

CMakeFiles/proto.dir/msg.pb.cc.o: CMakeFiles/proto.dir/flags.make
CMakeFiles/proto.dir/msg.pb.cc.o: msg.pb.cc
CMakeFiles/proto.dir/msg.pb.cc.o: CMakeFiles/proto.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/proto.dir/msg.pb.cc.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/proto.dir/msg.pb.cc.o -MF CMakeFiles/proto.dir/msg.pb.cc.o.d -o CMakeFiles/proto.dir/msg.pb.cc.o -c "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python/build/msg.pb.cc"

CMakeFiles/proto.dir/msg.pb.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/proto.dir/msg.pb.cc.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python/build/msg.pb.cc" > CMakeFiles/proto.dir/msg.pb.cc.i

CMakeFiles/proto.dir/msg.pb.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/proto.dir/msg.pb.cc.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python/build/msg.pb.cc" -o CMakeFiles/proto.dir/msg.pb.cc.s

# Object files for target proto
proto_OBJECTS = \
"CMakeFiles/proto.dir/msg.pb.cc.o"

# External object files for target proto
proto_EXTERNAL_OBJECTS =

libproto.a: CMakeFiles/proto.dir/msg.pb.cc.o
libproto.a: CMakeFiles/proto.dir/build.make
libproto.a: CMakeFiles/proto.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python/build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX static library libproto.a"
	$(CMAKE_COMMAND) -P CMakeFiles/proto.dir/cmake_clean_target.cmake
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/proto.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/proto.dir/build: libproto.a
.PHONY : CMakeFiles/proto.dir/build

CMakeFiles/proto.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/proto.dir/cmake_clean.cmake
.PHONY : CMakeFiles/proto.dir/clean

CMakeFiles/proto.dir/depend: msg.pb.cc
CMakeFiles/proto.dir/depend: msg.pb.h
	cd "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python/build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python" "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python" "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python/build" "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python/build" "/media/ayushman/Seagate Expansion Drive/TiVRA AI/Repo/Project-Setup-Helper/C++/zmq_c++_python/build/CMakeFiles/proto.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/proto.dir/depend
