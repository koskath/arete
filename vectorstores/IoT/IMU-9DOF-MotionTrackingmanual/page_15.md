<a id='9d0887e9-b4b4-42b4-bb24-5a21fb6265f2'></a>

7/23/22, 9:09 PM

<a id='2da66da1-4e43-45f2-9e37-6130fbc7c364'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='afbdb56b-6d93-4771-b73a-7b425ead4e35'></a>

```c
112 value_x_max = x;
113 value_y_min = y;
114 value_y_max = y;
115 value_z_min = z;
116 value_z_max = z;
117 delay(100);
118 
119 timeStart = millis();
120 
121 while((millis() - timeStart) < timeout)
122 {
123 ak09918.getData(&x, &y,&z);
124 
125 /* Update x-Axis max/min value */
126 if(value_x_min > x)
127 {
128 value_x_min = x;
129 // Serial.print("Update value_x_min: ");
130 // Serial.println(value_x_min);
131 
132 }
133 else if(value_x_max < x)
134 {
135 value_x_max = x;
136 // Serial.print("update value_x_max: ");
137 // Serial.println(value_x_max);
138 }
139 
140 /* Update y-Axis max/min value */
141 if(value_y_min > y)
142 {
143 value_y_min = y;
144 // Serial.print("Update value_y_min: ");
145 // Serial.println(value_y_min);
146 
147 }
148 else if(value_y_max < y)
149 {
150 value_y_max = y;
151 // Serial.print("update value_y_max: ");
152 // Serial.println(value_y_max);
```

<a id='258f414a-74ae-4165-a6d5-d6e5d34bfdfc'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='8b2bb639-8296-4bcd-9552-ee25dcb2573c'></a>

15/23