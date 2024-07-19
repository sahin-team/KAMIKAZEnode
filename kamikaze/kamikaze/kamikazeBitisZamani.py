import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class kamikazeBitisZamani(Node):

    def __init__(self):
        super().__init__('kamikaze_end')
        self.publisher_ = self.create_publisher(String, 'kamikaze_completed', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info("Kamikaze Mission Successful")

    def timer_callback(self):
        kamikaze_news = [
            'END',
            {
            'saat': 11,
            'dakika': 50,
            'saniye': 59,
            'milisaniye': 361,
            }
        ]
        msg = String()
        msg.data = json.dumps(kamikaze_news)  # Serialize the data to JSON
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.timer.cancel()  # Cancel the timer to stop further callbacks

def main(args=None):
    rclpy.init(args=args)
    node = kamikazeBitisZamani()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
