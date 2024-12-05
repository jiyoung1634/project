import can
import time
from gpioBuzzer import play_tone

def receive_can_message():
    # CAN 인터페이스 설정
    bus = can.interface.Bus(channel='can0', bustype='socketcan')  # 'can0'은 예시로, 실제 환경에 맞게 수정

    while True:
        # CAN 메시지 수신
        message = bus.recv()
        if message:
            # 메시지에서 주파수와 지속 시간을 추출 (예: 데이터 첫 번째, 두 번째 바이트)
            frequency = int(message.data[0])  # 첫 번째 데이터: 주파수
            duration = int(message.data[1])   # 두 번째 데이터: 지속 시간

            # 추출된 값을 이용해 버저 소리 재생
            print(f"Received CAN message: Frequency={frequency}Hz, Duration={duration}s")
            play_tone(17, frequency, duration)  # GPIO 17에서 톤 재생

if __name__ == "__main__":
    print("Starting CAN message reception...")
    receive_can_message()
