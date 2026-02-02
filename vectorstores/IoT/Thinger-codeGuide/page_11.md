<a id='9eb5d84c-ea7c-444c-828c-9d343322c43f'></a>

# Communication between devices

In Thinger.io, it is possible that devices can communicate between them. There are two possibilities here. One is the communication between devices from the same account, and the other is the communication between devices from different accounts. Here we describe the two different approaches:

<a id='944c4c65-4cf5-447d-9080-5c946ee0d8d6'></a>

# Same account communication

For this use case, in which both devices belong to the same user account, there is a specific method that allows devices to communicate with other devices with low latency and simple codification. This communication can contain data or not (it is possible to make an empty call). Let's suppose that we have two devices: deviceA and deviceB, and we want to communicate both calls from deviceB to a specific deviceA input resource. We can use "thing.call_device(,);":

<a id='047399cc-25da-44aa-97fc-6ab1ae1035e3'></a>

The `deviceA` defines a resource:

```
setup(){
    thing["resource_On_A"] = [](){
        Serial.println("Someone is calling me!");
    };
}
```

`deviceB` can easily call this resource and send data to it:

```
loop(){
    thing.handle();
    // be sure to call it at an appropriate rate
    thing.call_device("deviceA", "resource_On_A");
}
```

<a id='ad1317ae-7918-48a9-93ad-16eade23231d'></a>

On the other hand, if we want to send the message with a `pson` payload in order to share data between devices. In this case, the `deviceA` will need to define a resource with some expected input

<a id='367bf585-f1c0-44c2-a006-0670025d765a'></a>

11