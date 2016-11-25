//This file is responsible for creating a listener for the aprilrag
//This listener will convert apriltag positions in the camea frame to the map frame
//We can use this information later for example plotting a marker in the Rviz

#include <ros/ros.h>
#include <tf/transform_listener.h>
#include "geometry_msgs/Pose2D.h"

int id;

int main(int argc, char** argv){
	ros::init(argc, argv, "apriltag_tf_listener");
	ros::NodeHandle nh;
	tf::TransformListener listener;
	//Getting the private id
	if (ros::param::get("~id",id))
 	{
		std::cout<<"Using id  "<<id<<std::endl;
	}
	else
	{
		id=0;
		ROS_INFO("No parameter 'id' found. Using id 0 for the april tag");
	}

	//we are publishing to global namespace /apriltag/global_position/id
	ros::Publisher pub = nh.advertise<geometry_msgs::Pose2D>("/apriltag/global_position/"+std::to_string(id), 10);
	

	ros::Rate rate(10.0);
	while (nh.ok())
	{
		tf::StampedTransform transform;
		try{
			//We are listening to the topic /droneX/apriltag/id
			listener.lookupTransform("/map", "apriltag/"+std::to_string(id) ,ros::Time(0), transform);
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
