<a id='05b68aec-3ea4-4cea-a9c2-8f1e8faa4906'></a>

## Dashboard Settings

Layout Share **Developer** Placeholders Functions Controls

option Dashboard Configuration: [ ]

{} JSON

```json
{
"controls": {
"aggregation": {
"auto": true,
"period": "1m"
},
"timespan": {
"magnitude": "minute",
"mode": "relative",
"period": "latest",
"value": 30
}
},
"description": "Example Dashboard for documentation",
"functions": "function convertFunction(value to series()) (
}
```

Cancel Save

<a id='db7d53bd-e873-4147-bef8-fbf777abcb79'></a>

Developer tab in dashboard settings

<a id='9511191c-c76b-47a9-9ec8-d1eabec04abc'></a>

# Placeholders

Dashboard placeholders allow defining variables to be used in any part of the dashboard by using their placeholder name inside double braces. The value can be extracted from a device property or set manually.

<a id='193f63b7-688d-4f63-a940-e5c4974d397c'></a>

62