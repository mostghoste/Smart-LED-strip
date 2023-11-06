from flask import Flask, request, jsonify
from gpiozero import LED
app = Flask(__name__)
led = LED(15)

@app.route('/process/<int:number>', methods=['GET'])
def process_number(number):
   if number == 1:
      led.on()
      print("LED turned ON")
   elif number == 2:
      led.off()
      print("LED turned OFF")
   elif number == 3:
      print("Number is Three")
   else:
      return jsonify(status='error', message='Number out of range'), 400
   return jsonify(status='OK')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
