<a id='26b1f43c-689a-4fd4-a602-f27413235f9e'></a>

7/23/22, 9:09 PM

<a id='3c443e11-edc1-42c1-8848-491674973200'></a>

Grove - IMU 9DOF(Icm20600+AK09918) - Seeed Wiki

<a id='f75489af-c881-43c3-8be1-997bfefa4962'></a>

```
}

/* Update z-Axis max/min value */
if(value_z_min > z)
{
  value_z_min = z;
  // Serial.print("Update value_z_min: ");
  // Serial.println(value_z_min);
}
else if(value_z_max < z)
{
  value_z_max = z;
  // Serial.print("update value_z_max: ");
  // Serial.println(value_z_max);
}

Serial.print(".");
delay(100);
}

*offsetx = value_x_min + (value_x_max - value_x_min)/
*offsety = value_y_min + (value_y_max - value_y_min)/
*offsetz = value_z_min + (value_z_max - value_z_min)/
}
```

<a id='00bc67e8-ff0e-484e-a87a-c98aa1b82dc1'></a>

## Note
There are 3 demos in the library:

**test_6axis**
> This example shows how to get gyroscope and acceleration data from ICM20600.

**test_magnet**
> This example shows how to get magnetic data from AK09918.

**compass**

<a id='b91c25a2-31a5-483b-86ff-ca03931c7b78'></a>

https://wiki.seeedstudio.com/Grove-IMU_9DOF-Icm20600%2BAK09918/

<a id='a7906553-7bb7-4326-a1da-3b1d72f06854'></a>

16/23