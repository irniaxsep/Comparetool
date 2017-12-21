import json

with open('uk.json') as uk_id:
    uk = json.load(uk_id)

with open('us.json') as us_id:
    us = json.load(us_id)


uk_spaces = [x['space_guid'] for x in uk['service_instances']]
us_spaces = [x['space_guid'] for x in us['service_instances']]


reader = open("spaceID.txt", "r+")
lines = reader.readlines()
#f = open("valid_id", "r+")
print 'Spaces in UK'
for line in lines:
    #print line
    line = line.strip('\n')
    if line in uk_spaces:
        print line
        #f.write()
        #f.close()
print 'Spaces in US'
for line in lines:
    line = line.strip('\n')
    if line in us_spaces:
        # us.write("valid_id_us")
        print line
        # us.close()

