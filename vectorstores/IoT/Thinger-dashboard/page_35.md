<a id='2d208825-92a3-48d2-8cfa-dcd908d16da0'></a>

option Basic Code Snippet: [x]
option Table Code Snippet: [ ]
option Third Party Scripts: [ ]

<a id='99891082-68f2-42ae-953c-dc52fd6c26c7'></a>

Example hello world displaying timestamp, timestamp formatted as a date, and the selected value.

<a id='8ea21e31-0ff7-497a-844d-7d7139e05c2c'></a>

# Hello World!

Ts: 1636920253129

Date: Nov 14, 2021 9:04:13 PM

Value: ["a":1234,"b":"890","c":"900"}

Simple HTML widget displaying data timestamp and its value.

<a id='8bf27b32-1c7a-41de-bea6-ab68a2908e28'></a>

The widget code is the following:

```html
<h1>Hello World !</h1>
<p>Ts: {{ts}}</p>
<p>Date: {{ts | date: 'medium'}}</p>
<p>Value: {{value}}</p>
```

<a id='d9ee8031-2918-40e6-9dba-61ccc43d09d6'></a>

# From File Storage

For more complex developments over the HTML Widget, where several source code files are required, it is possible to use the **File Storage** ↗ feature. This allows the development of more complex interfaces that exploit all the representation capabilities of the browser, such as 3D object representation, animated widgets, etc. Moreover, widgets from File Storage can be shared between multiple dashboards is required, so it is much more maintainable in the long term.

<a id='07ddec03-0526-422d-9551-0b4db9c14645'></a>

It is possible to point the widget to an HTML file inside a file storage by selecting the `File Storage` from `HTML Source` option and then typing the file name.

<a id='af2cf320-ad02-496c-ba95-1774e6768cfa'></a>

41