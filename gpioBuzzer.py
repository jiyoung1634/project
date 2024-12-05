import time
import os

# GPIO 관련 경로 설정
GPIO_EXPORT_PATH = "/sys/class/gpio/export"
GPIO_UNEXPORT_PATH = "/sys/class/gpio/unexport"
GPIO_DIRECTION_PATH_TEMPLATE = "/sys/class/gpio/gpio{}/direction"
GPIO_VALUE_PATH_TEMPLATE = "/sys/class/gpio/gpio{}/value"

def export_gpio(gpio_number):
    """GPIO를 export하는 함수"""
    try:
        print(f"Exporting GPIO {gpio_number}...")  # Debugging print
        with open(GPIO_EXPORT_PATH, 'w') as export_file:
            export_file.write(str(gpio_number))
        print(f"GPIO {gpio_number} exported successfully.")
    except IOError as e:
        print(f"Error exporting GPIO {gpio_number}: {e}")

def unexport_gpio(gpio_number):
    """GPIO를 unexport하는 함수"""
    try:
        print(f"Unexporting GPIO {gpio_number}...")  # Debugging print
        with open(GPIO_UNEXPORT_PATH, 'w') as unexport_file:
            unexport_file.write(str(gpio_number))
        print(f"GPIO {gpio_number} unexported successfully.")
    except IOError as e:
        print(f"Error unexporting GPIO {gpio_number}: {e}")

def set_gpio_direction(gpio_number, direction):
    """GPIO 방향 설정"""
    gpio_direction_path = GPIO_DIRECTION_PATH_TEMPLATE.format(gpio_number)
    try:
        print(f"Setting GPIO {gpio_number} direction to {direction}...")  # Debugging print
        with open(gpio_direction_path, 'w') as direction_file:
            direction_file.write(direction)
        print(f"GPIO {gpio_number} direction set to {direction}.")
    except IOError as e:
        print(f"Error setting GPIO {gpio_number} direction: {e}")

def set_gpio_value(gpio_number, value):
    """GPIO 값 설정"""
    gpio_value_path = GPIO_VALUE_PATH_TEMPLATE.format(gpio_number)
    try:
        print(f"Setting GPIO {gpio_number} value to {value}...")  # Debugging print
        with open(gpio_value_path, 'w') as value_file:
            value_file.write(str(value))
        print(f"GPIO {gpio_number} value set to {value}.")
    except IOError as e:
        print(f"Error setting GPIO {gpio_number} value: {e}")

def play_tone(gpio_number, frequency, duration):
    """버저에 주파수에 맞는 톤을 울리는 함수"""
    print(f"Starting to play tone on GPIO {gpio_number} with frequency {frequency} Hz for {duration} seconds...")  # Debugging print
    period = 1.0 / frequency
    half_period = period / 2
    end_time = time.time() + duration
    while time.time() < end_time:
        print("Playing tone...")  # Debugging print
        set_gpio_value(gpio_number, 1)
        time.sleep(half_period)
        set_gpio_value(gpio_number, 0)
        time.sleep(half_period)
    print("Tone finished.")  # Debugging print

# 메인 코드 실행 예시
if __name__ == "__main__":
    gpio_pin = 17  # 예시 GPIO 핀 번호
    frequency = 1000  # 1kHz 주파수
    duration = 5  # 5초 동안 재생

    print("Starting GPIO setup...")
    export_gpio(gpio_pin)
    set_gpio_direction(gpio_pin, "out")
    play_tone(gpio_pin, frequency, duration)
    unexport_gpio(gpio_pin)
    print("GPIO cleanup completed.")
