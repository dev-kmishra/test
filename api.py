import json

from urllib.request import urlopen

with urlopen("https://api.covid19india.org/state_district_wise.json") as response:
    source=response.read()

#print(source)

data=json.loads(source)

with open('new_data.json','w') as states_file:
    json.dump(data,states_file,indent=3)

dictStates={}
dictStates={'states':data}

#print(dictStates)

for state in dictStates['states']:
     for i in dictStates['states'][state]['districtData']:
        print( state, 
     "    ", i,
     "     ", dictStates['states'][state]['districtData'][i]['confirmed'])
