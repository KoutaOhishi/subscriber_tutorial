#! /usr/bin/env python
# coding:utf-8
import rospy
import codecs
import time
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("encryption_publisher")

    pub = rospy.Publisher("subscriber_tutorial/encryption", String, queue_size=1)

    while not rospy.is_shutdown():
        try:
            #encryption = codecs.decode("Soka University", "rot13")
            pub.publish(codecs.decode("Soka University", "rot13"))
            time.sleep(1)

            pub.publish(codecs.decode("Choi Laboratory", "rot13"))
            time.sleep(1)

            pub.publish(codecs.decode("Team SOBITS", "rot13"))
            time.sleep(1)

        except KeyboardInterrupt:
            break
