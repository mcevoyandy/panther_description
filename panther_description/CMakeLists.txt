cmake_minimum_required(VERSION 2.8.3)
project(panther_description)


catkin_package(
)

install(DIRECTORY meshes rviz urdf
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
