#!/usr/bin/env python

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# WASP Challenge - Chalmers
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Server getting the request from the index.html
# It processes it according to the "action" value and publishes commands to the scheduler.py accordingly
# Available actions are: start, cancel and emergency_area
#
# ROS Node name: skynet
# Publishing on: wasp_cth_operator



import web
import view
from view import render
from std_msgs.msg import String
import rospy


from os.path import expanduser
currentFile = expanduser("~") + '/wasp_challenge_current_state';

# urls = ('/', 'index')

pubToScheduler = rospy.Publisher('wasp_cth_operator', String, queue_size=1)


urls = (
    '/' , 'index' ,
    '/add', 'add' ,
    '/(js|css|images)/(.*)', 'static',
    '/one' , 'one'
)

class static:
    def GET(self, media, file):
        try:
            f = open(media+'/'+file, 'r')
            return f.read()
        except:
            return '' # you can send an 404 error here if you want


class index:
    def GET(self):
        data = web.input(action="no action")
        if(data.action == 'start'):
            pubToScheduler.publish("start")
            return "Start Command Published Successfully"

        if(data.action == 'cancel'):
            pubToScheduler.publish("cancel")
            return "Cancel Command Published Successfully"

        data = web.input(emergency_area_x="no_x")

        if(data.emergency_area_x != 'no_x'):
            data = web.input(emergency_area_y="no_y")
            if(data.emergency_area_y != 'no_y'):
                pubToScheduler.publish("emergency_area " + str(data.emergency_area_x) + " " + str(data.emergency_area_y))
                return "Emergency Area with X,Y=(" + str(data.emergency_area_x) + "," + str(data.emergency_area_y) + ") Published Successfully"
        else:
            if len(web.input()) > 0:
                with open(currentFile, 'r') as f:
                    data=f.read()
                return data
            else:
                return render.index(view.list())

if __name__ == "__main__":
    rospy.init_node('skynet')
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
    rospy.spin()