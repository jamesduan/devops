# encoding:utf8

import json

OPENSTACK_ADMIN_AUTH = {
	'host' : '10.0.0.101',
	'user' : 'openstack' ,
	'password' : 'magima.1',
}

OPSSERVER = {
	'host' : '10.0.0.142',
	'user' : 'mtagent',
	'password' : 'magima.1'
}

with open('../../../juarez/scripts/role/orc_paas.json', 'r') as f:
	jsondata = f.read()

j = json.loads(jsondata)
IPS = []
for key, val in j.items():
	IPS.append(key)

#CS_IMAGEUID = '7506540b-8218-4276-97b4-1fd33b3717b3'
#CC_IMAGEUID = '5dd38526-3767-4603-a756-a2a44291711d'

# pqa new 
CC_IMAGEUID = '420ba99e-d185-4bc3-8b9e-945490ac3721'

# clientenv
#NODE1 = '9b1639b4-f9e0-4ba9-82f6-ecab7aecdaac'
#NODE2 = 'c35d23a4-0097-4acd-8858-3c1e27b02d36'
#NODE3 = '4af7fab2-d2c4-4d1f-bcbc-564aae81c2b3'

# pqa new
NODE1 = 'bd1f54f0-63e9-4b50-ae1d-02d6a414b95c'
NODE2 = 'bb6f02b1-e8d9-4577-92a9-f462def9f501'
NODE3 = '20c2f4ba-c0e4-4c2c-b8b5-dff18b1f986e'
NODE4 = '71ae6721-2116-4611-813f-a0385ece2c83'
NODE5 = '09c91f26-e212-4654-aede-00489022472e'
BOC = '38ff3a41-0e31-4eb6-b1ba-559390355a44'

