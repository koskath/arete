<a id='6b19b32f-6ccc-4246-8630-cc5c215f3bb5'></a>

5. `Url pattern` must be configured according to the Thinger.io user ID and our bucket name.

*   The pattern should be like
    `https://api.thinger.io/v1/users/{user_id}/buckets/{bucket_id}/data`.
*   The `{user_id}` and `{bucket_id}` must be changed to match the account. For example, the final URL pattern will be
    `https://api.thinger.io/v1/users/alvarolb/buckets/SmartEverything/data`.
    Note that Sigfox variables can also be used to compose the URL; for instance, to store data from each device in a different bucket, a URL could be created:
    `https://api.thinger.io/v1/users/alvarolb/buckets/{device}/data`.
6. `HTTP Method` should be set to POST.
7. In `Headers` we must include an `Authorization` header with our device token in order to authenticate the bucket write request.
*   Header name should be `Authorization`
*   Header value should be `Bearer {access_token}`, where the `{access_token}` token is generated in the previous steps.
*   This is the example final header value. Note the space between `Bearer` and the token itself:

    ```
    Bearer
    eyJhbGci0iJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGki0iJTbWFydEV2ZX
    J5dGhpbmciLCJ1c3Ii0iJhbHZhcm9sYiJ9.0Qb48c_ToBiIVcC0dvXU2Kn5
    1mTnGLDcN44shVRzN1s
    ```
8. The final step is to configure the `Body` and its `Content type`. For content type, we will set `application/json` as the bucket can store arbitrary JSON data. The body will then contain all the information we want to store, formatted in JSON. In Sigfox, the body can be defined using available variables, which include those provided by the platform (such as device ID, link quality, or device location) and those defined by the payload configuration. In our case, we defined variables `temp`, and `hum`, that will be included with other Sigfox variables. For this example, the payload is:

<a id='3073ac0b-0b32-47c0-a3ac-d47a14e38d51'></a>

6