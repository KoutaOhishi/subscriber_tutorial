#! /usr/bin/env python
# coding:utf-8
import rospy
import random
import time
from std_msgs.msg import String, Int32
from subscriber_tutorial.msg import Formula

if __name__ == "__main__":
    rospy.init_node("publisher")

    #pub = rospy.Publisher("subscriber_tutorial/formula", Formula, queue_size=1)

    pub_item_1 = rospy.Publisher("subscriber_tutorial/item_1", Int32, queue_size=1)
    pub_item_2 = rospy.Publisher("subscriber_tutorial/item_2", Int32, queue_size=1)
    pub_operators = rospy.Publisher("subscriber_tutorial/operators", String, queue_size=1)

    while not rospy.is_shutdown():
        try:
            item_1 = int(random.uniform(-100,100))

            while True:
                item_2 = int(random.uniform(-100,100))
                if item_2 != 0:
                    break

            tmp = int(random.uniform(-100,100)%4)
            if tmp == 0:
                operators = "+"
            elif tmp == 1:
                operators = "-"
            elif tmp == 2:
                operators = "*"
            else: #tmp == 3:
                operators = "/"

            pub_item_1.publish(item_1)
            pub_item_2.publish(item_2)
            pub_operators.publish(operators)
            time.sleep(1)

        except KeyboardInterrupt:
            break
