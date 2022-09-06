import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():
  pkg_name = 'panther_description'

  pkg_dir = get_package_share_directory(pkg_name)
  rviz_config_file = os.path.join(pkg_dir, 'rviz', 'panther.rviz')
  urdf_file = os.path.join(pkg_dir, 'urdf', 'panther.urdf.xacro')

  # Publish the joint state values for the non-fixed joints in the URDF file.
  joint_state_publisher_cmd = Node(
    package='joint_state_publisher_gui',
    executable='joint_state_publisher_gui',
    name='joint_state_publisher_gui',
  )

  # Subscribe to the joint states of the robot, and publish the 3D pose of each link.
  robot_state_publisher_cmd = Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    parameters=[{
      'robot_description': Command(['xacro ', urdf_file])
    }],
    arguments=[urdf_file]
  )

  # Launch RViz
  rviz_cmd = Node(
    package='rviz2',
    executable='rviz2',
    name='rviz2',
    output='screen',
    arguments=['-d', rviz_config_file])

  return LaunchDescription([
    rviz_cmd,
    joint_state_publisher_cmd,
    robot_state_publisher_cmd
  ])
