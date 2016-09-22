#!/usr/bin/env python
'''
This source will act as support to finish your project and does not follow best
coding practices.
'''
#Import Python Packages, ROS messages
from __future__ import print_function
from __future__ import division
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
import time
from geometry_msgs.msg import PointStamped
from sensor_msgs.msg import Image
#import the custom message we created to store objects
from wasp_custom_msgs.msg import object_loc
import tf
from math import hypot

#Define Constants
#Define Constants
#Ratio W/H = 1.77
IMG_W = 300
IMG_H = 176
GRANULARITY = 0.02

ite = 0


#Focal Length of the Asus Prime sensor camera
focal_leng = 570.34222

#This may change during the competetion, need to be calibrated
square_side_lenth = 0.115 #in mts

#This function finds the lengths of all the sides and estimates the longest.
def Longest_Length(approxcontour):
	#add the first element in the end to complete the loop
	approxcontour = np.concatenate((approxcontour,[approxcontour[0]]))
	#The below lines find the length between two adjacent points
	#and append them in  an array
	ptdiff = lambda (p1,p2): (p1[0]-p2[0], p1[1]-p2[1])
	diffs = map(ptdiff, zip(approxcontour,approxcontour[1:]))
	dist = []
	for d in diffs:
		dist.append(hypot(*d))
	#find maximum of lenghts found
	LongestSide = max(dist)
	return LongestSide



#This is the main class for object detection, it has some initializations about nodes
#Call back functions etc
class object_detection:
	def __init__(self):
		#Create Rospy Publisher and subscriber
		self.object_location_pub = rospy.Publisher("/object_location", object_loc, queue_size =1)
		#original images is huge and creates lot of latency, therefore subscribe to compressed image

		#self.image_sub = rospy.Subscriber("/camera/rgb/image_raw/compressed",CompressedImage, self.callback)
		#self.image_sub = rospy.Subscriber("/ardrone/image_raw",Image,self.callback)
		self.image_sub = rospy.Subscriber("/ardrone/image_raw/compressed",CompressedImage,self.callback)
		#Cv Bridge is used to convert images from ROS messages to numpy array for openCV and vice versa
		self.bridge = CvBridge()
		#Obejct to transform listener which will be used to transform the points from one coordinate system to other.
		self.tl = tf.TransformListener()

	#Callback function for subscribed image

	def callback(self,data):
	#asdasd
		global ite
		ite = ite + 1
		if ite == 100 :
		    ite = 0
		    #The below two functions conver the compressed image to opencv Image
		    #'''
		    np_arr = np.fromstring(data.data, np.uint8)
		    #cv_image = cv2.imdecode(np_arr, cv2.CV_LOAD_IMAGE_COLOR)


		    cv_image = cv2.imdecode(np_arr, cv2.CV_LOAD_IMAGE_COLOR)
		    cv_image_small = cv2.resize(cv_image, (IMG_W, IMG_H))
		    cv_image = cv_image_small


		    #'''
		    #cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		    #Create copy of captured image
		    img_cpy = cv_image.copy()
		    #Color to HSV and Gray Scale conversion
		    hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
		    #gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

		    #Red_Thresholds
		    lower_red1 = np.array([0, 100, 50])
		    #lower_red1 = np.array([0, 100, 100])

		    upper_red1 = np.array([5, 255,255])

		    lower_red2 = np.array([160,100,50])
		    #lower_red2 = np.array([160,100,100])

		    upper_red2 = np.array([179,255,255])
		    #Blue Thresholds

		    #brighter treshold
		    #lower_blue = np.array([104,110,110])
		    #darker treshold
		    lower_blue = np.array([104,110,50])
		    upper_blue = np.array([143,255,255])
		    #Green Thresholds

		    #darker treshold:
		    lower_green = np.array([60,60,20])
		    #brighter treshold:
		    #lower_green = np.array([60,60,46])
		    upper_green = np.array([97,255,255])

		    # Threshold the HSV image to get only single color portions
		    mask2 = cv2.inRange(hsv, lower_green, upper_green)
		    mask3 = cv2.inRange(hsv, lower_red1, upper_red1)
		    mask4 = cv2.inRange(hsv, lower_red2, upper_red2)
		    mask5 = cv2.inRange(hsv, lower_blue, upper_blue)

		    mask_list = np.array([mask2, mask3, mask4, mask5])

		    #Find contours(borders) for the shapes in the image
		    #NOTE if you get following error:
		    # contours, hierarchy = cv2.findContours(mask2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		    # ValueError: need more than two values to unpack
		    # change following line to:
		    # contours, hierarchy = cv2.findContours(mask2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		    for m in range (4):
		        mask = mask_list[m]
		        #print("m = ", m)

		        contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		        numLargeContours = 0
		        for x in range (len(contours)):
		            contourarea = cv2.contourArea(contours[x])
		            #if contourarea > 600:
		            if contourarea > 100:
		                numLargeContours = numLargeContours + 1

		        #print (numLargeContours)
		        #Pass through each contour and check if it has required properties to classify into required object
		        for x in range (len(contours)):
		            contourarea = cv2.contourArea(contours[x]) #get area of contour
		            if contourarea > 600: #Discard contours with a small area as this may just be noise
		                #The below 2 functions help you to approximate the contour to a nearest polygon
		                arclength = cv2.arcLength(contours[x], True)
		                approxcontour = cv2.approxPolyDP(contours[x], GRANULARITY * arclength, True)
		                #Find the coordinates of the polygon with respect to he camera frame in pixels
		                rect_cordi = cv2.minAreaRect(contours[x])
		                obj_x = int(rect_cordi[0][0])
		                obj_y = int(rect_cordi[0][1])

		                ID = 0
		                #Simple shape
		                if numLargeContours == 1:
		                    #print("m2 = ", m)
		                    #Green
		                    if m == 0:
		                        #print("m0 = ", m, " (green)")
		                        #Check for Square
		                        if len(approxcontour) == 4:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((4,2))
		                            ID = 122
		                        #Check for Star
		                        elif len(approxcontour) == 8:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((8,2))
		                            ID = 121
		                        #Check for Triangle
		                        elif len(approxcontour) == 3:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((3,2))
		                            ID = 123

		                    #Red
		                    elif m == 1 or m == 2:
		                        #print("m1/2 = ", m, " (red)")
		                        #Check for Square
		                        if len(approxcontour) == 4:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((4,2))
		                            ID = 112
		                        #Check for Star
		                        elif len(approxcontour) == 8:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((8,2))
		                            ID = 111
		                        #Check for Triangle
		                        elif len(approxcontour) == 3:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((3,2))
		                            ID = 113

		                    #Blue
		                    elif m == 3:
		                        #Check for Square
		                        if len(approxcontour) == 4:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((4,2))
		                            ID = 132
		                        #Check for Star
		                        elif len(approxcontour) == 8:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((8,2))
		                            ID = 131
		                        #Check for Triangle
		                        elif len(approxcontour) == 3:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((3,2))
		                            ID = 133

		                #Complex Shape
		                elif numLargeContours == 2:
		                    #Green
		                    if m == 0:
		                        #Check for Square
		                        if len(approxcontour) == 4:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((4,2))
		                            ID = 125
		                        #Check for Star
		                        elif len(approxcontour) == 8:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((8,2))
		                            ID = 124

		                    #Red
		                    elif m == 1 or m == 2:
		                        #Check for Square
		                        if len(approxcontour) == 4:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((4,2))
		                            ID = 115
		                        #Check for Star
		                        elif len(approxcontour) == 8:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((8,2))
		                            ID = 114

		                    #Blue
		                    elif m == 3:
		                        #Check for Square
		                        if len(approxcontour) == 4:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((4,2))
		                            ID = 135
		                        #Check for Star
		                        elif len(approxcontour) == 8:
		                            #print ('Length ', len(approxcontour))
		                            cv2.drawContours(cv_image,[approxcontour],0,(0,255,255),2)
		                            approxcontour = approxcontour.reshape((8,2))
		                            ID = 134
		                    #Move to next Contour
		                    else:
		                        continue


		                if ID == 0 :
		                    continue

		                LongestSide = Longest_Length(approxcontour)
		                Distance = (focal_leng*square_side_lenth)/LongestSide

		                #Calculate Cordinates wrt to Camera, convert to Map
		                #Coordinates and publish message for storing
		                #319.5, 239.5 = image centre
		                obj_cam_x = ((obj_x - 319.5)*Distance)/focal_leng
		                obj_cam_y = ((obj_y - 239.5)*Distance)/focal_leng

		                #convert the x,y in camera frame to a geometric stamped point
		                P = PointStamped()
		                P.header.stamp = rospy.Time.now() - rospy.Time(23)
		                #print ('time: ', data.header.stamp)
		                P.header.frame_id = 'camera_rgb_optical_frame'
		                P.point.x = obj_cam_x
		                P.point.y = obj_cam_y
		                P.point.z = Distance
		                roundx = float("{0:.2f}".format(P.point.x))
		                roundy = float("{0:.2f}".format(P.point.y))
		                roundz = float("{0:.2f}".format(P.point.z))
		                print("Distance: x=", roundx, ", y=", roundy, ", z=", roundz)

		                #Transform Point into map coordinates
		                #trans_pt = self.tl.transformPoint('/map', P)

		                #fill in the publisher object to publish
		                obj_info_pub = object_loc()
		                obj_info_pub.ID = ID #ID need to be changed
		                #obj_info_pub.point.x = trans_pt.point.x
		                #obj_info_pub.point.y = trans_pt.point.y
		                #obj_info_pub.point.z = trans_pt.point.z

		                #publish the message
		                self.object_location_pub.publish(obj_info_pub)


		        #Display the captured image
		        cv2.imshow("Image",cv_image)
		        #cv2.imshow("HSV", hsv)
		        cv2.waitKey(1)


#Main function for the node
def main(args):
	rospy.init_node('object_detection', anonymous = False)
	ic = object_detection()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print('Shutting Down object_detection Node')
		cv2.destroyAllWindows()

if __name__ == '__main__':
	main(sys.argv)

