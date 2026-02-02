<a id='85e18ac0-bb68-4075-9287-742643ddd1a4'></a>

12/4/25, 2:51 PM

<a id='ed801c92-4afa-4c4a-a817-8664660711d6'></a>

Arduino_MKRGPS | Arduino Documentation

<a id='59379fbc-837c-47fe-95ce-c3aee626e64d'></a>

ARDUINODOCS

<a id='316897da-a504-471c-adf7-5d82d9a7d7a9'></a>

[ ]

<a id='03f6e762-64e6-43be-85af-50d3c491935f'></a>

1 GPS.variation()

<a id='bc175c83-65d3-476c-aa2c-1c9e5a0f5a0c'></a>

## Parameters

None.

<a id='96d98cff-2961-4039-9b34-aa2bad2bca0c'></a>

## Returns

GPS magnetic variation in degrees.

<a id='f8c9cbf6-dd18-4952-a176-f44bd380fa1d'></a>

## Example

```
1 // Check if there is new GPS data
2 if (GPS.available()) {
3   // Read GPS data
4   float variation = GPS.variation();
5 
6   // ...
7 
8   // Print GPS data
9   Serial.print("Variation: ");
10  Serial.print(variation);
11  Serial.println(" degrees");
12 }
```

<a id='98ab4786-70b9-45c1-8a75-a6891167c873'></a>

## See also

begin()
end()
available()
latitude()
longitude()
speed()
course()
altitude()
satellites()
getTime()
standby()
wakeup()

<a id='a78d625f-85e3-4b59-875a-6f7418011320'></a>

altitude()

Read the altitude of the GPS.

# Syntax

<a id='7201fde5-5fe6-4ca5-8fe8-426dfdb66e5f'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-GPS-library.html

<a id='6989d508-a768-4b7f-a299-3a3884ec2152'></a>

8/15