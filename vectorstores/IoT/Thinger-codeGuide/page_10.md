<a id='484fd79f-7552-4798-b3ed-200296c2312d'></a>

# Modify Sketch Variables

Our sketch usually defines some parameters or variables that are used inside the loop code. These kinds of resources are normally used to handle or control the execution behaviour. With these kinds of resources, we can modify any parameter we want to expose, like a float, an integer, a boolean, etc.

<a id='a8416200-6e54-42fe-94b1-7f8b6d7992b1'></a>

In this example, it is possible to remotely modify the boolean `sdLogging` variable defined as a global variable.

<a id='213006a1-ceab-4e2f-b30b-55b0d96ddc41'></a>

thing["logging"] << inputValue(sdLogging);

<a id='6e066dff-6c14-4485-a92d-a9ce316b79a4'></a>

It is also possible to define a callback function to know when the variable has changed, so we can perform any other action. For this use case, define the resource to have some code executed when the `hysteresisVar` changes.

<a id='a46dd314-2ed4-4b23-b280-b8a7c5512889'></a>

```
thing["hysteresis"] << inputValue(hysteresisVar, {
// execute some code when the value changes
Serial.println("Hystereis changed to: ");
Serial.print(hysteresisVar);
});
```

<a id='87a5c01a-74fb-4073-9542-fddb3239221e'></a>

# Servo control

It is also possible to define a resource for controlling a servo instance. This way, the defined resource will automatically handle the servo instance, reading its current position, or changing to a new one according to the API interactions.

<a id='8a26ca93-85f3-4794-8325-c733ffc22b38'></a>

To define a servo resource, just define and initialize the servo as usual, and then use the declared instance in the resource definition.

<a id='8e6aa5ba-e547-4fa3-9d12-a892c9f9ab61'></a>

thing["servo"] << servo(myServoInstance);

<a id='1e023a41-12fe-4946-925e-af2aef3bc5b0'></a>

10