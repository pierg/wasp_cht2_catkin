//This node is responsible for converting the apriltag location in respect to the turtlebot.
// This way we can set up a listener that looks at the apriltag tf and put it into the world coordinate system

#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include "wasp_custom_msgs/object_loc.h"
#include "std_msgs/Bool.h"
#include "std_msgs/String.h"
#include "std_srvs/Empty.h"
#include <string>
#include "geometry_msgs/Pose2D.h"


bool canScan = false;
bool detected = false;
ros::ServiceClient serviceClient;
ros::Publisher pub;
geometry_msgs::Pose2D position;
geometry_msgs::Pose2D apriltag_position;
int id;


void toggleCamera()
{
	std_srvs::Empty empty;
	if(serviceClient.call(empty))
		{
			std::cout<<"Changing camera"<<std::endl;		
		}
}

//This callback function is responsible for getting the camera-apriltag distance and add a mpde tp tje 
void transform_callback(const wasp_custom_msgs::object_loc &msg)
{
		
		apriltag_position.x = position.x;
		apriltag_position.y = position.y;
		id = msg.ID;

}

void scan_callback(const std_msgs::Bool &msg)
{
	canScan = msg.data;
	if(canScan)
	{
		toggleCamera();
		double x,y;
		
		x = apriltag_position.x;
		y = apriltag_position.y;
		std::string s = std::to_string(x) + " " +std::to_string(y) +  " " + std::to_string(id);
		std::cout<<s<<std::endl;
		std_msgs::String pubmsg;
		pubmsg.data = s;			
		pub.publish(pubmsg);
		toggleCamera();
		canScan=false;
	}

}

void droneGlobalPositionCallback(const geometry_msgs::Pose2D &msg)
{
	position.x = msg.x;
	position.y = msg.y;
}

int main(int argc, char** argv){
	ros::init(argc, argv, "apriltag_victim");
	ros::NodeHandle nh;
	serviceClient = nh.serviceClient<std_srvs::Empty>("ardrone/togglecam");
	pub = nh.advertise<std_msgs::String>("/wasp_cth_victims", 10);
	ros::Subscriber sub =  nh.subscribe("global_position", 1, &droneGlobalPositionCallback);
	ros::Subscriber sub2 =  nh.subscribe("object_location", 1, &transform_callback);
	ros::Subscriber subscan =  nh.subscribe("scan", 1, &scan_callback);
	ros::spin();
};
