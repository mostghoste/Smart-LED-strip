import time
import threading
from rpi_rf import RFDevice

rf_tx = RFDevice(17)  # Assume transmitter is connected to GPIO 17
rf_rx = RFDevice(27)  # Assume receiver is connected to GPIO 27

def send_signal(code):
    rf_tx.tx_code(code, 1, 350)
    print(f'Signal {code} sent')

def receive_signal():
    timestamp = None
    rf_rx.enable_rx()
    print("Listening")
    while True:
        if rf_rx.rx_code_timestamp != timestamp:
            timestamp = rf_rx.rx_code_timestamp
            print(f"{rf_rx.rx_code} [pulselength {rf_rx.rx_pulselength}, protocol {rf_rx.rx_proto}]")
        time.sleep(0.01)

if __name__ == '__main__':
    try:
        listener_thread = threading.Thread(target=receive_signal)
        listener_thread.start()
        rf_tx.enable_tx()
        send_signal(12345)  # Send a code
    finally:
        rf_tx.cleanup()
        rf_rx.cleanup()
