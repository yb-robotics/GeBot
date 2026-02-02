#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
     
class MoveRobot(Node): 
    def __init__(self):
        super().__init__("move_robot") 
        self.speed= 1.0
        self.duration = 3
        self.start_time = time.time()
        self.publisher_ = self.create_publisher(Twist ,"/cmd_vel" , 10 )
        self.timer_ = self.create_timer(0.5 ,self.callback_move_robot )

    def callback_move_robot(self):
        msg = Twist()
        
        elapsed_time = time.time() - self.start_time
        if elapsed_time < self.duration:
            msg.linear.x = self.speed
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.publisher_.publish(msg)
            self.get_logger().info(f"robot has completed {self.duration} at speed {self.speed} ")
            self.timer_.cancel()
            return

        self.publisher_.publish(msg)             

def main(args=None):
    rclpy.init(args=args)
    node = MoveRobot() 
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
        main()