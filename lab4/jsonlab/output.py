import json
print("Interface Status\n================================================================================\nDN                                                 Description           Speed    MTU  \n-------------------------------------------------- --------------------  ------  ------")
json_list=open("C:\\Users\\ayan\\Desktop\\folder\\vscode\\python\\lab4\\jsonlab\\sample-json.json").read()
json_load=json.loads(json_list)
im_data=json_load["imdata"]
for i in im_data:
    dn=i["l1PhysIf"]["attributes"]["dn"]
    #id=i["l1PhysIf"]["attributes"]["id"]
    description=i["l1PhysIf"]["attributes"]["descr"]
    speed=i["l1PhysIf"]["attributes"]["speed"]
    mtu=i["l1PhysIf"]["attributes"]["mtu"]
    print("{0:50}{1:22}{2:10}{3:6}".format(dn,description,speed,mtu))