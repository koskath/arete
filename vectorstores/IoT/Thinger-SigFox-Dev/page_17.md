<a id='9cd87b30-beee-44f6-9ba5-1a55d7944285'></a>

In the code, this payload can be easily represented by a `struct` containing two floats. It is possible to define custom structs with different data types (though **structure padding** and **architecture** should be considered). However, the **Sigfox payload** must be reconfigured to properly decode the fields being sent.

<a id='eed3ded8-37a7-4cb7-b890-7e3f15f81049'></a>

```c
struct data{
    float temp;
    float hum;
};
```

<a id='fbf565f8-f9d5-4717-81cf-cbefe36ec34c'></a>

**Notice** that this code has not been optimized for battery-powered use cases. Use the power-saving mode on the device if needed, but this is out of the scope of this example.

<a id='35934f17-912c-4016-80cf-5a1acaee5549'></a>

17