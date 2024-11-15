# app.py
from flask import Flask, request, jsonify, render_template
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

app = Flask(__name__)

# ROS2 ノードの初期化
class ChairArrangementPublisher(Node):
    def __init__(self):
        super().__init__('chair_arrangement_publisher')
        self.publisher_ = self.create_publisher(String, 'chair_arrangement_topic', 10)

    def publish_command(self, num_people, pattern):
        msg = String()
        msg.data = f"人数: {num_people}, 配置パターン: {pattern}"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

# Flask アプリケーションの起動時に ROS2 ノードを初期化
rclpy.init()
chair_arrangement_publisher = ChairArrangementPublisher()

@app.route('/')
def index():
    return render_template('index.html')  # index.htmlを表示する

@app.route('/api/send_command', methods=['POST'])
def send_command():
    data = request.json
    num_people = data.get('numberOfPeople')
    pattern = data.get('pattern')

    # ROS2 トピックにデータをパブリッシュ
    chair_arrangement_publisher.publish_command(num_people, pattern)

    print(f"人数: {num_people}, 配置パターン: {pattern}")
    return jsonify({'status': 'success', 'message': '指令が送信されました！'})

# Flask アプリケーションの終了時に ROS2 ノードをシャットダウン
@app.before_first_request
def shutdown_ros2():
    import atexit
    atexit.register(rclpy.shutdown)

if __name__ == '__main__':
    app.run(debug=True)
