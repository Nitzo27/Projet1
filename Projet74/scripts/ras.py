#! /usr/bin/env python
import rospy
from std_msgs.msg import Float64

rospy.init_node('ras')

def callback(data):
        data.data=data.data-1
        print (data.data)

rospy.Subscriber('myTopic', Float64, callback)

while not rospy.is_shutdown():
    pass
