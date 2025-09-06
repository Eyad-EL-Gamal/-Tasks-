empty_dict = {}
contacts = {"eyad":1557971685,
            "mohamed":1245879624,
            "sara":1154962574,}
print(contacts.keys())
search = ("eyad")
if ("eyad") in contacts :
    print(contacts["eyad"])
else:
    print(False)
#-------------------------------
students = [{"name":"ahmed","grades":[80,85,90]},
            {"name":"salma","grades":[95,70,85]},
            {"name":"omar","grades":[75,80,85]}]
for x in students :
    avg = sum(x["grades"]) / len(x["grades"])
    print(avg)