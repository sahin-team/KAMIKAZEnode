import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class KamikazeNodes(Node):

    def __init__(self):
        super().__init__('kamikaze_nodes')
        
        # Subscribers
        self.control_command_sub = self.create_subscription(
            String,
            'control_command',
            self.control_command_callback,
            10
        )
        
        self.telemetry_sub = self.create_subscription(
            String,
            'telemetry',
            self.telemetry_callback,
            10
        )
        
        self.kamikaze_completed_sub = self.create_subscription(
            String,
            'kamikaze_completed',
            self.kamikaze_completed_callback,
            10
        )
        
        self.qr_target_sub = self.create_subscription(
            String,
            'qr_target',
            self.qr_target_callback,
            10
        )

        # Publishers
        self.control_command_pub = self.create_publisher(String, 'control_command', 10)
        self.kamikaze_completed_pub = self.create_publisher(String, 'kamikaze_completed', 10)
        
        # Timers
        self.coordinate_timer = self.create_timer(1.0, self.publish_coordinate)
        self.orientation_timer = self.create_timer(1.0, self.publish_orientation)
        self.kamikaze_start_timer = self.create_timer(1.0, self.publish_kamikaze_start)
        self.kamikaze_end_timer = self.create_timer(1.0, self.publish_kamikaze_end)
        
        self.get_logger().info("Kamikaze Node has been started.")

    # Callbacks for subscribers
    def control_command_callback(self, msg):
        control_data = json.loads(msg.data)
        self.get_logger().info(f"Received control command data: {control_data}")

    def telemetry_callback(self, msg):
        telemetry_data = json.loads(msg.data)
        self.get_logger().info(f"Received telemetry data: {telemetry_data}")

    def kamikaze_completed_callback(self, msg):
        kamikaze_news = json.loads(msg.data)
        self.get_logger().info(f"Received kamikaze news: {kamikaze_news}")

    def qr_target_callback(self, msg):
        qr_data = json.loads(msg.data)
        self.get_logger().info(f"Received QR data: {qr_data}")

    # Methods for publishing messages
    def publish_coordinate(self):
        coordinate_data = {
            "iha_enlem": 41.508775,
            "iha_boylam": 36.118335,
            "iha_irtifa": 38,
            "iha_hiz": 28,
        }
        msg = String()
        msg.data = json.dumps(coordinate_data)
        self.control_command_pub.publish(msg)
        self.get_logger().info('Publishing Coordinate: "%s"' % msg.data)

    def publish_orientation(self):
        orientation_data = {
            "iha_dikilme": 7,
            "iha_yonelme": 210,
            "iha_yatis": -30,
        }
        msg = String()
        msg.data = json.dumps(orientation_data)
        self.control_command_pub.publish(msg)
        self.get_logger().info('Publishing Orientation: "%s"' % msg.data)

    def publish_kamikaze_start(self):
        kamikaze_start_news = [
            'STARTED',
            {
                'saat': 11,
                'dakika': 44,
                'saniye': 13,
                'milisaniye': 361,
            }
        ]
        msg = String()
        msg.data = json.dumps(kamikaze_start_news)
        self.kamikaze_completed_pub.publish(msg)
        self.get_logger().info('Publishing Kamikaze Start: "%s"' % msg.data)
        self.kamikaze_start_timer.cancel()  # Stop this timer after first publish

    def publish_kamikaze_end(self):
        kamikaze_end_news = [
            'END',
            {
                'saat': 11,
                'dakika': 50,
                'saniye': 59,
                'milisaniye': 361,
            }
        ]
        msg = String()
        msg.data = json.dumps(kamikaze_end_news)
        self.kamikaze_completed_pub.publish(msg)
        self.get_logger().info('Publishing Kamikaze End: "%s"' % msg.data)
        self.kamikaze_end_timer.cancel()  # Stop this timer after first publish

def main(args=None):
    rclpy.init(args=args)
    node = KamikazeNodes()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
