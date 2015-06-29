# Create A Realtime Security Camera Using Raspberry Pi, Parse & PubNub

Nowadays an insight is more or less useless if it is out of time. There are so many time-sensitive industries such as financial trading and risk-management systems which require immediate access to data. Changes in market conditions for example, happen far too quickly to rely on old information. One must have access to realtime information to make well-informed decisions. The same logic holds true for home security. Time is the biggest factor in any emergency, but in the case of fire, and break-ins, time is of the essence. A realtime emergency alert could mean the difference between safety and severe danger.

In this blog post I'm going to show you how you can use a Raspberry Pi (with just a few additional parts) to build your very own Security Camera which can detect motion, detect human faces, and alert you if people are detected in real-time by utilizing the PubNub Python & Javascript SDKs. 

##Overview

In order to make our security camera we will be using:

* **Raspberry Pi B+** as our computer board of choice
* **Raspberry Pi Camera Module**  
* **PIR Sensor** to detect motion
* **Parse** to store our photos
* **OpenCV** to enable accurate facial detection of photos 
* **PubNub** to facilitate realtime communication between our RPi and Web Console


The high-level process of the security camera is that the PIR sensor will detect motion and tells the camera module snap a photo. We use OpenCV to decide if that photo did in fact contain a person; if the algorithm does detect a person in the photo then we store the photo in our Parse database; else, delete the photo. Last, we use PubNub to publish an alert in realtime to our web console. 

(For fun we decided to overlay any facial detections with face cutouts of super heroes and celebrities, this part of the tutorial is definitely not useful as a security feature, however I would recommended it for a good laugh.)
