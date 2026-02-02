<a id='df1b962b-395c-4731-9439-60da4eb4226e'></a>

7/23/22, 9:09 PM

<a id='52419da6-0e26-44a7-b6c5-f6fc8378a735'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='7ebce823-d715-4e1e-b4b7-bdbef6d57eb2'></a>

71 Serial.print(", ");
72 Serial.print(y);
73 Serial.print(",");
74 Serial.print(z);
75 Serial.println(" uT");
76
77 // roll/pitch in radian
78 roll = atan2((float)acc_y, (float)acc_z);
79 pitch = atan2(-(float)acc_x, sqrt((float)acc_y*acc_
80 Serial.print("Roll: ");
81 Serial.println(roll*57.3);
82 Serial.print("Pitch: ");
83 Serial.println(pitch*57.3);
84
85 double Xheading = x * cos(pitch) + y * sin(roll) *
86 double Yheading = y * cos(roll) - z * sin(pitch);
87
88
89 double heading = 180 + 57.3*atan2(Yheading, Xheadin;
90
91 Serial.print("Heading: ");
92 Serial.println(heading);
93 Serial.println("---------------------------------");
94
95 delay(500);
96
97 }
98
99 void calibrate(uint32_t timeout, int32_t *offsetx, int3
100 {
101 int32_t value_x_min = 0;
102 int32_t value_x_max = 0;
103 int32_t value_y_min = 0;
104 int32_t value_y_max = 0;
105 int32_t value_z_min = 0;
106 int32_t value_z_max = 0;
107 uint32_t timeStart = 0;
108
109 ak09918.getData(&x, &y, &z);
110
111 value_x_min = x;

<a id='7a30ecdb-1f33-4133-92a2-2b90729fb6b0'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='124b70c9-16a3-4b89-bd80-9e1adaada8c3'></a>

14/23