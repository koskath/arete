<a id='6e577049-6c5d-400f-b467-efefb8b04107'></a>

# Arduino_MQTT_Pro_Mini

Arduino MQTT client for ESP8266 and ESP32 using the [AsyncMQTT_Pro_Mini](https://github.com/hideaki-tanaka/AsyncMQTT_Pro_Mini) library.

This library allows you to create an MQTT client for your Arduino projects, providing a simple interface for connecting to an MQTT broker, publishing messages, and subscribing to topics. It supports both ESP8266 and ESP32 microcontrollers.

## Examples included!

*   `MQTT_Connect`
*   `MQTT_Connect_LastWill`
*   `MQTT_Publish`
*   `MQTT_Subscribe`
*   `MQTT_Subscribe_QoS1`
*   `MQTT_Subscribe_QoS2`
*   `MQTT_Subscribe_QoS_All`
*   `MQTT_Subscribe_Multi`
*   `MQTT_Publish_Retain`
*   `MQTT_Publish_QoS1`
*   `MQTT_Publish_QoS2`
*   `MQTT_Publish_QoS_All`
*   `MQTT_Unsubscribe`
*   `MQTT_Disconnect`
*   `MQTT_Loop`
*   `MQTT_DeepSleep`
*   `MQTT_Custom_KeepAlive`
*   `MQTT_Custom_BufferSize`

# Classes

## MQTT_Client

```cpp
class MQTT_Client {
public:
  MQTT_Client(const String& clientID);
  // ... other methods ...
};
```

## MQTT_Client(const String& clientID)

This constructor creates an instance of the `MQTT_Client` class with the specified client ID.

```cpp
MQTT_Client(const String& clientID);
```

**Parameters:**

*   `clientID`: The unique ID for the MQTT client.

# Methods

## begin()

Initializes the MQTT client and sets up the connection to the MQTT broker.

```cpp
void begin();
```

## connect()

Connects to the MQTT broker. This method should be called after `begin()`.

```cpp
bool connect();
bool connect(const String& username, const String& password);
bool connect(const String& username, const String& password, const String& willTopic, uint8_t willQoS, bool willRetain, const String& willMessage);
```

## disconnect()

Disconnects from the MQTT broker.

```cpp
void disconnect();
```

## publish(const String& topic, const String& payload)

Publishes a message to the specified topic with QoS 0.

```cpp
void publish(const String& topic, const String& payload);
```

## publish(const String& topic, const String& payload, uint8_t qos)

Publishes a message to the specified topic with the given QoS.

```cpp
void publish(const String& topic, const String& payload, uint8_t qos);
```

## publish(const String& topic, const String& payload, uint8_t qos, bool retain)

Publishes a message to the specified topic with the given QoS and retain flag.

```cpp
void publish(const String& topic, const String& payload, uint8_t qos, bool retain);
```

## subscribe(const String& topic)

Subscribes to the specified topic with QoS 0.

```cpp
void subscribe(const String& topic);
```

## subscribe(const String& topic, uint8_t qos)

Subscribes to the specified topic with the given QoS.

```cpp
void subscribe(const String& topic, uint8_t qos);
```

## unsubscribe(const String& topic)

Unsubscribes from the specified topic.

```cpp
void unsubscribe(const String& topic);
```

## setCallback(std::function<void(char*, uint8_t*, unsigned int)> callback)

Sets the callback function to be called when a message is received.

```cpp
void setCallback(std::function<void(char*, uint8_t*, unsigned int)> callback);
```

## loop()

This method should be called in the main loop of your sketch to allow the client to process incoming messages and maintain the connection.

```cpp
void loop();
```

## setKeepAlive(uint16_t keepAlive)

Sets the keep-alive interval in seconds. Default is 60 seconds.

```cpp
void setKeepAlive(uint16_t keepAlive);
```

## setBufferSize(uint16_t bufferSize)

Sets the size of the receive buffer. Default is 1024 bytes.

```cpp
void setBufferSize(uint16_t bufferSize);
```

## connected()

Returns `true` if the client is currently connected to the MQTT broker, `false` otherwise.

```cpp
bool connected();
```

## lastPingTime()

Returns the timestamp of the last successful ping response.

```cpp
unsigned long lastPingTime();
```

## lastPublishTime()

Returns the timestamp of the last successful publish operation.

```cpp
unsigned long lastPublishTime();
```

## lastSubscribeTime()

Returns the timestamp of the last successful subscribe operation.

```cpp
unsigned long lastSubscribeTime();
```

## lastUnsubscribeTime()

Returns the timestamp of the last successful unsubscribe operation.

```cpp
unsigned long lastUnsubscribeTime();
```

## lastDisconnectTime()

Returns the timestamp of the last successful disconnect operation.

```cpp
unsigned long lastDisconnectTime();
```

## lastConnectTime()

Returns the timestamp of the last successful connect operation.

```cpp
unsigned long lastConnectTime();
```

## setWill(const String& willTopic, uint8_t willQoS, bool willRetain, const String& willMessage)

Sets the Last Will and Testament message.

```cpp
void setWill(const String& willTopic, uint8_t willQoS, bool willRetain, const String& willMessage);
```

## clearWill()

Clears the Last Will and Testament message.

```cpp
void clearWill();
```

## setCleanSession(bool cleanSession)

Sets whether the client should start a clean session. Default is `true`.

```cpp
void setCleanSession(bool cleanSession);
```

## setServer(const String& server, uint16_t port)

Sets the MQTT broker server address and port.

```cpp
void setServer(const String& server, uint16_t port);
```

## setCredentials(const String& username, const String& password)

Sets the username and password for authentication.

```cpp
void setCredentials(const String& username, const String& password);
```

## setClientId(const String& clientID)

Sets the client ID for the MQTT connection.

```cpp
void setClientId(const String& clientID);
```

## setHost(const String& host)

Sets the hostname for the MQTT connection.

```cpp
void setHost(const String& host);
```

## setPort(uint16_t port)

Sets the port for the MQTT connection.

```cpp
void setPort(uint16_t port);
```

## setSecure(bool secure)

Sets whether to use SSL/TLS for the connection.

```cpp
void setSecure(bool secure);
```

## setFingerprint(const uint8_t fingerprint[20])

Sets the SSL/TLS certificate fingerprint for verification.

```cpp
void setFingerprint(const uint8_t fingerprint[20]);
```

## setCACert(const char* caCert)

Sets the CA certificate for SSL/TLS verification.

```cpp
void setCACert(const char* caCert);
```

## setCert(const char* clientCert, const char* clientKey)

Sets the client certificate and private key for SSL/TLS client authentication.

```cpp
void setCert(const char* clientCert, const char* clientKey);
```

## setTopicAlias(uint16_t alias)

Sets a topic alias for the next publish message.

```cpp
void setTopicAlias(uint16_t alias);
```

## getTopicAlias()

Returns the current topic alias.

```cpp
uint16_t getTopicAlias();
```

<a id='5b408ddb-66ee-4ac5-baa1-a84aaead10ff'></a>

← Go Back

# Library

Recents viewed

Arduino_MKRGPS
Arduino_APDS9960
Arduino_MKRIoTCarrier

<a id='cf685ac9-1059-4a82-a216-3b70070f6c15'></a>

Home / Programming / Library / Arduino_MKRIoTCarrier

SENSORS

# Arduino_MKRIoTCarrier

GNU Lesser General Public License v2.1 V2.1.0

Riccardo Rizzo, Jose García, Pablo Marquínez 04/04/2024

Arduino <info@arduino.cc>

https://github.com/arduino-li... info@arduino.cc

<a id='245379e3-9b3d-49cf-98ab-4e67e8b0e321'></a>

ON THIS PAGE

Usage/Examples
Compatibility
Releases