# import library
import requests
from pprint import pprint
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# array file and variable global
arr_file = ['/etc/passwd', '/etc/shadow', '/etc/hosts', '/etc/crontab']
url = 'https://zabbix.naixo.com/zabbix/api_jsonrpc.php'
global auth
global hostid

# json for zabbix api
headers = {
    'content-type': 'application/json',
}

login = {
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "Admin",
        "password": "zabbix"
    },
    "id": 1
}

get_host = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid"],
        "filter": {
            "host": [
                "www.naixo.com"
            ]}
    },
    "auth": "",
    "id": 2
}

create_item = {
    "jsonrpc": "2.0",
    "method": "item.create",
    "params": {
        "name": "",
        "key_": "",
        "hostid": "",
        "type": 2,
        "value_type": 4,
        "delay": "30s"
    },
    "auth": "",
    "id": 1
}

create_trigger = {
  "jsonrpc": "2.0",
  "method": "trigger.create",
  "params": {
    "description": "",
    "expression": "{www.naixo.com:change-file-[etc/passwd].diff()}=1"
  },
  "auth": "",
  "id": 1
}

logout = {
    "jsonrpc": "2.0",
    "method": "user.logout",
    "params": [],
    "id": 1,
    "auth": ""
}
# function
# function generate md5 file
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# function login and get auth
def login_Zabbix():
    res  = requests.post(url, data=json.dumps(login), headers=headers, verify=False)
    res = res.json()
    pprint(res)
    auth_tmp = res[u'result']
    auth_tmp = auth_tmp.encode('ascii', 'replace')
    return auth_tmp
    
# gethost
def gethost():
    get_host["auth"] = auth
    print get_host
    res  = requests.post(url, data=json.dumps(get_host), headers=headers, verify=False)
    res = res.json()
    pprint(res)
    hostid = res['result'][0]
    hostid = hostid['hostid']
    hostid = hostid.encode('ascii', 'replace')
    return hostid

# fuction logout user zabbix
def logout_Zabbix():
    logout["auth"] = auth
    print logout
    res  = requests.post(url, data=json.dumps(logout), headers=headers, verify=False)
    res = res.json()
    pprint(res)

# fucntion create items
def modAndCreateItem(file):
    create_item['params']['name'] = 'File ' + file + ' changed!'
    create_item['params']['key_'] = 'change-file-['+ file +']'
    create_item['params']['hostid'] = hostid
    create_item['auth'] = auth
    print "============================================================"
    print create_item
    res  = requests.post(url, data=json.dumps(create_item), headers=headers, verify=False)
    res = res.json()
    pprint(res)

# fucntion create trigger
def modAndCreateTrigger(file):
    create_trigger['params']['description'] = "Change file ["+ file +"]"
    create_trigger['params']['expression'] = "{www.naixo.com:change-file-["+ file +"].diff()}=1"
    create_trigger['auth'] = auth
    print "======================================="
    print create_trigger
    res  = requests.post(url, data=json.dumps(create_trigger), headers=headers, verify=False)
    res = res.json()
    pprint(res)


auth = login_Zabbix()
hostid = gethost()
for file in arr_file:
    modAndCreateItem(file)
    modAndCreateTrigger(file)
logout_Zabbix()
