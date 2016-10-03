#include <ros/ros.h>
#include "wasp_custom_msgs/object_loc.h"
#include <std_msgs/Float64.h>
using namespace std;

//Simple Global variables
ros::Publisher pub;
int id_ref = 0;

void filterTag(const wasp_custom_msgs::object_loc &msg)
{
	int id = msg.ID;
	if(id == id_ref)
	{
		std_msgs::Float64 dist_x;
		dist_x.data = msg.point.x;
		pub.publish(dist_x);
		std::cout << "ID "<< id << ", distance x: " << dist_x<<std::endl;
	}
}

int main(int argc, char **argv) 
{
	// Initialize the ROS system.
	ros::init(argc, argv, "filter_tag");
	// Establish this program as a ROS node.
	ros::NodeHandle nh;
	//Declaring and setting the subscriber
	ros::Subscriber sub = nh.subscribe("object_location/", 1, &filterTag);
	//Setting the publisher
	pub = nh.advertise<std_msgs::Float64>("state/", 1);
	


	
	ros::spin();
}

