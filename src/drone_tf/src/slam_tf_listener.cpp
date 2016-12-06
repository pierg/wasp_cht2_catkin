// This file is responsible for creating a listener for the position of the drone
// in the global coordinates system and publishing


#include <ros/ros.h>
#include <tf/transform_listener.h>
#include "geometry_msgs/Pose2D.h"
#include "nav_msgs/Odometry.h"


int id;

int main(int argc, char** argv) {
	ros::init(argc, argv, "slam_tf_listener");
	ros::NodeHandle nh;
	tf::TransformListener listener;
	//Getting the private id

	//we are publishing to global namespace /apriltag/global_position/id
	ros::Publisher pub = nh.advertise<geometry_msgs::Pose2D>("global_position", 10);
	ros::Publisher pub2 = nh.advertise<nav_msgs::Odometry>("global/pos", 10);
	
	ros::Rate rate(10.0); // 10Hz publishing rate
	while (nh.ok())
	{
		tf::StampedTransform transform;
		try{
			//We are listening to the topic /droneX/apriltag/id
			listener.lookupTransform("/map", "drone", ros::Time(0), transform);
			
			//For the rviz debuger			
			geometry_msgs::Pose2D position;
			position.x = transform.getOrigin().x();
			position.y = transform.getOrigin().y();
			position.theta = tf::getYaw(transform.getRotation());
			pub.publish(position);

			//for the file drone.py
			nav_msgs::Odometry globpos;
			globpos.pose.pose.position.x = transform.getOrigin().x();
			globpos.pose.pose.position.y = transform.getOrigin().y();
			globpos.pose.pose.position.z = transform.getOrigin().z();
			tf::Quaternion qt = tf::Quaternion();
			qt.setRPY(0,0,tf::getYaw(transform.getRotation()));
			globpos.pose.pose.orientation.x = qt.x();
			globpos.pose.pose.orientation.y = qt.y();
			globpos.pose.pose.orientation.z = qt.z();
			globpos.pose.pose.orientation.w = qt.w();
			pub2.publish(globpos);

			



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
