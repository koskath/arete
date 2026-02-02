<a id='8149eb51-ad7d-452c-a9ec-b7fd7f0d232f'></a>

12/4/25, 2:51 PM

<a id='e5d4e548-2719-43ca-b71a-a9eaef09414d'></a>

Arduino_MKRENV | Arduino Documentation

<a id='91b7e701-afb8-4f26-9307-9c8707d716f9'></a>

ARDUINODOCS

<a id='8dee1664-518f-431e-8ce0-7b7ce1b12fac'></a>

readIlluminance()
Read the light sensor's value.

<a id='3e8665e5-cc53-419e-b47d-e6c0bcae752c'></a>

## Syntax

```
1 ENV.readIlluminance(unit)
```

<a id='e4fae01e-047f-4a97-b110-40ffe63a5489'></a>

# Parameters

unit: FOOTCANDLE to get the light
value in footcandle, METERCANDLE to
get the light in metercandle and LUX to
get the light value in lux (default).

<a id='2d1bc875-cf37-4271-b3ec-5b6a39753c0e'></a>

# Returns

The light sensor's value as float in the specified unit.

<a id='821fa859-9db0-460f-9110-a0645243752d'></a>

Example

```
1 Serial.print("Lux = ");
2 Serial.println(ENV.readIllumina
```

<a id='bcb9a5a4-cfae-4217-a269-b0ecdb86e2e7'></a>

See also

begin()
end()
readTemperature()
readHumidity()
readPressure()
readUVA()
readUVB()
readUVIndex()

<a id='7d8e18f0-b759-4b2d-8928-42741953114a'></a>

readUVA()
Read the UV sensor's UV A value.

<a id='151b2088-351f-4814-a4fe-cbe3fad7a353'></a>

Syntax

```
1 ENV.readUVA()
```

<a id='0f431a30-e401-48dc-ad32-913370550ca4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='c95f9bd5-9388-464f-869c-d2cdb670ac0e'></a>

6/10