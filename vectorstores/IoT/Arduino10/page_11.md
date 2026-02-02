<a id='e806efd8-858d-4da9-bea2-7a80f2a387b6'></a>

12/4/25, 2:52 PM

<a id='b72a6295-ae19-4830-9e7e-729cccabb8af'></a>

WiFiNINA | Arduino Documentation

<a id='fbf9f13b-4629-4a32-95e6-adbe79adc8c5'></a>

ARDUINODOCS

<a id='212b238c-4234-4ad2-a859-d06c0d8e929d'></a>



<a id='cc596e0a-b5e8-4fc3-b10e-c17b2dc92f7d'></a>

# Syntax

```
1 client.println()
2 client.println(data)
3 client.print(data, BASE)
```

<a id='74ddfe24-2c61-462b-82e4-d17c288f2396'></a>

# Parameters

data (optional): the data to print (char,
byte, int, long, or string)

BASE (optional): the base in which to
print numbers: DEC for decimal (base
10), OCT for octal (base 8), HEX for
hexadecimal (base 16).

<a id='3591e797-230c-4635-a041-983684d4cd0b'></a>

## Returns

byte: return the number of bytes
written, though reading that number is
optional

<a id='ad6d2c07-d466-4351-a1e9-febb8bbc143c'></a>

client.available()

<a id='f4645d9d-8e60-4579-bd1e-db9341396376'></a>

## Description

Returns the number of bytes available for reading (that is, the amount of data that has been written to the client by the server it is connected to).

<a id='e3b1820b-84b1-484f-9ba3-5e2588c7a029'></a>

available() inherits from the Stream utility class.

<a id='8b03ea34-39db-4bdf-8a99-0cbea0747887'></a>

## Syntax

```
1 client.available()
```

<a id='cd4e4a02-b291-4446-a119-28d516c517b7'></a>

Parameters

None

<a id='9e9025d9-1d60-4b75-9866-9536fa16ca35'></a>

## Returns

The number of bytes available.

<a id='85e9b110-5616-4b6e-9538-311cc15179a0'></a>

Example

<a id='81d280a5-4d7f-4ca6-8915-6250a46f3dc4'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='3ca8ffb4-7eae-4e2e-8e8b-20425926a2b7'></a>

11/16