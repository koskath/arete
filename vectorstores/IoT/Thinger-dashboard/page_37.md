<a id='9b2a65bf-3cba-424b-8e06-f7db2120ab5d'></a>

option helloWidget.js: [x]
option helloWidget.html: [ ]

<a id='1494d278-78c4-4fd1-ada9-fa9617e6692c'></a>

```javascript
angular.module('helloWidget', [])
.directive('helloWidget', function () {
  return {
    restrict: 'EA',
    scope: {
      source : "=",
      ts: "=",
      value: "="
    },
    templateUrl: function() {
      let url =
        document.querySelector("script[src*='helloWidget.js']");
      return url.src.replace('.js','.html');
    },
    controller: ["$scope", function ($scope) {
      console.log("controller initialized! scope is",
        $scope);

      // listeners for process source changes (if
      // required)
      $scope.$watch('source', function (newVal, oldVal) {
        console.log("Source has changed:", newVal,
          oldVal);
      });

      // listeners for process value changes (if
      // required)
      $scope.$watch('value', function (newVal, oldVal) {
        console.log("Value has changed:", newVal,
          oldVal);
      });
    }]
  }
});
```

<a id='75fbb0d3-4a7d-435a-a040-de56f463dc78'></a>

- Create a new widget pointing to the `helloWidget.js` file. Note that we are loading the file with the `.js` extension that will load the counterpart `.html` file as specified in `templateUrl` function.

<a id='57f37063-50bd-47ba-9490-f82f9647c8bf'></a>

43