from flask import Flask, request, jsonify
from gpiozero import LED
from rpi_rf import RFDevice

app = Flask(__name__)
led = LED(15)
transmitter = RFDevice(14)

def send_signal(code):
    transmitter.tx_code(code, 1, 350)
    print(f'Signal {code} sent!')

@app.route('/process/<int:number>', methods=['GET'])
def process_number(number):
   if number == 1:
      led.on()
      send_signal(10)
      print("LED turned ON")
   elif number == 2:
      led.off()
      send_signal(20)
      print("LED turned OFF")
   elif number == 3:
      print("Number is Three")
   else:
      return jsonify(status='error', message='Number out of range'), 400
   return jsonify(status='OK')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    transmitter.enable_tx()
