<a id='0933d691-5ec4-4fae-9bb1-ef8bfccf04a8'></a>

≡ thinger.io ⬜

<a id='04f002d8-639b-4d56-a182-e81f33a87486'></a>



<a id='fab626c6-4dc3-4bc0-bcb1-95729ac768be'></a>

<li class="right-items">
<li class="right-items">
<li class="right-items">
</ul>
</nav>
<section id="intro-section">
<article id="intro-section--text">
![waving hand](images/icons/waving-hand.png)
<h1 class="section--header">
Hey, ik ben Arnold!
</h1>
<p class="section--text">
Ik ben een front-end developer en student
</p>
<a href="#work--section" class="pink-button scroll">
</article>
![Arnold Francisca](images/hero-pf.jpg)
</section>

<a id='a09c33a3-aeda-471c-a45f-4c4d841d0bcc'></a>

CODING GUIDE

<a id='bf051427-14be-440a-a5b6-f448ac519c70'></a>

<::transcription of the content
: Button with GitHub Octocat icon, "Edit" text, and a dropdown arrow::>

<a id='3d559f0d-e9eb-442c-8994-0c73b7c15901'></a>

# Sketch Overview

Almost all Arduino Sketches share a common structure, consisting of a `setup` method and a `loop` method. This structure remains unchanged when integrating with Thinger.io. However, it is important to understand where device resources should be defined and where interaction with external services is possible. In general terms, any device resource (such as an LED, relay, sensor, or servo) must be defined inside the `setup()` method. Similar to initializing devices, setting the input/output direction of a digital pin, or initializing the Serial port speed, resources also need to be initialized here. This essentially involves configuring which values or resources are to be exposed over the Internet.

<a id='41486192-36f6-46a6-a757-882d65e222eb'></a>

The `loop()` is the designated place to consistently call the `thing.handle()` method, allowing the Thinger libraries to manage the platform connection. This method also serves as the location for calling endpoints or streaming real-time data to a dashboard. It is important to avoid adding any delays within the `loop()` unless specific actions, such as working with deep sleep modes on a device, are being implemented. Any other delay will negatively impact Thinger's proper functioning on the device. Additionally, reading a sensor value in every loop iteration can be detrimental if the sensor requires significant time to complete a read, as this will lead to a device with noticeable lag when responding to commands.

<a id='88dc711d-8e6f-42fd-82d0-f201f00db973'></a>

1