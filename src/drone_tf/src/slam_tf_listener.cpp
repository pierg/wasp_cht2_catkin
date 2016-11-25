// This file is responsible for creating a listener for the position of the drone
// in the global coordinates system and publishing


#include <ros/ros.h>
#include <tf/transform_listener.h>
#include "geometry_msgs/Pose2D.h"

int id;

int main(int argc, char** argv) {
	ros::init(argc, argv, "slam_tf_listener");
	ros::NodeHandle nh;
	tf::TransformListener listener;
	//Getting the private id

	//we are publishing to global namespace /apriltag/global_position/id
	ros::Publisher pub = nh.advertise<geometry_msgs::Pose2D>("global_position", 10);
	
	ros::Rate rate(10.0); // 10Hz publishing rate
	while (nh.ok())
	{
		tf::StampedTransform transform;
		try{
			//We are listening to the topic /droneX/apriltag/id
			listener.lookupTransform("/SLAM_TF/drone_global_position", "/map", ros::Time(0), transform);
			geometry_msgs::Pose2D position;
			position.x = transform.getOrigin().x();
			position.y = transform.getOrigin().y();
			position.theta = tf::getYaw(transform.getRotation());
			pub.publish(position);
		}
		catch (tf::TransformException ex){
			//Tired of seeing this useless error of conversion			
			//ROS_ERROR("%s",ex.what());
			ros::Duration(1.0).sleep();
		}
		//Wait for next iteration
		rate.sleep();
	}
	return 0;
};
