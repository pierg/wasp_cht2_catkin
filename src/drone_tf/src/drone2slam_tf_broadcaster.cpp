//This node is responsible for converting the apriltag location in respect to the turtlebot.
// This way we can set up a listener that looks at the apriltag tf and put it into the world coordinate system

#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include "wasp_custom_msgs/object_loc.h"
#include "std_msgs/Bool.h"
#include "nav_msgs/Odometry.h"
#include <string>

double scale;
//This callback function is responsible for getting the camera-apriltag distance and add a mpde tp tje 
void transform_callback(const nav_msgs::Odometry &msg)
{
			std::cout<<msg.pose.pose.position.x<<std::endl;
			std::cout<<msg.pose.pose.position.y<<std::endl;
			std::cout<<msg.pose.pose.position.z<<std::endl;
			static tf::TransformBroadcaster br;
			tf::Transform transform;
			
			transform.setOrigin( tf::Vector3(msg.pose.pose.position.x*scale, msg.pose.pose.position.y*scale, msg.pose.pose.position.z*scale) );
			//We dont care about the rotation of the tag	
			tf::Quaternion qt = tf::Quaternion(msg.pose.pose.orientation.x,msg.pose.pose.orientation.y,msg.pose.pose.orientation.z,msg.pose.pose.orientation.w);
			//qt.setRPY(0,0,0);//pure experimentation with the angles published by the april tag
			transform.setRotation(qt);

			br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "slam/map", "drone"));

}

int main(int argc, char** argv){
	ros::init(argc, argv, "slam2drone_tf_broadcaster");
	ros::NodeHandle nh;
	ros::Subscriber sub =  nh.subscribe("slam/pos", 1, &transform_callback);
	if (ros::param::get("~scale",scale))
 	{
		std::cout<<"scale"<<scale<<std::endl;
	}
	else
	{
		scale=1;
		ROS_INFO("No parameter 'scale' found. Using scale 1 for the scale");
	}
	ros::spin();
};
