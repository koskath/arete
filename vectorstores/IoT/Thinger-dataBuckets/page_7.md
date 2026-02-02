<a id='0bdb2169-01f7-487a-a82b-9f9c7ecaa516'></a>

thinger.io

- Statistics
- Devices
- Dashboards
- Data Buckets
- Endpoints
- Alarms
- Access Tokens
- Assets >
- File Storages
- Products
- Projects
- Plugins
- Toolbox >

<a id='79de8e1c-d031-4983-8a7e-82ba7a28ab37'></a>

Administration
User Accounts
Cluster Hosts
Domains
Brands
OAuth2 Clients
Proxies
Billing

Account

<a id='065f5de2-59aa-459e-abbe-e8f8fb58510f'></a>

Menu icon | Folder icon | Statistics dropdown | Plus icon | Megaphone icon | user- | User profile icon

<a id='447017e8-1927-4d9a-9b2d-b4f2ec18ee83'></a>

user

<a id='2a8ab5fa-06aa-494f-bd70-efa467be3f93'></a>

Buckets > Add

### Bucket Details

#### Bucket Settings

Bucket Id: MQTTexample

#### Bucket Information

Bucket Name: from MQTT topic
Bucket Description: Bucket subscribed to MQTT Topic

#### Bucket Configuration

option Enabled: [x]
Data Tags: Type tags...
Data Source: From MQTT Topic
MQTT Topic: kitchen/temperature

#### Advanced Options

option Asset Type: [ ] Select Type...
option Asset Group: [ ] Select Group...
option Product: [ ] Select Product...

#### Database Options

Backend: MongoDB
Retention: 3 months

<a id='9ed9a5e1-4c52-4cff-b145-379d97188af3'></a>

option Add Bucket: [x]

<a id='d4913740-d835-40b4-a33b-8b03b82a4faa'></a>

i Note that the data buckets system has been created to store JSON format messages, so the data from the MQTT device must be in this format.

<a id='f10c2e34-2f70-4f57-bf7d-2d24768ae9bc'></a>

# Custom data timestamp

Thinger.io data bucket feature has been created using time series databases, The system has been programmed to store the data points using the timestamp of the instant they are stored in the database as the indexing variable, however, it is possible to customize this variable by entering a timestamp in the payload using this key-value structure:

<a id='150c5260-50c1-4c90-8bbf-c5188c34e3ba'></a>

7