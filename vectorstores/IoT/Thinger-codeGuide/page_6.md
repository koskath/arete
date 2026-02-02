<a id='bff21c99-6ac3-4076-b8da-c77a0c2d1e34'></a>

This sample code basically returns the current state (like a boolean, a number, etc) if there is no input control, or uses the incoming data to update the current state. This can be easily adapted for controlling a LED, while showing its current state in the dashboard once opened or updated.

<a id='2faee321-f1ba-4398-a560-64c9baabc3a1'></a>

thing["led"] << [] (pson& in){
    if(in.is_empty()){
        in = (bool) digitalRead(pin);
    }
    else{
        digitalWrite(pin, in ? HIGH : LOW);
    }
};

<a id='980cea33-65fe-47a9-b231-06468d0d7087'></a>

Note: For controlling a digital pin, just use the method explained in the Easier Resources
Section.

<a id='b969f1fd-d53b-4c7e-8149-61e21fa6148e'></a>

## Output Resources

Output resources should be used in general when needed to sense or read a sensor value, like temperature, humidity, etc. So the output resources are quite useful for extracting information from the device.

<a id='a802f9de-0c87-46ed-848c-94c1c99bea47'></a>

To define an output resource it is used the operator >> to point to the resource name,
and it uses a C++11 Lambda function to define the output function.

<a id='2734d709-10ff-4e88-ba5f-17ba11cd3569'></a>

The output resource function takes one parameter of `pson` type that is a variable type that can contain booleans, numbers, floats, strings, or even structured information like in a JSON document.

<a id='7bdbe836-f67d-4c62-a3df-e2684bfb710b'></a>

The following subsections will show how to define different output resources for typical use cases.

<a id='0908fd9a-2d58-45dc-809f-d05af94f7abf'></a>

Read a sensor value

<a id='9c3cb80a-a0ce-4669-82b2-29d4affbe9e5'></a>

6