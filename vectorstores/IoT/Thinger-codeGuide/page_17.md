<a id='31ecdff2-9322-4f8d-b4b9-154794afed80'></a>

And receiving an email with the text:

<a id='5f014367-2901-4875-8fbb-9f9d73a083d3'></a>

The the room temperature is 80.34%

<a id='d854461c-8259-44d4-90cf-d5243734cdf2'></a>

# Using Data Buckets

Thinger.io provides an easy-to-use and extremely scalable virtual storage system that allows for storing long-term device data from device output resources. This information can be used to be plotted in dashboards, or can be exported in different formats for offline processing or a third-party Data Analysis process.

<a id='0287d181-1834-4404-a658-d312822c9e23'></a>

# From Device Resource

It is not necessary to implement specific codification in device firmware to start storing data in a data bucket. Data buckets will retrieve information from output resources; simply configure the Data Bucket to set the source and sampling interval as explained in the Console documentation. ↗

<a id='a1ba7b93-6e9c-4ccc-afa8-ae52e3b72b45'></a>

# Streaming Resource Data

To enable the device to stream information only when required, such as upon event detection, the "Update by Device" option can be used during bucket configuration. This utilizes streaming resource instructions. For instance, using a previously defined Output Resource named "location," this could be achieved with this code snippet:

<a id='d3bc2c3f-3cac-4a15-a4b3-ec7eb3d9c566'></a>

```c
void loop() {
    thing.handle();
    // use the logic here to determine when to stream/record the
    resource.
    if(requires_recording){
        thing.stream("location");
    }
}
```

<a id='ad8cb95a-f7f9-4290-becc-d6acfe53752e'></a>

17