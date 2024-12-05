import time
import threading
import gpioBuzzer
import IPC_Library

# 사용하려는 GPIO 핀 번호
gpio_pin = 89

def ipc_listener():
    """CAN 통신을 통해 수신한 메시지를 처리하는 함수"""
    while True:
        try:
            if IPC_Library.received_pucData:
                print("Received data:", IPC_Library.received_pucData)
                if IPC_Library.received_pucData[0] == 1:
                    print("Playing C")
                    gpioBuzzer.play_tone(gpio_pin, 261.63, 0.5)
                elif IPC_Library.received_pucData[0] == 2:
                    print("Playing D")
                    gpioBuzzer.play_tone(gpio_pin, 293.66, 0.5)
                else:
                    print("No relevant data received.")
            else:
                print("No data received.")
            time.sleep(0.1)
        except Exception as e:
            print(f"Error in IPC listener: {e}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        # IPC 통신을 위한 쓰레드 실행
        ipc_thread = threading.Thread(target=ipc_listener)
        ipc_thread.daemon = True
        ipc_thread.start()

        # GPIO 초기화
        gpioBuzzer.export_gpio(gpio_pin)
        gpioBuzzer.set_gpio_direction(gpio_pin, "out")

        # 메인 루프 - CAN 메시지를 계속 기다리며 처리
        while True:
            pass  # 지속적으로 IPC 데이터를 처리합니다.

    except KeyboardInterrupt:
        print("\nProgram interrupted")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        gpioBuzzer.unexport_gpio(gpio_pin)
