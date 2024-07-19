import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class Orientation(Node):

    def __init__(self):
        super().__init__('orientation')
        self.publisher_ = self.create_publisher(String, 'control_command', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info("Orientation Orders Node has been started.")

    def timer_callback(self):
        orientation_data = {
            "iha_dikilme": 7,
            "iha_yonelme": 210,
            "iha_yatis": -30,
        }
        msg = String()
        msg.data = json.dumps(orientation_data)  # Serialize the data to JSON
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = Orientation()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()