import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class QRCoordinate(Node):

    def __init__(self):
        super().__init__('QRcoordinate')
        self.subscription = self.create_subscription(
            String,
            'qr_target',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning
        self.get_logger().info("QR Coordinate Subscriber Initialized")

    def listener_callback(self, msg):
        qr_data = json.loads(msg.data)  # Deserialize the JSON data
        self.get_logger().info(f"Received QR data: {qr_data}")

def main(args=None):
    rclpy.init(args=args)
    node = QRCoordinate()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()