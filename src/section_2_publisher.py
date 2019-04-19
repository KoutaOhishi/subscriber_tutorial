#! /usr/bin/env python
# coding:utf-8
import rospy
import random
import time
from std_msgs.msg import String, Int32
from subscriber_tutorial.msg import Formula

if __name__ == "__main__":
    rospy.init_node("publisher")

    pub = rospy.Publisher("subscriber_tutorial/formula", Formula, queue_size=1)

    while not rospy.is_shutdown():
        try:
            msg = Formula()

            msg.item_1 = int(random.uniform(-100,100))

            while True:
                msg.item_2 = int(random.uniform(-100,100))
                if msg.item_2 != 0:
                    break

            tmp = int(random.uniform(-100,100)%4)
            if tmp == 0:
                msg.operators = "+"
            elif tmp == 1:
                msg.operators = "-"
            elif tmp == 2:
                msg.operators = "*"
            else: #tmp == 3:
                msg.operators = "/"

            pub.publish(msg)
            time.sleep(1)

        except KeyboardInterrupt:
            break
