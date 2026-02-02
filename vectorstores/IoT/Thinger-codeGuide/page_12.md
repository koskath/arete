<a id='c59b149c-03b5-41d9-a26c-9fb2cd5d9842'></a>

```
setup(){
    thing["resourceOnA"] << [](pson& in){
        int val1 = in["anyValue1"];
        float val2 = in["anyValue2"];
        // Work with the updated parameters here
    };
}
```

<a id='81773c17-2cba-456b-a95d-4a0b7bb2e700'></a>

Then `deviceB` can call this method, providing the appropriate input by defining a `pson` type that is filled with the same keys used on `resource0nA` :

<a id='82cd7ba5-3e07-4ab8-923a-38481ce4887b'></a>

```
loop(){
  thing.handle();
  // be sure to call it at an appropriate rate
  pson data;
  data["anyValue1"] = 3;
  data["anyValue2"] = 43.1;
  thing.call_device("deviceA", "resourceOnA", data);
}
```

<a id='5a3bb941-0b98-4043-a34a-3c67c32d1a0e'></a>

`deviceB` can also call this method by providing the information from a defined resource that generates the information. In this case, the call is similar to the previous example, but using the resource as the data source.

<a id='dc0f5382-d522-435d-9084-3760129dd633'></a>

setup(){
    thing["resourceName"] >> [] (pson& out){
        out["anyValue1"] = 3;
        out["anyValue2"] = 43.1;
    };
}

loop(){
    thing.handle();
    // be sure to call it at an appropriate rate
    thing.call_device("deviceA", "resource0nA",
    thing["resourceName"]);
}

<a id='1a48507a-15c6-40bb-bc49-0a1ff4204401'></a>

Communication between different accounts

<a id='874ee620-1415-4c34-81d0-8886c7ebb16b'></a>

12