import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class Coordinate(Node):

    def __init__(self):
        super().__init__('coordinate')
        self.publisher_ = self.create_publisher(String, 'control_command', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info("Coordinate Orders Node has been started.")

    def timer_callback(self):
        coordinate_data = {       
            "iha_enlem":  41.508775,
            "iha_boylam": 36.118335,
            "iha_irtifa": 38,
            "iha_hiz":    28,
        }
        msg = String()
        msg.data = json.dumps(coordinate_data)  # Serialize the data to JSON
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = Coordinate()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()