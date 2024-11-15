# subscriber_node.py
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json

class ChairArrangementSubscriber(Node):
    def __init__(self):
        super().__init__('chair_arrangement_subscriber')
        self.subscription = self.create_subscription(
            String,
            'chair_arrangement_command',
            self.listener_callback,
            10
        )
        self.subscription  # 変数を保持して購読が続くようにします

    def listener_callback(self, msg):
        # メッセージをJSON形式でデコード
        data = json.loads(msg.data)
        num_people = data.get('numberOfPeople')
        pattern = data.get('pattern')
        
        # 受信した人数と配置パターンを表示（または他の処理に利用）
        self.get_logger().info(f'受信した人数: {num_people}, 配置パターン: {pattern}')
        
        # ロボットにデータを基に指令を実行させるコードをここに記述
        # 例: ロボットの移動制御、モーターのアクチュエーションなど

def main(args=None):
    rclpy.init(args=args)
    chair_arrangement_subscriber = ChairArrangementSubscriber()

    try:
        rclpy.spin(chair_arrangement_subscriber)
    except KeyboardInterrupt:
        pass
    finally:
        chair_arrangement_subscriber.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
