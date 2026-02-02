<a id='0c34ad17-3b46-4185-96b5-bc065c97fd49'></a>

There is an example of an email endpoint that contains some text and variables that are filled when the device calls the endpoint, adding the current temperature and humidity reported by the device. Notice that `temperature` and `humidity` variables are closed inside double brackets `{{}}`, so the endpoint will be expecting this information to complete the body.

<a id='9b633ce2-ab70-4b19-bf95-9daac7034696'></a>

Endpoint Type
Email

Email Address
alvarolb@gmail.com

Email Subject
Example email for documentation

Email Body
option Send device data as JSON: [ ]
option Send custom body: [x]

<a id='246791ab-5127-4326-8e05-ea22187ab19a'></a>

<table id="2-1">
<tr><td id="2-2">H1</td><td id="2-3">H2</td><td id="2-4">H3</td><td id="2-5">H4</td><td id="2-6">H5</td><td id="2-7">H6</td><td id="2-8">P</td><td id="2-9">pre</td><td id="2-a">&quot;</td><td id="2-b">B</td><td id="2-c">I</td><td id="2-d">U</td><td id="2-e">S (with strikethrough)</td><td id="2-f">bulleted list icon</td><td id="2-g">numbered list icon</td><td id="2-h">curved arrow pointing left</td><td id="2-i">curved arrow pointing right</td><td id="2-j">circle with diagonal line</td></tr>
<tr><td id="2-k">four horizontal lines</td><td id="2-l">four horizontal lines</td><td id="2-m">four horizontal lines</td><td id="2-n">four horizontal lines</td><td id="2-o">four horizontal lines (with play icon)</td><td id="2-p">menu icon</td><td id="2-q">&lt;/&gt;</td><td id="2-r">image icon</td><td id="2-s">link icon</td><td id="2-t">play button icon</td><td id="2-u"></td><td id="2-v"></td><td id="2-w"></td><td id="2-x"></td><td id="2-y"></td><td id="2-z"></td><td id="2-A"></td><td id="2-B"></td></tr>
</table>

<a id='a01ea9e4-736c-4de5-82dd-89639ce0c783'></a>

Hi Dude! ☁️
Temperature is: {{temperature}} °C
Humidity is: {{humidity}} %

<a id='4eabaf0f-803b-4887-b6ea-36901bb244d0'></a>

Calling endpoints is well documented here ↗, but it is basically required to call the endpoint by using the `call_endpoint` method, which requires the endpoint id, `ExampleEmail` in this example, the optional data to be sent to the endpoint, which is a `pson` document (quite similar to JSON) with two keys named `temperature` and `humidity` holding the readings from a DHT sensor:

<a id='505d8098-c041-4645-9fa7-fe05ae4c5d40'></a>

3