//THis is a very basic node that filters the content of the identified april tags for a single id number. THis way we can select only the tags we are interested

#include <ros/ros.h>
//ROS Messages
#include "wasp_custom_msgs/object_loc.h"
#include <std_msgs/Float64.h>
#include <std_msgs/Bool.h>
#include <geometry_msgs/Pose2D.h>
#include <tf/transform_datatypes.h>
#include <visualization_msgs/Marker.h>


using namespace std;
//Simple Global variables
ros::Publisher marker_pub;
uint32_t shape = visualization_msgs::Marker::CUBE;

void updateMarkers(const geometry_msgs::Pose2D &msg)
{
	tf::Quaternion qt = tf::Quaternion();
	qt.setRPY(0,0,msg.theta);
	visualization_msgs::Marker marker;
	marker.header.frame_id = "/map";
	marker.header.stamp = ros::Time::now();
	marker.ns = "drone";
	marker.id = 0;
	marker.type = shape;
	marker.pose.position.x = msg.x;
	marker.pose.position.y = msg.y;
	marker.pose.position.z = 0;
	marker.pose.orientation.x = qt.x();
	marker.pose.orientation.y = qt.y();
	marker.pose.orientation.z = qt.z();
	marker.pose.orientation.w = qt.w();

	cout << marker.pose <<endl;

	// Set the scale of the marker -- 1x1x1 here means 1m on a side
	marker.scale.x = 0.1;
	marker.scale.y = 0.1;
	marker.scale.z = 1.0;

	// Set the color -- be sure to set alpha to something non-zero!
	marker.color.r = 0.0f;
	marker.color.g = 1.0f;
	marker.color.b = 0.0f;
	marker.color.a = 1.0;
	
	marker_pub.publish(marker);
}

int main( int argc, char** argv )
{
	ros::init(argc, argv, "drone_rviz_markers");
	ros::NodeHandle nh;

	//Declaring and setting the subscriber and publisher
	ros::Subscriber sub = nh.subscribe("global_position", 1, &updateMarkers);
	marker_pub = nh.advertise<visualization_msgs::Marker>("/visualization_marker", 1);
	
	ros::spin();
	

}
