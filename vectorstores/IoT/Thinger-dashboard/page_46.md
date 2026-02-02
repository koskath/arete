<a id='2bb05d38-6a45-4fe0-9a60-ec355c63efe3'></a>

Finally, using the "code snippet" section, it's possible to customize the appearance of the table structure. It's important to take care of the data structure when calling the variables. The example above has been created by means of a simple source code in HTML, whose variable ID's must fit with the ones introduced in the source "Name" input box.

<a id='3443519b-7b7d-4cda-b4d4-dd3c329443c8'></a>

<div style="width=100%; height:100%; overflow-y:scroll">
<table class="table table-striped">
<thead>
<tr>
<th>Date</th>
<th>Temperature</th>
<th>Humidity</th>
</tr>
</thead>
<tbody>
<tr ng-repeat="entry in value">
<td>{{entry.ts| date: 'medium'}}</td>
<td>{{entry.temperature}}</td>
<td>{{entry.humidity}}</td>
</tr>
</tbody>
</table>
</div>

<a id='0f2bca4a-8478-4311-82a2-c5ea38cfab51'></a>

# Group Widget

The **Group Widget** is a container element designed to organize and group multiple individual widgets within a single visual unit. This structure allows for a semantically meaningful layout, enabling users to associate related widgets visually and functionally.

<a id='42280c64-453b-49fe-a8c0-5c5c91538a06'></a>

52