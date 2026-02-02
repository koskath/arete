<a id='d515e3e3-7891-440f-bbc8-af104b3704ef'></a>

<table id="22-1">
<tr><td id="22-2">State</td><td id="22-3">Description</td></tr>
<tr><td id="22-4">NETWORK_CONNECTING</td><td id="22-5">The underlying network is being connected, i.e., initializing ethernet, wifi, gsm, etc.</td></tr>
<tr><td id="22-6">NETWORK_CONNECTED</td><td id="22-7">The network is connected and ready to be used.</td></tr>
<tr><td id="22-8">NETWORK_CONNECT_ERROR</td><td id="22-9">The network cannot be initialized, i.e., bad WiFi credentials, cannot reach GSM, etc.</td></tr>
<tr><td id="22-a">SOCKET_CONNECTING</td><td id="22-b">After the network is connected, it means that the client is connecting to Thinger.io servers.</td></tr>
<tr><td id="22-c">SOCKET_CONNECTED</td><td id="22-d">The socket has been connected to the server.</td></tr>
<tr><td id="22-e">SOCKET_CONNECTION_ERROR</td><td id="22-f">The socket cannot be connected to Thinger.io. If often means a bad Internet connection.</td></tr>
<tr><td id="22-g">SOCKET_DISCONNECTED</td><td id="22-h">The connection with Thinger.io has been closed.</td></tr>
<tr><td id="22-i">SOCKET_ERROR</td><td id="22-j">An error happened with the socket, i.e, bad read or write, which will cause a disconnect.</td></tr>
<tr><td id="22-k">SOCKET_TIMEOUT</td><td id="22-l">The socket timed out while reading or writing, so the connection will be closed.</td></tr>
<tr><td id="22-m">THINGER_AUTHENTICATING</td><td id="22-n">Thinger.io client is connected and it is being authenticated.</td></tr>
<tr><td id="22-o">THINGER_AUTHENTICATED</td><td id="22-p">Thinger.io client is connected and authenticated, so it can use Thinger.io, i.e., call an endpoint, read a property, etc.</td></tr>
<tr><td id="22-q">THINGER_AUTH_FAILED</td><td id="22-r">Thinger.io client authentication failed. Please, review the server, username, device id, and password.</td></tr>
<tr><td id="22-s">THINGER_STOP_REQUEST</td><td id="22-t">Thinger.io client was requested to stop, i.e., from the source code, or by the server.</td></tr>
</table>
Previous
OTHER DEVICES

<a id='372e4cc3-b2c2-4e2e-a381-c4b944975f7d'></a>

23