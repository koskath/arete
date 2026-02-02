<a id='cb4b1ab1-c95f-4c34-be98-f7ac7a3a07a1'></a>

12/4/25, 2:51 PM

<a id='d24ed296-fb24-460e-9242-3704c830180a'></a>

Arduino_MKRENV | Arduino Documentation

<a id='92169dea-4fd8-44ec-abb9-4b9fd765114b'></a>

ARDUINODOCS

<a id='06f1bbbb-a56f-456e-abdd-3655e23b5f3a'></a>

Initialize the sensors on the shield.

<a id='70e0c676-1142-40e1-b9b7-0d8b965ed716'></a>

# Syntax

```
1 ENV.begin()
```

<a id='adfa65c9-241a-4af5-9a60-681e428179aa'></a>

Parameters

None.

<a id='9e4dff73-5f46-44b9-a998-ad3269d1be07'></a>

## Returns

1 on success, 0 on failure.

<a id='eeb54d06-3b98-42e9-b6ba-67c5ecd18312'></a>

# Example

```
1 if (!ENV.begin()) {
2   Serial.println("Failed to i
3   while (1);
4 }
```

<a id='48206411-75bb-4b91-84e2-471f21a4f6f0'></a>

## See also

end()
readTemperature()
readHumidity()
readPressure()
readIlluminance()
readUVA()
readUVB()
readUVIndex()

<a id='59126eea-fb5b-4b0a-bba5-52fd8f6c47d2'></a>

end()
De-initialize the sensors on the shield.

## Syntax

```
1 ENV.end()
```

## Parameters

<a id='6fd6f7bb-9f73-4484-a3f8-204a95e189ea'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-ENV-library.html

<a id='2c91b8da-dfb6-4b31-ab8a-f48a7b205253'></a>

2/10