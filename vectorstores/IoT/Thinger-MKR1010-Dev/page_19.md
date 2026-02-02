<a id='a01a60d5-5b88-40cb-b1c7-9404c3888aa3'></a>

ArduinoNanoRP2040.ino arduino_secrets.h

<a id='0f1240c1-e03c-4abc-8e94-893428d1eda6'></a>

#define USERNAME "your_user_name"
#define DEVICE_ID "your_device_id"
#define DEVICE_CREDENTIAL "your_device_credential"

#define SSID "your_wifi_ssid"
#define SSID_PASSWORD "your_wifi_ssid_password"

<a id='1924dc24-b542-4b54-be11-dcb739edafe5'></a>

For using Arduino Nano RP2040 over the default TLS/SSL connection, it is required to install the Thinger.io server certificate in the board with the Wifi101 Firmware Updater located in the Tools menu.

<a id='ad0e87e6-e845-4e06-a682-7a45a2283511'></a>

WiFi101 Firmware/Certificates Updater

1. Select port of the WiFi module
If the port is not listed click "Refresh list" button to regenerate the list

/dev/cu.SOC
/dev/cu.MALS
/dev/cu.Bluetooth-Incoming-Port
/dev/cu.usbmodem1442211
/dev/cu.usbmodem1442311

Refresh list
Test connection

2. Update firmware
Select the firmware from the dropdown box below
WINC1501 Model B (19.5.2)

Update Firmware

3. Update SSL root certificates
Add domains in the list below using "Add domain" button

arduino.cc:443
thinger.io:443

Add domain
Remove domain

Upload Certificates to WiFi module

<a id='7e54a96d-d560-49fa-bed6-36cba7fb2b88'></a>

WiFiNINA Certificates Updater

<a id='4f71f11e-6ac9-4aa6-81b1-6eee8f81e69f'></a>

19