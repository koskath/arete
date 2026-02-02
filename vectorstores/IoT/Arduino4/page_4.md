<a id='213d08c8-2012-4e1a-b377-b2f153be1de8'></a>

12/4/25, 2:51 PM

<a id='3fcb5d0e-38c7-464f-9822-cb1f1ca1ddff'></a>

Arduino_MKRENV | Arduino Documentation

<a id='fb4c23b0-d48b-42a6-91b2-1e0285fc237b'></a>

ARDUINODOCS

<a id='be7ffb32-94ed-43da-ba1f-ad6cbf2dd25c'></a>

```
1 Serial.print("Temperature = ");
2 Serial.print(ENV.readTemperatur
3 Serial.println(" C");
```

<a id='cdb26587-aac6-4be5-a28c-1a37920f8254'></a>

## See also

begin()

end()

readHumidity()

readPressure()

readIlluminance()

readUVA()

readUVB()

readUVIndex()

<a id='d17dca78-4e56-4fd6-9c7f-45e106752136'></a>

readHumidity()

Read the HTS221 sensor's relative humidity
(rH), and returns it as a percentage. Read
more about relative humidity in this article.

<a id='527f440c-90f6-4acc-830f-8f605b06ba3c'></a>

# Syntax

```
1 ENV.readHumidity()
```

<a id='726fa45a-645e-4145-b671-3fb32697f580'></a>

Parameters

None.

<a id='0d1f4fe7-52c4-45ae-97ed-4ecddffca264'></a>

## Returns

Returns the relative humidity (rH) in percentage.

<a id='24473f61-20a1-42dd-91b9-3c52541ad402'></a>

# Example

```
Serial.print("Humidity     = ");
Serial.print(ENV.readHumidity());
Serial.println(" %");
```

<a id='aaec5b20-25e8-405d-b90b-cb511554ca3b'></a>

See also

begin()

<a id='9597ac38-da8d-449f-9efe-a65908b62440'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='42d48612-14ed-4003-bb92-618e54741afd'></a>

4/10