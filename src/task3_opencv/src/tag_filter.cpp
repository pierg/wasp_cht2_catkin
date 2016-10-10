#include <ros/ros.h>
#include "wasp_custom_msgs/object_loc.h"
#include <std_msgs/Float64.h>
using namespace std;

//Simple Global variables
ros::Publisher pub_x;
ros::Publisher pub_y;
ros::Publisher pub_phi;
int id_ref = 0;

void filterTag(const wasp_custom_msgs::object_loc &msg)
{
	int id = msg.ID;
	if(id == id_ref)
	{
		std_msgs::Float64 dist_x; double x;
		std_msgs::Float64 dist_y; double y;
		std_msgs::Float64 phi;
		dist_x.data = msg.point.x;
		dist_y.data = msg.point.y;
		//phi =
		pub_x.publish(dist_x);
		pub_y.publish(dist_y);
		//pub_phi.publish(dist_x);

		std::cout << "ID "<< id << ", distance x: " << dist_x <<std::endl;
		std::cout << "ID "<< id << ", distance y: " << dist_y <<std::endl;

	}
}

int main(int argc, char **argv) 
{
	// Initialize the ROS system.
	ros::init(argc, argv, "filter_tag");
	// Establish this program as a ROS node. Private node to receive only the node parameters
	ros::NodeHandle nh("~");
	
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
	ros::Subscriber sub = nh.subscribe("object_location/", 1, &filterTag);
	//Setting the publisher
	pub_x = nh.advertise<std_msgs::Float64>("state_x/", 1);
	pub_y = nh.advertise<std_msgs::Float64>("state_y/", 1);
	pub_phi = nh.advertise<std_msgs::Float64>("state_phi/", 1);
	
	
	ros::spin();
}

