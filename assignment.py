import json
with open('in.json',"r") as f:
    lst=json.loads(f.read())                 #reading data from file
    count=0
    for i in lst:
        print(json.dumps(lst[i],indent=0))   #parsing data upto 3 findings
        print()
        count += 1
        if count==3:                         # we can add any variable here and ask user for how many entries they want
            break
