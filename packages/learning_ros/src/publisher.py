#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

def move_turtle_square():
    rospy.init_node('move_turtle_square', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz, adjust as needed

    time.sleep(1)  # Wait for a moment to let the other nodes start

    # Create a Twist message for moving forward
    forward_msg = Twist()
    forward_msg.linear.x = 2.0  # Linear velocity in m/s

    # Create a Twist message for turning
    turn_msg = Twist()
    turn_msg.angular.z = 1.5708  # Angular velocity in rad/s (approximately 90 degrees)

    for _ in range(4):
        # Move forward for 2 units
        distance_moved = 0
        while distance_moved < 2.0:
            velocity_publisher.publish(forward_msg)
            rate.sleep()
            distance_moved += forward_msg.linear.x / rate.hz

        # Stop the turtle
        velocity_publisher.publish(Twist())

        # Turn 90 degrees
        start_time = rospy.Time.now().to_sec()
        while rospy.Time.now().to_sec() - start_time < 1.0:  # Turn for 1 second
            velocity_publisher.publish(turn_msg)
            rate.sleep()

        # Stop the turtle
        velocity_publisher.publish(Twist())

    rospy.spin()

if __name__ == '__main__':
    try:
        move_turtle_square()
    except rospy.ROSInterruptException:
        pass

