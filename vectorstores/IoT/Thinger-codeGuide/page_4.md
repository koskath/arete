<a id='44db2917-efa8-4034-940b-132e135c0d36'></a>

This kind of resource only requires an on/off state, so it can be enabled or disabled as required. As the `pson` type can hold multiple data types, we can think that the `pson` parameter of the input function is like a boolean.

<a id='37d3e4f4-78e6-4964-adf3-2a1878582b44'></a>

So, inside the setup function, place a resource called led (but use any other name),
of input type (using the operator <<), that takes a reference to a pson parameter.
This example will turn on/off the digital pin 10 using a ternary operator over the in
parameter.

<a id='96550b32-f8a5-4250-ab2c-91d10e5dc663'></a>

thing["led"] << [](pson& in){
    digitalWrite(10, in ? HIGH : LOW);
};

<a id='db35727b-2643-4bfc-a348-e92e5a4b54b3'></a>

### Modify a servo position

Modifying a servo position is quite similar to turning on/off a LED. In this case, however, it is necessary to use an integer value. As the `pson` type can hold multiple data types, we can still use the `pson` type as an integer value.

<a id='1d69c364-ec07-437d-afbd-dfb3cca0e939'></a>

thing["servo"] << [](pson& in){
    myServo.write(in);
};

<a id='ad9d1b36-507f-4e55-b117-14a729ba3bc2'></a>

_**Update sketch variables**_

Input resources can also be used to update sketch variables, allowing for dynamic changes in device behavior. This is quite useful in situations where it is desirable to temporarily disable an alarm, change reporting intervals, update a hysteresis value, and so on. In this way, additional resources can be defined to change variables.

<a id='b0a50418-cac0-4d9b-9dbc-79aaca72f55b'></a>

```
float hysteresis = 0; // defined as a global variable
thing["hysteresis"] << [] (pson& in){
    hysteresis = in;
};
```

<a id='803b09c3-d2a3-451a-be65-25a9b7b8c15b'></a>

Pass multiple data

<a id='1c51dcfe-737d-4a44-8084-6b68c9ed1a7a'></a>

4