import can

def send_can_message(frequency, duration):
    # CAN 인터페이스 설정
    bus = can.interface.Bus(channel='can0', bustype='socketcan')

    # CAN 메시지 생성 (여기서는 주파수와 지속 시간 데이터 포함)
    message = can.Message(arbitration_id=0x123, data=[frequency, duration], is_extended_id=False)
    
    try:
        # CAN 메시지 전송
        bus.send(message)
        print(f"Sent CAN message: Frequency={frequency}Hz, Duration={duration}s")
    except can.CanError:
        print("Error sending CAN message.")
