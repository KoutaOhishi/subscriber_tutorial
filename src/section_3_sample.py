#! /usr/bin/env python
# coding:utf-8
import rospy
import random
import time
from std_msgs.msg import String, Int32

item_1_global = Int32()
item_2_global = Int32()
operators_global = String()

def item_1_callback(msg):
    global item_1_global
    item_1_global = msg

def item_2_callback(msg):
    global item_2_global
    item_2_global = msg

def operators_callback(msg):
    global operators_global
    operators_global = msg

def calc():
    if operators_global.data == "+":
        res = item_1_global.data + item_2_global.data
        rospy.loginfo("(%s) %s (%s) = %s"%(str(item_1_global.data),operators_global.data,str(item_2_global.data),str(res)))

    elif operators_global.data == "-":
        res = item_1_global.data - item_2_global.data
        rospy.loginfo("(%s) %s (%s) = %s"%(str(item_1_global.data),operators_global.data,str(item_2_global.data),str(res)))

    elif operators_global.data == "*":
        res = item_1_global.data * item_2_global.data
        rospy.loginfo("(%s) %s (%s) = %s"%(str(item_1_global.data),operators_global.data,str(item_2_global.data),str(res)))

    else: #operators_global.data == "/":
        if item_2_global.data != 0:
            res = float(item_1_global.data) / float(item_2_global.data)
            rospy.loginfo("(%s) %s (%s) = %s"%(str(item_1_global.data),operators_global.data,str(item_2_global.data),str(res)))

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
