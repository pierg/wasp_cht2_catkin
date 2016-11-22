#!/usr/bin/env python
import web
import view
from view import render
import roslib
import rospy


from os.path import expanduser
currentFile = expanduser("~") + '/wasp_challenge_current_state';

urls = ('/', 'index')

class index:
	def GET(self):
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