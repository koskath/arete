<a id='40f7aecd-eb32-4ed2-b054-3875a23dccf5'></a>

```cpp
void setup() {
  // the setup code here..

  thing.set_state_listener([&](ThingerClient::THINGER_STATE
  state) {
    switch (state) {
      case ThingerClient::NETWORK_CONNECTING:
        break;
      case ThingerClient::NETWORK_CONNECTED:
        break;
      case ThingerClient::NETWORK_CONNECT_ERROR:
        break;
      case ThingerClient::SOCKET_CONNECTING:
        break;
      case ThingerClient::SOCKET_CONNECTED:
        break;
      case ThingerClient::SOCKET_CONNECTION_ERROR:
        break;
      case ThingerClient::SOCKET_DISCONNECTED:
        break;
      case ThingerClient::SOCKET_ERROR:
        break;
      case ThingerClient::SOCKET_TIMEOUT:
        break;
      case ThingerClient::THINGER_AUTHENTICATING:
        break;
      case ThingerClient::THINGER_AUTHENTICATED:
        break;
      case ThingerClient::THINGER_AUTH_FAILED:
        break;
      case ThingerClient::THINGER_STOP_REQUEST:
        break;
    }
  });
}
```

<a id='d0f29651-d108-4127-a9e9-7b206876edd6'></a>

In this table it is detailed the different values and their descriptions.

<a id='8f5bc14b-3b4a-4137-88b8-ec54adec2a78'></a>

22