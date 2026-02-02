<a id='5957141a-0204-464f-9f4f-2e879a477692'></a>

## Checking Sigfox Setup

After we have both the device code running, the Sigfox callback configured, and the data bucket created, we should check that everything is up and running.

<a id='d1e069d5-8a4e-4549-a591-f5c24b9bcd32'></a>

We can start by checking that the Sigfox platform is receiving our messages. Just go to the device in the Sigfox back-end, and open the `Messages` section that is on the left panel. Here, some messages have been received. See the payload being sent (in hexadecimal), and some other information like link quality, timestamp, or callback result.

<a id='86b83c13-370b-4080-ba0f-5e486b7d6cc7'></a>

Time Data / Decoding Location Link quality Callbacks
2017-04-22 22:22:58 5a7dcf41e1182342 <::compass icon: icon::> <::four-bar signal strength indicator: icon::> <::up arrow in circle: icon::>
2017-04-22 22:12:50 e0f1cf4130272242 <::compass icon: icon::> <::four-bar signal strength indicator: icon::> <::up arrow in circle: icon::>
2017-04-22 22:02:42 4e94ce4110462442 <::compass icon: icon::> <::four-bar signal strength indicator: icon::> <::up arrow in circle: icon::>
2017-04-22 21:52:35 f9c3bb41aec44c42 <::compass icon: icon::> <::four-bar signal strength indicator: icon::> <::up arrow in circle: icon::>
2017-04-22 21:36:59 a264cb4154c12542 <::compass icon: icon::> <::four-bar signal strength indicator: icon::> <::up arrow in circle: icon::>
2017-04-22 21:26:52 45c9ca4137612642 <::compass icon: icon::> <::four-bar signal strength indicator: icon::> <::up arrow in circle: icon::>

<a id='a839be6b-f6c2-4563-8c58-c8e693a9a616'></a>

It is interesting here to check that our callback response is successful, as the callback icon changes from green to red depending on the result. In our case, our callbacks are in green, so the request was ok. Click on the icon to see the server response, which is a 200 OK HTTP response.

<a id='6e300b08-74ce-4bd7-8339-908eda9d85e3'></a>

20