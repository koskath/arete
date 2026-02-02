<a id='34159ec5-c9d8-440c-a30a-a6c3ad8ac799'></a>

*   **Check interval**: Is used to define how frequently the system evaluates the conditions set in a rule to determine if an alarm should be triggered. It allows users to adjust the check interval based on the specific needs of their monitoring setup.

<a id='2744328b-2c41-407c-93ab-412b905d7bb3'></a>

Note that setting an appropriate check interval helps balance the frequency of evaluations with system resource usage. In scenarios requiring high responsiveness, a shorter interval may be chosen, while less critical scenarios may use a longer interval. If the interval is too long, critical issues might not be detected promptly, while a very short interval may lead to excessive checks and potential performance impacts.

<a id='9e665c9c-a264-41ca-afa5-34db1a2d8486'></a>

# Rule definition

Este submenú permite especificar el comportamiento de la regla, especificando qué variables se van a monitorizar, cual es el valor de consigna y qué resultado tendrá cuando se produzcan evaluaciones positivas de la condición. También se especifica el comportamiento de desactivación de la regla.

<a id='ce728e11-bc76-4749-a3f1-56c54e5f7b84'></a>

# Data sources
This section allows users to specify which data sources will be evaluated by the rule. Data sources may include data from buckets, device properties, or the device status (allowing also to monitor device disconnections).

<a id='bd3a244c-60a8-4d7d-9df7-5384235b1265'></a>

<::tab_navigation::>option Data Source: [x] (icon: stacked rectangles)option Activation: [ ] (icon: bell)option Normalization: [x] (icon: checkmark)option Reminder: [ ] (icon: calendar)<::/tab_navigation::> <::tab_navigation::>option Data1: [x] (icon: grey circle)option Data2: [ ] (icon: grey circle)<::/tab_navigation::> Name (icon: info) <::input_field::>Data1 (icon: three vertical dots)<::/input_field::> Data Source (icon: info) <::dropdown::>From Data Bucket<::/dropdown::> Data Bucket (icon: info) <::dropdown::>Select Bucket Environmental data<::/dropdown::> <::buttons::>Add Source (icon: plus)Clone Source (icon: copy)Remove Source (icon: trash can)<::/buttons::>

<a id='4450718f-fec7-4a3a-966f-f6e6e981e9b6'></a>

4