import threading
import time

# IPC 통신 관련 변수
received_pucData = None

def receive_data():
    """가상의 CAN 데이터 수신 함수"""
    global received_pucData
    while True:
        # 여기서 실제 CAN 통신을 처리하는 부분을 구현합니다.
        # 예시로 특정 데이터를 수신했다고 가정
        time.sleep(2)  # 2초 간격으로 데이터 수신
        received_pucData = [1]  # 예시로 데이터 '1' 수신
        print("Received data:", received_pucData)
        time.sleep(0.1)

def start_ipc_listener():
    """IPC 통신 리스너 시작"""
    ipc_thread = threading.Thread(target=receive_data)
    ipc_thread.daemon = True  # 메인 프로그램 종료 시 자동 종료
    ipc_thread.start()
