<a id='5ed32cee-630a-47c6-a282-a38f3309974a'></a>

12/4/25, 2:51 PM

<a id='d91c4cc9-d89a-480f-a86d-e025567ee208'></a>

Arduino_MKRENV | Arduino Documentation

<a id='a7d5e315-83d6-437e-8355-d27f62957d97'></a>

ARDUINODOCS

<a id='a9e19fb7-adcc-4c4b-94cc-061dcffc7613'></a>



<a id='84023407-79e6-42f3-a569-bef0267be1db'></a>

```
1 Serial.print("UVB = ");
2 Serial.println(ENV.readUVB());
```

<a id='7533eeb4-e67c-41eb-9ea3-4a7be7cb8357'></a>

## See also

* begin()
* end()
* readTemperature()
* readHumidity()
* readPressure()
* readIlluminance()
* readUVA()
* readUVIndex()

<a id='deb633a8-1487-4716-bd7f-7f6fbca1464e'></a>

readUVIndex()
  Read the UV sensor's UV index value.

<a id='cb8431ce-c110-47ab-8f28-a2c1fff0c955'></a>

## Syntax

```
1 ENV.readUVIndex()
```

<a id='d0a31388-bd96-416c-a712-72b36fd50ff1'></a>

**Parameters**

None.

<a id='871e1c43-125e-46eb-9b41-40b3ea0b056c'></a>

Returns

The UV sensor's UV index value.

<a id='054c00fb-dfa3-4ca9-a2d6-72523cbbd6f4'></a>

Example

```
1 Serial.print("UV Index = ");
2 Serial.println(ENV.readUVIndex(
```

<a id='6d3e0516-f68c-467a-8925-19ca3b0d2433'></a>

**See also**

begin()
end()
readTemperature()
readHumidity()
readPressure()

<a id='2025cc46-f6eb-4e11-aafc-db2da76e2c65'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='1b2d5d8b-dfc5-4371-aa9f-af95fb0f57b9'></a>

8/10