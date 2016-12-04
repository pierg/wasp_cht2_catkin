//Connecting SLAM with the global map

#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include "wasp_custom_msgs/object_loc.h"
#include "std_msgs/Bool.h"
#include <string>


int main(int argc, char** argv){
	ros::init(argc, argv, "slam_tf_broadcaster");
	ros::NodeHandle nh;
	double apriltag_initial_x;
	double apriltag_initial_y;
	double apriltag_initial_theta;

	if (ros::param::get("~apriltag_initial_x",apriltag_initial_x))
 	{
		std::cout<<"X initial position  "<<apriltag_initial_x<<std::endl;
	}
	else
	{
		apriltag_initial_x=0;
		ROS_INFO("No parameter 'apriltag_initial_x' found. Using apriltag_initial_x 0 for the apriltag_initial_x");
	}
	if (ros::param::get("~apriltag_initial_y",apriltag_initial_y))
 	{
		std::cout<<"Y initial position  "<<apriltag_initial_y<<std::endl;
	}
	else
	{
		apriltag_initial_y=0;
		ROS_INFO("No parameter 'apriltag_initial_y' found. Using apriltag_initial_y 0 for the apriltag_initial_y");
	}
	if (ros::param::get("~apriltag_initial_theta",apriltag_initial_theta))
 	{
		std::cout<<"theta initial position  "<<apriltag_initial_theta<<std::endl;
	}
	else
	{
		apriltag_initial_theta=0;
		ROS_INFO("No parameter 'apriltag_initial_theta' found. Using apriltag_initial_theta 0 for the apriltag_initial_theta");
	}
	ros::Rate rate(10.0);
  	while (nh.ok())
	{
		static tf::TransformBroadcaster br;
			tf::Transform transform;
			//Setting the position of the apriltag related to the drone
			transform.setOrigin( tf::Vector3(apriltag_initial_x, apriltag_initial_y, 0));
			//We dont care about the rotation of the tag	
			tf::Quaternion qt = tf::Quaternion();
			qt.setRPY(0,0,apriltag_initial_theta);//pure experimentation with the angles published by the april tag
			transform.setRotation(qt);

			br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "/map", "slam/map"));
	
		rate.sleep();
	}
};
