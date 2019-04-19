#! /usr/bin/env python
# coding:utf-8
def decoder(input):
    """
        inputに暗号を入れると、解読した結果をreturnします。
    """
    import codecs
    return codecs.decode(str(input), "rot13")

import rospy
import time
from std_msgs.msg import String

def callback(msg):
    print decoder(msg.data)


if __name__ == "__main__":
    rospy.init_node("encryption_subscriber")

    sub = rospy.Subscriber("subscriber_tutorial/encryption", String, callback)

    rospy.spin()
