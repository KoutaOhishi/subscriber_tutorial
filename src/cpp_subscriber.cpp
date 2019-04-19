#include "ros/ros.h"
#include "std_msgs/Int32.h"
#include "std_msgs/String.h"
#include "subscriber_tutorial/Formula.h"

void Callback(const subscriber_tutorial::Formula::ConstPtr &msg)
{
  //printf("%d\n", msg->item_1);
  if (msg->operators == "+"){
    int res = msg->item_1 + msg->item_2;
    printf("%d\n", res);
  }

  else if (msg->operators == "-"){
    int res = msg->item_1 - msg->item_2;
    printf("%d\n", res);
  }

  else if (msg->operators == "*"){
    int res = msg->item_1 * msg->item_2;
    printf("%d\n", res);
  }

  else{
    float res = msg->item_1 / msg->item_2;
    printf("%f\n", res);
  }



}

int main(int argc, char **argv){
  ros::init(argc, argv, "cpp_subscriber");
  ros::NodeHandle nh;
  ros::Subscriber sub = nh.subscribe("subscriber_tutorial/formula", 1, Callback);

  ros::spin();

  return 0;

}
