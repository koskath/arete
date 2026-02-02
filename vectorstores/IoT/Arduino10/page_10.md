<a id='857d876d-18ae-434d-b36a-d789c3084fa1'></a>

12/4/25, 2:52 PM

<a id='9086759c-851e-4b96-a7dd-fa936e302f6d'></a>

WiFiNINA | Arduino Documentation

<a id='36a2922f-78a2-405b-be63-ef612827e77d'></a>

ARDUINODOCS

<a id='9422a797-0d05-4de3-b3c4-a750053493ba'></a>

data: the outgoing byte
buffer: the outgoing message
size: the size of the buffer

<a id='3ed26df2-addb-405a-9da8-5af8d13aa02b'></a>

# Returns

The number of bytes written. It is not
necessary to read this.

<a id='e5997b7b-3dae-45fc-921e-fe804f780fa2'></a>

client.print()

<a id='f9d0d1fb-2f98-4707-a5f2-1c592d3bc194'></a>

## Description

Print data to the server that a client is connected to. Prints numbers as a sequence of digits, each an ASCII character (e.g. the number 123 is sent as the three characters '1', '2', '3').

<a id='ccb691d1-6ca7-42be-9209-adf944c77131'></a>

## Syntax

```
client.print(data)
client.print(data, BASE)
```

<a id='107a18ee-9e4b-4a8e-ae38-3f9cde217ac0'></a>

# Parameters

data: the data to print (char, byte, int, long, or string)

BASE (optional): the base in which to print numbers:, DEC for decimal (base 10), OCT for octal (base 8), HEX for hexadecimal (base 16).

<a id='f4bcd83d-40b5-4ee0-82a1-0ede0d492a8a'></a>

Returns

byte : returns the number of bytes
written, though reading that number is
optional

<a id='083fb54e-2d90-45cb-88ba-a5c44b3aa8a3'></a>

client.println()

<a id='bfe53cdc-4a92-4797-a15f-8ed361563af9'></a>

# Description
Print data, followed by a carriage return and newline, to the server a client is connected to. Prints numbers as a sequence of digits, each an ASCII character (e.g. the number 123 is sent as the three characters '1', '2',

<a id='09cef40e-b280-438d-9c60-9e0c5b6649fc'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-wifiClient-library.html

<a id='caadd0d8-2231-47d4-aad2-1f92e5ed3f76'></a>

10/16