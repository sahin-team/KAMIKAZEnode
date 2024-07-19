import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class ControlCommand(Node):

    def __init__(self):
        super().__init__('controler')
        self.subscription = self.create_subscription(
            String,
            'control_command',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning
        self.get_logger().info("control command Subscriber Initialized")

    def listener_callback(self, msg):
        control_data = json.loads(msg.data)  # Deserialize the JSON data
        self.get_logger().info(f"Received telemetry data: {control_data}")

def main(args=None):
    rclpy.init(args=args)
    node = ControlCommand()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()