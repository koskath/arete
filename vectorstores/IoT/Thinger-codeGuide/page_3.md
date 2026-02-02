<a id='8a2f2d6c-d6a7-4e46-a02e-240a55945d94'></a>

In the Thinger.io platform, each device can define several resources. A resource can be considered anything that can be sensed or activated. For example, typical resources include a sensor value like temperature or humidity, or a relay that controls a light. Therefore, the resources that need to be exposed over the Internet should be defined.

<a id='6eff77b7-9534-4c49-b0eb-7404819efde2'></a>

All resources must be defined inside the `setup()` method of the Arduino sketch. This way, the resources are configured at the beginning, but can be accessed later as necessary.

<a id='36718241-5e93-496b-9e6f-50f4d533b0fe'></a>

There are three different types of resources, which are explained in the following sections.

<a id='0b5fcc69-26f6-48d6-adff-3ed071eebef8'></a>

# Input Resources

If control or actuation of an IoT device is required, an input resource must be defined. An input resource serves as a source of information for the device. Examples include resources for controlling a light or relay, adjusting a servo position, or modifying a device parameter.

<a id='30d7114d-1dc9-49bf-8dcc-f73a1f22876b'></a>

To control or actuate an IoT device, it is necessary to define an input resource. An input resource is anything that can provide information to a device. Examples include a resource for turning a light or a relay on and off, changing a servo position, or adjusting a device parameter.

<a id='09b3597b-74b4-494e-aed7-e3ccbad54d96'></a>

To define an input resource it the operator is used << , pointing to the resource name,
and it uses a C++11 Lambda function to define the function.

<a id='55fbd457-f882-40fa-b5d3-8fecc9187ff0'></a>

The input resource function takes one parameter of type `pson` that is a variable type that can contain booleans, numbers, floats, strings, or even structured information like in a JSON document.

<a id='39a96035-4537-43b6-b7e2-bdc2b13a3644'></a>

The following subsections will show how to define different input resources for typical use cases.

<a id='ca4ede91-3d8d-4be5-871e-74db2c98be49'></a>

*Turn on/off a LED, a relay, etc*

<a id='02bd4718-ab1b-46bb-a65f-8ce68e009193'></a>

3