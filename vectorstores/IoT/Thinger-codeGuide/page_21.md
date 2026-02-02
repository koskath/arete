<a id='a7639e3a-f2d5-4106-a61f-66bbed0ba3a1'></a>

It is also necessary to enable `Serial` communication, as all the debugging information is displayed over the Serial. So, enable it in the sketch in the setup method.

<a id='b9a2b73b-719e-4801-84af-703753c64dd4'></a>

```
void setup() {
  Serial.begin(115200);
}
```

<a id='d47057d1-5c7a-4af3-b00f-2e7c11ff5855'></a>

# Listen for Connection State

Sometimes it can be useful for an application to know the current connection status with Thinger.io, i.e., to notify disconnected status with a LED, request device configuration after authentication, or any other internal control flow according to connection state.

<a id='357575d3-151b-46a5-a602-5f611d926fe2'></a>

In order to create a listener for such connection states, it can be done with the `set_state_listener` function in the `setup()` method. For example, it is possible to define a listener that will receive the different connection states for the network, server, or authentication:

<a id='df90e769-5919-42e7-aaf3-e57aad9a36ab'></a>

21