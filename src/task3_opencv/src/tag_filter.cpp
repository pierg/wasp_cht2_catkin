#include <ros/ros.h>

//ROS Messages
#include "wasp_custom_msgs/object_loc.h"
//#include "wasp_custom_msgs/image_point.h"
#include <std_msgs/Float64.h>
#include <std_msgs/Bool.h>
using namespace std;

//Simple Global variables
ros::Publisher pub_x;
ros::Publisher pub_y;
//ros::Publisher pub_yaw;

ros::Publisher pub_pid_enable;
int id_ref = 0;

void filterTag(const wasp_custom_msgs::object_loc &msg)
{

	int id = msg.ID;
	//std::cout<<"Callback"<<std::endl;
	if(id == id_ref)
	{
		
		//distance
		std_msgs::Float64 dist_x;
		std_msgs::Float64 dist_y;
		std_msgs::Float64 dist_z;
		//Euler angles
		std_msgs::Float64 pitch;
		std_msgs::Float64 yaw;
		std_msgs::Float64 roll;
		
		//Retrieving info from message
		dist_x.data = msg.point.x;
		dist_y.data = msg.point.y;
		dist_z.data = msg.point.z;
		pitch.data = msg.angles.x;
		yaw.data = msg.angles.y;
		roll.data = msg.angles.z;

		//Publishing data
		
		pub_x.publish(dist_x);
		pub_y.publish(dist_y);
		//If it is  detecting the reference enable PID
		std_msgs::Bool enable;
		enable.data = true;
		pub_pid_enable.publish(enable);
		
		//Debugging
		//std::cout << "ID "<< id << ", distance x: " << dist_x <<std::endl;
		//std::cout << "ID "<< id << ", distance y: " << dist_y <<std::endl;
		//std::cout << "ID "<< id << ", distance z: " << dist_z <<std::endl;
		std::cout << "ID "<< id << ", Pitch: " << pitch <<std::endl;
		std::cout << "ID "<< id << ", Yaw: " << yaw <<std::endl;
		std::cout << "ID "<< id << ", Roll: " << roll <<std::endl;
	}
}

int main(int argc, char **argv) 
{
	// Initialize the ROS system.
	ros::init(argc, argv, "filter_tag");
	// Establish this program as a ROS node. 
	//Public node	
	ros::NodeHandle nh;
	
	//Getting parameter name id for the april tag	
	if (nh.hasParam("id_ref"))
 	{
 		// Found parameter, can now query it using param_name
		nh.getParam("id_ref", id_ref);
		std::cout<<"Using id_ref  "<<id_ref<<std::endl;
	}
	else
	{
		id_ref=0;
		ROS_INFO("No parameter 'id_ref' found. Using id 0 for the april tag");
	}


	//Declaring and setting the subscriber
	ros::Subscriber sub = nh.subscribe("object_location", 1, &filterTag);
	//Setting the publisher
	pub_x = nh.advertise<std_msgs::Float64>("state_x/", 1);
	pub_y = nh.advertise<std_msgs::Float64>("state_y/", 1);
	
	pub_pid_enable = nh.advertise<std_msgs::Bool>("pid_enable/", 1);
	//pub_phi = nh.advertise<std_msgs::Float64>("state_phi/", 1);
	
	
	ros::spin();
}

