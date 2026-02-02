<a id='0a37f8ab-cc59-463f-b991-c20767949502'></a>

<table id="72-1">
<tr><td id="72-2">Option in the dropdown</td><td id="72-3">What it does</td><td id="72-4">Typical use-case</td></tr>
<tr><td id="72-5">None</td><td id="72-6">Leave the value untouched.</td><td id="72-7">Raw sensor read-outs.</td></tr>
<tr><td id="72-8">abs</td><td id="72-9">Returns the absolute value.</td><td id="72-a">Converting ± current readings into a unipolar magnitude.</td></tr>
<tr><td id="72-b">ceil</td><td id="72-c">Rounds up to the nearest integer.</td><td id="72-d">Guaranteeing that never display less than the true amount (e.g., inventory pieces).</td></tr>
<tr><td id="72-e">floor</td><td id="72-f">Rounds down to the nearest integer.</td><td id="72-g">Showing whole-number counts such as completed batches.</td></tr>
<tr><td id="72-h">round</td><td id="72-i">Rounds to the nearest integer.</td><td id="72-j">Tidying noisy decimals for dashboards aimed at non-technical audiences.</td></tr>
<tr><td id="72-k">difference</td><td id="72-l">Computes the delta between consecutive samples.</td><td id="72-m">Displaying incremental energy consumption from a cumulative meter.</td></tr>
<tr><td id="72-n">derivative</td><td id="72-o">Calculates the rate of change per second (can be negative).</td><td id="72-p">Turning distance into velocity or bytes into bandwidth.</td></tr>
<tr><td id="72-q">non_negative_derivative</td><td id="72-r">Same as derivative but clips negative spikes—handy when counters reset to 0.</td><td id="72-s">Network-interface byte counters, water meters that roll over.</td></tr>
<tr><td id="72-t">cumulative_sum</td><td id="72-u">Adds each new sample to a running total.</td><td id="72-v">Tracking production totals without changing the device firmware.</td></tr>
<tr><td id="72-w">elapsed</td><td id="72-x">Returns milliseconds/seconds since the previous data point.</td><td id="72-y">Measuring event spacing, e.g., time between machine cycles.</td></tr>
<tr><td id="72-z"></td><td id="72-A"></td><td id="72-B">Previous DATA BUCKETS</td></tr>
</table>
Next

<a id='f8881eb1-77be-4eba-842c-001be1d78406'></a>

73