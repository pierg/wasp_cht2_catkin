#include "headers/PCL_transform.h"

ros::Publisher tf_pub;
tf::TransformListener *tf_listener;

void callback(const sensor_msgs::PointCloud2ConstPtr& input)
{
 // Converting from PointCloud2 msg to pcl::PointCloud
 pcl::PCLPointCloud2 pcl_pc2;
 pcl::PointCloud<pcl::PointXYZ>::Ptr pcl_out(new pcl::PointCloud<pcl::PointXYZ>);
 pcl_conversions::toPCL(*input,pcl_pc2);
 pcl::PointCloud<pcl::PointXYZ>::Ptr pcl_in(new pcl::PointCloud<pcl::PointXYZ>);
 pcl::fromPCLPointCloud2(pcl_pc2,*pcl_in);

 // waiting for the transform and transform point cloud from its frame to the /camera_link frame
 // You might need to change camera_link frame to what ever frame you would like your
 // pointcloud to be transformed to...
 tf_listener->waitForTransform("/camera_link", (*pcl_in).header.frame_id, input->header.stamp, ros::Duration(5.0));
 pcl_ros::transformPointCloud("/camera_link", *pcl_in, *pcl_out, *tf_listener);

 sensor_msgs::PointCloud2 output;
 pcl::toROSMsg (*pcl_out, output);
 tf_pub.publish(output);
}

int main(int argc, char** argv)
{
 ros::init(argc, argv, "PCL_transform");
 ros::NodeHandle nh;
 ros::Subscriber sub = nh.subscribe("/camera/depth/filtered_points", 1, callback);
 tf_pub = nh.advertise<sensor_msgs::PointCloud2> ("/camera/depth/cloud_transformed", 1);

 tf_listener    = new tf::TransformListener();

 ros::spin();
 return 0;
}
