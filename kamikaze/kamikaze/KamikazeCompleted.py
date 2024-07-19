import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class KamikazeCompleted(Node):

    def __init__(self):
        super().__init__('kamikazenews')
        self.subscription = self.create_subscription(
            String,
            'kamikaze_completed',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning
        self.get_logger().info("mission news:")

    def listener_callback(self, msg):
        kamikaze_news = json.loads(msg.data)  # Deserialize the JSON data
        self.get_logger().info(f"Received telemetry data: {kamikaze_news}")

def main(args=None):
    rclpy.init(args=args)
    node = KamikazeCompleted()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()