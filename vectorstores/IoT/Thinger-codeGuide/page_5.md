<a id='e30b1961-fb04-4a16-b3e6-fe774d5296d0'></a>

The `pson` data type can hold not only different data types, but also is fully compatible with JSON documents. The PSON data type can be utilized to receive multiple values simultaneously. This example will receive two different floats that are stored with the `lat` and `lon` keys.

<a id='3b794f73-a64f-4e51-9cfb-b44611283c57'></a>

thing["location"] << [](pson& in){
    float lat = in["lat"];
    float lon = in["lon"];
};

<a id='8f039236-e9c1-4b89-8c6e-750df13f2eca'></a>

## Show Input Resources State in Dashboards and API

The Dashboards or API work in a way that when opening them, they query the associated resources to correctly print their current state, i.e., the switch is on or off. In this way, when the API or a Dashboard is open, each associated input resource is called, receiving empty data in the call, as there is no intention to control the resource (the pson input will be empty).

<a id='bd3ab188-7eac-4a9c-9a4b-3675817ab994'></a>

So, how do the Dashboards or the API know what is the current state of an input resource? The resource must set its current state in the input parameter, if it is empty, or use the input value if there is one. This way, we can obtain three different things: query the current resource state (without modifying it), modify the current resource state, and obtain the expected input on the resource (this is how the API explorer on the device works).

<a id='f7f81111-8b26-4d0e-925f-ea529f0f4177'></a>

Therefore, a correct input resource definition that actually allows to display of the current state of the resource in a Dashboard or in the API, will be like this example code.

<a id='e22a1cd1-c33b-4d94-bfbb-33d858dbe56f'></a>

```
thing["resource"] << [](pson& in){
    if(in.is_empty()){
        in = currentState;
    }
    else{
        currentState = in;
    }
};
```

<a id='2fcc286d-cd67-4761-813a-f0544efe3541'></a>

5