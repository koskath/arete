<a id='30870471-9be1-4334-b0a1-99eda3096e9e'></a>

12/4/25, 2:49 PM

<a id='521d9966-7b04-4463-a3de-fc0d5adc3f02'></a>

ArduinoBLE | Arduino Documentation

<a id='c4c0e739-fe90-487b-b847-cddcfd601534'></a>

ARDUINODOCS

<a id='f07b6223-4682-4811-a48b-df60c789cef0'></a>

[Empty input field]

<a id='eae402e1-b86d-4608-bbfd-9c96cafd1c48'></a>

1 if (BLE.connected()) {
2   BLE.disconnect();
3 }

<a id='fb62a011-dc6d-4420-977d-6bb6fdcf9489'></a>

v BLE.address()
Query the Bluetooth® address of the Bluetooth® Low Energy device.

<a id='b4a8eefe-081e-46f2-ac44-485b865c7225'></a>

## Syntax

```
1 BLE.address()
```

<a id='36fcaa4a-5fd9-4afb-baec-8811f758d825'></a>

Parameters

None

<a id='3bc5dd31-ceb9-44b6-869f-96a5fb91dc16'></a>

## Returns

The **Bluetooth® address** of the Bluetooth® Low Energy device (as a String).

<a id='c99af429-863b-49a1-b44c-da6c7831cd62'></a>

Example

```
1 String address = BLE.address();
2
3 Serial.print("Local address is: ");
4 Serial.println(address);
```

<a id='8422799f-9af9-4641-8a22-d41470f7d703'></a>

√ BLE.rssi()

Query the RSSI (Received signal strength indication) of the connected Bluetooth® Low Energy device.

# Syntax

```
1 BLE.rssi()
```

<a id='66a9366f-74ab-47a7-8816-504f941bd8d3'></a>

Parameters

<a id='cefa9af9-aead-4289-9dca-3f2747a08053'></a>

file:///Users/Konstantinos/Konstantinos/arete2/course_content/IoT/Documentation_html/MKR-BLE-library.html

<a id='5904297e-f721-4490-bbf4-2e4d23f5c99d'></a>

9/26