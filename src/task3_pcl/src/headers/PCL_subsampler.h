#include <ros/ros.h>
#include <ros/console.h>
#include <signal.h>
#include <iostream>
// PCL specific includes

// Include PointCloud message that we subscribe to
#include <sensor_msgs/PointCloud2.h>
// Include pass through filter
#include <pcl/filters/passthrough.h>
// Include voxel grid filter
#include <pcl/filters/voxel_grid.h>
// Include SOR filter
#include <pcl/filters/statistical_outlier_removal.h>
// Include library for convering from message to PCL::PointCloud
#include <pcl_conversions/pcl_conversions.h>


/* Truncating cloud on the interval [min, max] across the specified axis
Arguments:
cloud       cloud to filter
axis        axis to filter across
min         lower limit
max         upper limit
For more information check:
http://pointclouds.org/documentation/tutorials/passthrough.php
*/
void pass_through(pcl::PointCloud<pcl::PointXYZ>::Ptr cloud, std::string axis,
                                                        double min, double max){
  pcl::PassThrough<pcl::PointXYZ> pass;
  pass.setInputCloud(cloud);
  pass.setFilterFieldName(axis);
  pass.setFilterLimits(min, max);
  pass.filter(*cloud);
}

/* Downsampling cloud with leaf_size. The bigger leaf_size the more sparce cloud.
For more information check:
http://pointclouds.org/documentation/tutorials/voxel_grid.php
*/
void voxel_grid(pcl::PointCloud<pcl::PointXYZ>::Ptr cloud, double leaf_size){
  // 2. Downsampling with VoxelGrid
  pcl::VoxelGrid<pcl::PointXYZ> vox;
  vox.setInputCloud(cloud);
  vox.setLeafSize(leaf_size, leaf_size, leaf_size);
  vox.filter(*cloud);
}

/* Removing outliers with SOR filter
For more information check:
http://pointclouds.org/documentation/tutorials/statistical_outlier.php
*/
void statistical_outlier_removal(pcl::PointCloud<pcl::PointXYZ>::Ptr cloud,
    double mean_k, double stddev_thresh){
  // 3. Statistical outlier removal
  pcl::StatisticalOutlierRemoval <pcl::PointXYZ> sor;
  sor.setInputCloud(cloud);
  sor.setMeanK (mean_k);
  sor.setStddevMulThresh(stddev_thresh);
  sor.filter(*cloud);
}
