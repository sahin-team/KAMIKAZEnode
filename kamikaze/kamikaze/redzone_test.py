import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class RedZoneTest(Node):

    def __init__(self):
        super().__init__('redzonetest')
        self.publisher_ = self.create_publisher(String, 'qr_target', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info("Red zone data publisher started.")

    def timer_callback(self):
        redzone_data = [  
            {     
                'id': 0,
                'hssEnlem': 40.23260922,
                'hssBoylam': 29.00573015,
                'hssYaricap': 50,
            },
            {
                'id': 1,
                'hssEnlem': 40.23351019,
                'hssBoylam': 28.99976492,
                'hssYaricap': 50,
            },
            {
                'id': 2,
                'hssEnlem': 40.23105297,
                'hssBoylam': 29.00744677,
                'hssYaricap': 75,
            },
            {
                'id': 3,
                'hssEnlem': 40.23090554,
                'hssBoylam': 29.00221109,
                'hssYaricap': 150,
            },
        ]
        msg = String()
        msg.data = json.dumps(redzone_data)  # Serialize the data to JSON
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = RedZoneTest()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()