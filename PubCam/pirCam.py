from Pubnub import Pubnub

from iotconnector import iotbridge
from detector import Detector
import RPi.GPIO as GPIO
import time
import picamera
import sys, os
import json,httplib
import base64

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()


pi = iotbridge(publish_key = 'demo', subscribe_key = 'demo', uuid = 'PI')
cam = picamera.PiCamera()

startT = time.time()
count = 0

channel = 'iotchannel'
message = "hello from pi"
 


def callbackfn(m, n):
  print(m)

def is_person(image):
  det = Detector(image)
  if len(det.face()) or len(det.upper_body()) or len(det.pedestrian()):
    return True
  return False


try:
  cam.start_preview()
  cam.preview_fullscreen = False
  cam.preview_window = (10,10, 320,240)
  while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
      new_state = "HIGH" if current_state else "LOW"
      if current_state:  # new
        cam.start_preview()
        cam.preview_fullscreen = False
        cam.preview_window = (10,10, 320,240)
        print('Motion Detected')
        curTime = (time.strftime("%I:%M:%S"))
        imgFile = curTime + '.jpg'
        for i in range(3):
          cam.capture(imgFile, resize=(320,240))
          if is_person(imgFile):
            print "True"
            with open(imgFile, "rb") as image_file:
              encoded_string = base64.b64encode(image_file.read())
        
            connection.request('POST', '/1/classes/Selfie', json.dumps({
                "fileData": encoded_string,
                "fileName": curTime,
            }), {
                "X-Parse-Application-Id": "S7cS6MQyMb7eMjWRWsC32owq9cDx0zyrM58MSevK",
                "X-Parse-REST-API-Key": "RghYdl6Z2Pqpl2KjIqacZE6AoRn4csLM02e6j6ZH",
                "Content-Type": "application/json"
            })
            result = json.loads(connection.getresponse().read())
            print(result)
            pi.send(channel, curTime)
            os.remove(imgFile)
            break
          else: # Not a person
            os.remove(imgFile)
            print "False"
      else:
          cam.stop_preview()

except KeyboardInterrupt:
  cam.stop_preview()
  sys.exit(0)

