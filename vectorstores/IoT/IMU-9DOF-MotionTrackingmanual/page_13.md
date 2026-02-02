<a id='ba4213a7-dda7-453f-88dd-567638871d62'></a>

7/23/22, 9:09 PM

<a id='905ec715-e343-4898-bc60-82aae694b94d'></a>

Grove - IMU 9DOF(lcm20600+AK09918) - Seeed Wiki

<a id='be45e058-0408-4788-a578-61f9f3dc9103'></a>

```cpp
Serial.println("Waiting Sensor");
delay(100);
err = ak09918.isDataReady();
}

Serial.println("Start figure-8 calibration after 2");
delay(2000);
calibrate(10000, &offset_x, &offset_y, &offset_z);
Serial.println("");
}

void loop() {
  // get acceleration
  acc_x = icm20600.getAccelerationX();
  acc_y = icm20600.getAccelerationY();
  acc_z = icm20600.getAccelerationZ();

  Serial.print("A: ");
  Serial.print(acc_x);
  Serial.print(", ");
  Serial.print(acc_y);
  Serial.print(", ");
  Serial.print(acc_z);
  Serial.println(" mg");

  Serial.print("G: ");
  Serial.print(icm20600.getGyroscopeX());
  Serial.print(", ");
  Serial.print(icm20600.getGyroscopeY());
  Serial.print(", ");
  Serial.print(icm20600.getGyroscopeZ());
  Serial.println(" dps");

  ak09918.getData(&x, &y, &z);
  x = x - offset_x;
  y = y - offset_y;
  z = z - offset_z;

  Serial.print("M: ");
  Serial.print(x);
```

<a id='29e13344-a04d-4573-9dbb-9414f98b8535'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-lcm20600%2BAK09918/

<a id='03d7ce34-5ee1-4ae9-85a9-ddf8caa394aa'></a>

13/23