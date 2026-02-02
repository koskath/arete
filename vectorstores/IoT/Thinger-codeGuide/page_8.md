<a id='53176497-72ea-4082-bb26-d392dc0ab560'></a>

These kinds of resources are defined with the operator `=`. In this case, the function takes two different `pson` parameters. One for input data and another for output data. This example provides an altitude reading using the BMP180 Sensor. It takes the reference altitude as input and provides the current altitude as output.

<a id='9a2fadb6-0336-4da4-9d05-6f17020070ac'></a>

thing["altitude"] = [](pson& in, pson& out){
    out = bmp.readAltitude(in);
};

<a id='d6b0f9a3-768d-4efd-85d8-4a94b6269c58'></a>

Also, define more complex input/output resources that take several input values, to provide multiple output values, like in this example that takes `value1` and `value2` to provide the `sum` and `mult` values.

<a id='11cdfec3-d8be-4fa9-89b1-00ebad0b1e02'></a>

thing["in_out"] = [] (pson& in, pson& out){
out["sum"] = (long)in["value1"] + (long)in["value2"];
out["mult"] = (long)in["value1"] * (long)in["value2"];
};

<a id='f3a8d369-cba9-48c1-89aa-ec277ddecd8e'></a>

# Resources without parameters
It is also possible to define resources that do not require any input or generate any output. These are like callbacks that can be executed as needed, for example, to reboot the device or perform a required action.

<a id='846cdeed-f2c2-4110-babc-08e427d90669'></a>

In this case, the resource is defined as a function without any input or output parameters.

<a id='5a364ccb-f0c5-4555-9cf8-df7d0428e88a'></a>

```
thing["resource"] = [](){
// write here the execution code
};
```

<a id='abaac68e-e9eb-491b-a3bc-e8e850d93a82'></a>

Easier Resources

<a id='d1566e83-e3c1-40c5-a700-4a41a5d3d884'></a>

8