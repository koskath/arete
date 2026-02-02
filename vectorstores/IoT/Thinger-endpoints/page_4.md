<a id='d96271d5-ef2f-464f-a92c-11b6987f3926'></a>

Endpoint Type
HTTP Request

Request URL
POST https://dummyhost.com/data

Request Headers
Authorization Bearer 14in63er41v4r(
+ Add Header

Request Body
option Send device data as JSON: [x]
option Send custom data: [ ]

<a id='f117d059-a7a3-4275-b59f-018e0c28f5a3'></a>

Telegram Bot Endpoint

<a id='3102e33e-511c-4b98-86f8-3f50383a9b7f'></a>

This endpoint is pre-configured to send data to a Telegram bot in a simple way and thus use the messaging platform to get alerts or data from the IoT devices through Thinger.io.

<a id='1503fe4d-f419-4478-9c68-8127bb859093'></a>

thinger.io

Statistics
Devices
Dashboards
Data Buckets
**Endpoints**
Alarms
Access Tokens
Assets
File Storages
Products
Projects
Plugins
Toolbox

<a id='23daf549-aea2-498d-b51a-2932a2198af4'></a>

☰ 🗃 Statistics ▾ ⊕ 📣 user ▾ 👤

<a id='44a14d2c-d660-4d76-85c4-6e24cf5ccbb0'></a>

Endpoints > Add

Endpoint Details

Endpoint Identifier: TelegramTest
Endpoint Name: FirstEndpoint
Endpoint Description: Sending data to telegram bot
option Enabled: [ ]
Endpoint Type: Telegram Send Message
Bot Token: 9x1x3x4x6:AxH0JcxmPUhnERY_VXXnnO5c_8valwZ9XOOXX
Chat Identifier: 1096342XXX
Chat Message: the current temperature is {{temperature}}

Add Endpoint

<a id='7cf50854-6856-48ee-9e49-61d2c31a84a6'></a>

The next parameters need to be configured to work with Telegram bot:

<a id='a9d9db2c-de8d-437c-ac09-43f67415c814'></a>

• Bot Token: Is the bot identification and authorization stream; this parameter can be left empty on this form in order to specify it directly in the device source code with the key "token".

<a id='058bb91d-2503-4ebb-8617-31874b2615b4'></a>

5