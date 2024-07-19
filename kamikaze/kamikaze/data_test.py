import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class datatest(Node):

    def __init__(self):
        super().__init__('datatest')
        self.publisher_ = self.create_publisher(String, 'telemetry', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info("data publish started.")

    def timer_callback(self):
        telemetry_data = {       
            'iha_enlem': 41.508775,
            'iha_boylam': 36.118335,
            'iha_irtifa': 38,
            'iha_dikilme': 7,
            'iha_yonelme': 210,
            'iha_yatis': -30,
            'iha_hiz': 28,
            'iha_batarya': 50,
            'iha_otonom': 1,
            'saat': 11,
            'dakika': 38,
            'saniye': 37,
            'milisaniye': 654,
        }
        msg = String()
        msg.data = json.dumps(telemetry_data)  # Serialize the data to JSON
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = datatest()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()