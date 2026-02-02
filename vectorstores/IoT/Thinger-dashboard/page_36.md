<a id='4af92156-d85e-416e-97ef-840f8a3db114'></a>

The most interesting option is to create a custom AngularJS directive for custom widgets, as it allows isolating the widget scope, defining custom functions, reacting to changes, and in general, it is possible interacting more easily with the Thinger.io API via dependency injection.

<a id='62ad62fc-7825-4e51-a530-9625a8c77546'></a>

## AngularJS Directive Example: Hello World

Similar to the Basic Code Snippet example, in this one, a simple directive is created that will display basic information captured in the widget, i.e., the timestamp, the value, and the source configuration. For working with this example, it is required to:

<a id='91b27216-6a70-4722-b756-439ef760cbd5'></a>

- Create a new `File Storage` to store your widgets.

<a id='c0e29869-9830-4a05-b696-2b486a7c5a29'></a>

i Set public read access to the storage so the widgets can be retrieved when sharing your dashboard via Projects or shared links.

<a id='d0bd8256-1b3d-4c2f-a7c3-de556c50c4c8'></a>

- Create two files named `htmlWidget.js`, and `htmlWidget.html` inside the storage. The JavaScript file is the place where you will set your widget code and logic. On the other side, the HTML widget will hold your widget view.
- Initialize the code of both files from the following code:

<a id='acff1fe7-9895-49b3-b50f-45c746d98e68'></a>

42