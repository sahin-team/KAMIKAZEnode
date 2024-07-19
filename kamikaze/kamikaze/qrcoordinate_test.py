import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class qrcoordinatetest(Node):

    def __init__(self):
        super().__init__('qrcotest')
        self.publisher_ = self.create_publisher(String, 'qr_target', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info("qr coordinate publish started.")

    def timer_callback(self):
        qr_data = {       
            'qrEnlem': 41.51238882,
            'qrBoylam': 36.11935778,
        }
        msg = String()
        msg.data = json.dumps(qr_data)  # Serialize the data to JSON
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = qrcoordinatetest()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()