#! /usr/bin/env python
# coding:utf-8
import rospy
import random
import time
from std_msgs.msg import String, Int32

item_1_g = Int32()
item_2_g = Int32()
operators_g = String()

def item_1_callback(msg):
    global item_1_g
    item_1_g = msg

def item_2_callback(msg):
    global item_2_g
    item_2_g = msg

def operators_callback(msg):
    global operators_g
    operators_g = msg

def calc():
    if operators_g.data == "+":
        res = item_1_g.data + item_2_g.data
        rospy.loginfo("(%s) %s (%s) = %s"%(str(item_1_g.data),operators_g.data,str(item_2_g.data),str(res)))

    elif operators_g.data == "-":
        res = item_1_g.data - item_2_g.data
        rospy.loginfo("(%s) %s (%s) = %s"%(str(item_1_g.data),operators_g.data,str(item_2_g.data),str(res)))

    elif operators_g.data == "*":
        res = item_1_g.data * item_2_g.data
        rospy.loginfo("(%s) %s (%s) = %s"%(str(item_1_g.data),operators_g.data,str(item_2_g.data),str(res)))

    else: #operators_g.data == "/":
        if item_2_g.data != 0:
            res = float(item_1_g.data) / float(item_2_g.data)
            rospy.loginfo("(%s) %s (%s) = %s"%(str(item_1_g.data),operators_g.data,str(item_2_g.data),str(res)))

if __name__ == "__main__":
    rospy.init_node("formula_subscriber")

    sub_item_1 = rospy.Subscriber("subscriber_tutorial/item_1", Int32, item_1_callback)
    sub_item_2 = rospy.Subscriber("subscriber_tutorial/item_2", Int32, item_2_callback)
    sub_operators = rospy.Subscriber("subscriber_tutorial/operators", String, operators_callback)

    while True:
        if sub_item_1.get_num_connections() != 0:
            if sub_item_2.get_num_connections() != 0:
                if sub_operators.get_num_connections() != 0:
                    break

    while not rospy.is_shutdown():
        calc()
        time.sleep(1)
