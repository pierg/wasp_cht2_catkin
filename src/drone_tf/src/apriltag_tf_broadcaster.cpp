//This node is responsible for converting the apriltag location in respect to the turtlebot.
// This way we can set up a listener that looks at the apriltag tf and put it into the world coordinate system

#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include "tb_self_experimentation/object_loc.h"

//This callback function is responsible for getting the camera-apriltag distance and add a mpde tp tje 
void transform_callback(const tb_self_experimentation::object_loc &msg)
{
	static tf::TransformBroadcaster br;
	tf::Transform transform;
	transform.setOrigin( tf::Vector3(msg.point.x, msg.point.y, msg.point.z) );
	tf::Quaternion qt = tf::Quaternion();
	qt.setRPY(0,-msg.angles.y,0);//pure experimentation with the angles published by the april tag
	transform.setRotation(qt);
	br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "camera_rgb_frame", "apriltag"));
}

int main(int argc, char** argv){
	ros::init(argc, argv, "apriltag_tf_broadcaster");
	ros::NodeHandle nh;
	ros::Subscriber sub =  nh.subscribe("apriltag/distance", 1, &transform_callback);
	ros::spin();
};
