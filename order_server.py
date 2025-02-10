from flask import Flask, render_template, request, jsonify
import paho.mqtt.client as mqtt

app = Flask(__name__)

# MQTT 설정 (라즈베리파이 IP 입력)

MQTT_BROKER = "172.30.1.58"  # 또는 실제 Raspberry Pi의 IP 주소

MQTT_TOPIC = "order"

#client = mqtt.Client()

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, protocol=mqtt.MQTTv5)
client.connect(MQTT_BROKER, 1883, 60)

@app.route("/")
def home():
    return render_template("order.html")  # templates/order.html을 로드

@app.route("/order", methods=["POST"])
def order():
    data = request.json  # JSON 데이터 받기
    print(f"📦 주문 접수: {data}")

    # MQTT로 주문 정보 전송
    client.publish(MQTT_TOPIC, str(data))

    return jsonify({"message": "주문이 성공적으로 접수되었습니다!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
