//This node is responsible for converting the apriltag location in respect to the turtlebot.
// This way we can set up a listener that looks at the apriltag tf and put it into the world coordinate system

#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include "wasp_custom_msgs/object_loc.h"
#include "std_msgs/Bool.h"
#include <string>


int id;
bool canScan = false;


//This callback function is responsible for getting the camera-apriltag distance and add a mpde tp tje 
void transform_callback(const wasp_custom_msgs::object_loc &msg)
{
	if(canScan)
	{
		if(id == msg.ID)
		{
			std::cout<<"Receiving the correct id"<<std::endl;
			static tf::TransformBroadcaster br;
			tf::Transform transform;
			//Setting the position of the apriltag related to the drone
			transform.setOrigin( tf::Vector3(msg.point.x, msg.point.y, msg.point.z) );
			//We dont care about the rotation of the tag	
			tf::Quaternion qt = tf::Quaternion();
			qt.setRPY(0,0,0);//pure experimentation with the angles published by the april tag
			transform.setRotation(qt);

			br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "ardrone_base_frontcam", "apriltag/"+std::to_string(id)));
		}
	}
}

void scan_callback(const std_msgs::Bool &msg)
{
	canScan = msg.data;
}

int main(int argc, char** argv){
	ros::init(argc, argv, "apriltag_tf_broadcaster");
	ros::NodeHandle nh;
	ros::Subscriber sub =  nh.subscribe("object_location", 1, &transform_callback);
	ros::Subscriber subscan =  nh.subscribe("scan", 1, &scan_callback);
	if (ros::param::get("~id",id))
 	{
		std::cout<<"Using id  "<<id<<std::endl;
	}
	else
	{
		id=0;
		ROS_INFO("No parameter 'id' found. Using id 0 for the april tag");
	}

	ros::spin();
};
