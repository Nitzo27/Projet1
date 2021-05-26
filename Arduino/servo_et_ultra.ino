
#include <ros.h>
#include <ros/time.h>
#include <std_msgs/Float32.h>

#include <std_msgs/String.h>
#include <Servo.h>

Servo myservo; 
ros::NodeHandle  camera;

ros::NodeHandle ultratfmini;

std_msgs :: Float32 ultra_msg;
ros::Publisher ultra_publisher("/ultra", &ultra_msg);
int pingPin=7;

void messageCb( const std_msgs::String& my_msg){
 
 if(my_msg.data[0] == '1'  )  //check 1st letter of the string
   myservo.write(10); 
   if(my_msg.data[0] == '2')
   myservo.write(20); 
   if(my_msg.data[0] == '3')
   myservo.write(30); 
   if(my_msg.data[0] == '4')
   myservo.write(50); 
   if(my_msg.data[0] == '5')
   myservo.write(60); 
   if(my_msg.data[0] == '6' )
   myservo.write(70); 
   if(my_msg.data[0] == '7')
   myservo.write(80); 
  if(my_msg.data[0] == '8')
    myservo.write(90);

     else
digitalWrite(13,LOW);

}
ros::Subscriber<std_msgs::String> sub("myTopic", &messageCb );

void setup() {

   myservo.attach(9); // attaches the servo on pin 9 to the servo object
   ultratfmini.initNode();
   ultratfmini.subscribe(sub);
  // put your setup code here, to run once:

}

void loop() {
  
  float duration, cm;
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW); 
  pinMode(pingPin, INPUT);
  duration = pulseIn(pingPin, HIGH);
  float distanceU = duration / 29 /2 ;
  delay(50);
  
  // put your main code here, to run repeatedly:
ultra_msg.data = distanceU;
ultra_publisher.publish(&ultra_msg);

ultratfmini.spinOnce();
camera.spinOnce();
delay(15); 

}
