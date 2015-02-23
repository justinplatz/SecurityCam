from Pubnub import Pubnub

from iotconnector import iotbridge
import RPi.GPIO as GPIO
import time
import picamera
import sys
import json,httplib
import base64
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()



pi = iotbridge(publish_key = 'demo', subscribe_key = 'demo', uuid = 'PI')
camera = picamera.PiCamera()

startT = time.time()
count = 0

channel = 'iotchannel'
message = "hello from pi"
 


def callbackfn(m, n):
  print(m)
 
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	camera.start_preview()
	camera.preview_fullscreen = False
	camera.preview_window = (10,10, 320,240)
	while True:
                if count == 10:
                  break
	        input_state = GPIO.input(18)
	        if input_state == False:
	            print('Button Pressed')
	            curTime = (time.strftime("%I:%M:%S"))
		    camera.capture(curTime + '.jpg', resize=(320,240))
                    with open(curTime + '.jpg', "rb") as image_file:
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

                    count += 1
                    pi.send(channel, curTime)
                    #pi.connect(channel, callbackfn)

except KeyboardInterrupt:
        camera.stop_preview()
	sys.exit(0)



