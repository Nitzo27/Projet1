#include <ros.h>
#include <ros/time.h>
#include <std_msgs/Float32.h>
# include <SoftwareSerial.h>   //header file of software serial port

SoftwareSerial Serial1(0,1);

ros::NodeHandle ultratfmini;

std_msgs :: Float32 ultra_msg;
std_msgs::Float32 tfmini_msg;

int pingPin=7;

float distanceT;  //actual distance measurements of LiDAR
int strength; //signal strength of LiDAR
int check;  //save check value
int i;
int uart[9];  //save data measured by LiDAR
const int HEADER=0x59;  //frame header of data package

ros::Publisher ultra_publisher("/ultra", &ultra_msg);
ros::Publisher tfmini_publisher("/tfmini", &tfmini_msg);

void setup() {

  Serial.begin(9600); //set bit rate of serial port connecting Arduino with computer
  Serial1.begin(115200);  //set bit rate of serial port connecting LiDAR with Arduino
  
  // put your setup code here, to run once:
 
ultratfmini.initNode();
ultratfmini.advertise(ultra_publisher);
ultratfmini.advertise(tfmini_publisher);
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
  float distanceU = duration / 29 /2;
  delay(50);


if (Serial1.available()) {  //check if serial port has data input
    if(Serial1.read() == HEADER) {  //assess data package frame header 0x59
      uart[0]=HEADER;
      if (Serial1.read() == HEADER) { //assess data package frame header 0x59
        uart[1] = HEADER ;

        for (i = 2; i < 9; i++) { //save data in array
          uart[i] = Serial1.read();
        }
        check = uart[0] + uart[1] + uart[2] + uart[3] + uart[4] + uart[5] + uart[6] + uart[7];
        if (uart[8] == (check & 0xff)){ //verify the received data as per protocol
          distanceT = uart[2] + uart[3] * 256;     //calculate distance value
          strength = uart[4] + uart[5] * 256; //calculate signal strength value
          
        }
      }
    }
  }




  
  // put your main code here, to run repeatedly:

   ultra_msg.data = distanceU;
   tfmini_msg.data = distanceT;
   ultra_publisher.publish(&ultra_msg);
   tfmini_publisher.publish(&tfmini_msg);
   
 ultratfmini.spinOnce();

}
