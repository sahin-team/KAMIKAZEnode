import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class data(Node):

    def __init__(self):
        super().__init__('data')
        self.subscription = self.create_subscription(
            String,
            'telemetry',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning
        self.get_logger().info("Telemetry Subscriber Initialized")

    def listener_callback(self, msg):
        telemetry_data = json.loads(msg.data)  # Deserialize the JSON data
        self.get_logger().info(f"Received telemetry data: {telemetry_data}")

def main(args=None):
    rclpy.init(args=args)
    node = data()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()