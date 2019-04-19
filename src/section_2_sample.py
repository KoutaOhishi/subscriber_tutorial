#! /usr/bin/env python
# coding:utf-8
import rospy
from subscriber_tutorial.msg import Formula

def callback(msg):
    if msg.operators == "+":
        res = msg.item_1 + msg.item_2
        rospy.loginfo("(%s) %s (%s) = %s"%(str(msg.item_1),msg.operators,str(msg.item_2),str(res)))

    elif msg.operators == "-":
        res = msg.item_1 - msg.item_2
        rospy.loginfo("(%s) %s (%s) = %s"%(str(msg.item_1),msg.operators,str(msg.item_2),str(res)))

    elif msg.operators == "*":
        res = msg.item_1 * msg.item_2
        rospy.loginfo("(%s) %s (%s) = %s"%(str(msg.item_1),msg.operators,str(msg.item_2),str(res)))

    else: #msg.operators == "/":
        res = float(msg.item_1) / float(msg.item_2)
        rospy.loginfo("(%s) %s (%s) = %s"%(str(msg.item_1),msg.operators,str(msg.item_2),str(res)))

if __name__ == "__main__":
    rospy.init_node("formula_subscriber")

    sub = rospy.Subscriber("subscriber_tutorial/formula", Formula, callback)

    rospy.spin()
