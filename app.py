from flask import Flask, request, jsonify
import gpio
app = Flask(__name__)

@app.route('/process/<int:number>', methods=['GET'])
def process_number(number):
   if number == 1:
      gpio.turn_on()
      print("LED turned ON")
   elif number == 2:
      gpio.turn_off()
      print("LED turned OFF")
   elif number == 3:
      print("Number is Three")
   else:
      return jsonify(status='error', message='Number out of range'), 400
   return jsonify(status='OK')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
