#include <ros/ros.h>

//ROS Messages
#include "wasp_custom_msgs/object_loc.h"
#include "wasp_custom_msgs/image_point.h"
#include <std_msgs/Float64.h>
#include <std_msgs/Bool.h>
using namespace std;

//Simple Global variables
ros::Publisher pub_x;
ros::Publisher pub_y;
ros::Publisher pub_z;
ros::Publisher pub_yaw;
ros::Publisher pub_pitch_image;
ros::Publisher pub_roll_image;

ros::Publisher pub_pid_enable;
int id_ref = 0;

void filterTag_object_location(const wasp_custom_msgs::object_loc &msg)
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
		std_msgs::Float64 pitch_deg;
  		std_msgs::Float64 yaw_deg;
        std_msgs::Float64 roll_deg;
		
		//Retrieving info from message
		dist_x.data = msg.point.x;
		dist_y.data = msg.point.y;
		dist_z.data = msg.point.z;

		// Fixed
		pitch.data = msg.angles.z;
		yaw.data = msg.angles.x;
		roll.data = msg.angles.y;


		pitch_deg.data = pitch.data * 57.2958;
		yaw_deg.data = yaw.data * 57.2958;
		roll_deg.data = roll.data * 57.2958;


		//Publishing data
		pub_x.publish(dist_x);
		pub_y.publish(dist_y);
        pub_y.publish(dist_z);

		pub_pitch_image.publish(pitch_deg);
		pub_roll_image.publish(roll_deg);


		//If it is  detecting the reference enable PID
		std_msgs::Bool enable;
		enable.data = true;
		pub_pid_enable.publish(enable);


		std::cout << std::setprecision(3) << std::fixed;

		std::cout << "ID \t\t Roll \t\t Pitch \t\t Yaw" << std::endl;
		std::cout << id << "\t\t" << roll_deg.data << "\t\t" << pitch_deg.data << "\t\t" << yaw_deg.data << std::endl << std::endl;

		std::cout << "ID \t\t X_d \t\t Y_d \t\t Z_d" << std::endl;
	    std::cout << id << "\t\t" << dist_x.data << "\t\t" << dist_y.data << "\t\t" << dist_z.data << std::endl << std::endl << std::endl;

	}
}

void filterTag_tag_location_image(const wasp_custom_msgs::image_point &msg)
{

	int id = msg.ID;
	//std::cout<<"Callback"<<std::endl;
	if(id == id_ref)
	{
		std_msgs::Float64 center_x;
		//double center_y;
		//int width;
		//int height;
		center_x.data = msg.point.x;
		//center_y = msg.point.y;
		//height = msg.height.data;
		//width = msg.width.data;
        pub_yaw.publish(center_x);

		cout << "CENTER_X : \t" << center_x.data << "\n\n" << endl;// <<"   "<< center_y << "   "<< height<< "   "<< width<<endl;
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
	ros::Subscriber sub = nh.subscribe("object_location", 1, &filterTag_object_location);
	ros::Subscriber sub2 = nh.subscribe("tag_location_image", 1, &filterTag_tag_location_image);
	//Setting the publisher
	pub_x = nh.advertise<std_msgs::Float64>("state_x/", 1);
	pub_y = nh.advertise<std_msgs::Float64>("state_y/", 1);
	pub_z = nh.advertise<std_msgs::Float64>("state_z/", 1);
    //from the center of the picture
	pub_yaw = nh.advertise<std_msgs::Float64>("state_yaw/", 1);
    //the parameters of the april tag
	pub_pitch_image = nh.advertise<std_msgs::Float64>("image_pitch/", 1);
	pub_roll_image = nh.advertise<std_msgs::Float64>("image_roll/", 1);

	pub_pid_enable = nh.advertise<std_msgs::Bool>("pid_enable/", 1);

	
	ros::spin();
}

