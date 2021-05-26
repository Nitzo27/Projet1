#! /usr/bin/env python

import rospy
from std_msgs.msg import Float64

rospy.init_node('lidar')

pub = rospy.Publisher('myTopic',  Float64, queue_size=10)
rate = rospy.Rate(1)



my_msg = Float64()

my_msg.data = 19

while not rospy.is_shutdown():
    pub.publish(my_msg)
    rate.sleep()
