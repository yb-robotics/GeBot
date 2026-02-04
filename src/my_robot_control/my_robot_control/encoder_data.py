#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from math import sqrt
     
     
class EncoderData(Node): 
    def __init__(self):
        super().__init__("encoder_data") 
        self.start_x = None
        self.start_y = None

        self.subscriptions_ = self.create_subscription(Odometry , "/odom" , self.callback_odom, 10)

    def callback_odom(self,msg):

        x = msg.pose.pose.position.x 
        y = msg.pose.pose.position.y
        # q = msg.pose.pose.orientation 

        # linear_x =msg.twist.twist.linear.x
        # angular_z =msg.twist.twist.angular.z

        if self.start_x is None:
            self.start_x = x 
            self.start_y = y
            self.get_logger().info("Start position recorded")
            return

        distance = sqrt((x - self.start_x)**2 + (y - self.start_y)**2)
        self.get_logger().info(f"so my robot moved {distance}")
     
     
def main(args=None):
    rclpy.init(args=args)
    node = EncoderData() 
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
        main()