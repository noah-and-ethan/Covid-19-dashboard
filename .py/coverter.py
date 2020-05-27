# convert.py - file io application to read in latest covid19 data and spit out Leaflet.js circles using string concatenation
# March 24, 2020: mhoel - original coding 
# added geojson - https://github.com/datasets/geo-countries/tree/master/data

# Access data from: https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports
# Korea, South - Bahamas, The - Gambia, The : Must be manually fixed in the data (South Korea, Bahamas, Gambia) 

# Read file in
fi = open("04-21-2020.csv","r")
fi.readline() # skip over first title line
datarows = fi.readlines()
fi.close()

# loop through all rows in the csv file
countries = []
numdeaths = []

for line in datarows:
    templist = line.split(",")
    FIPS = templist[0]
    Admin2 = templist[1]
    Province_State = templist[2].lower()
    country = templist[3].lower()
    Last_Update = templist[4]
    lat = templist[5]
    lon = templist[6]
    Confirmed = templist[7]
    deaths = templist[8]
    Recovered = templist[9]
    Active = templist[10]
    Combined_Key = templist[11]

#if (country == "canada"):
    #print(country)
    countries.append(country)
    numdeaths.append(deaths)
 
#print(countries.index('Canada'))
#print(numdeaths)


import json

with open('world_map.geojson') as f:
  data = json.load(f)

f.close()

for country in data["features"]:
    name = country["properties"]["name"].lower()
    try:
        i = countries.index(name)
        print(name)
        print(i)
        print(numdeaths[i])
        country["properties"]["deaths"] = numdeaths[i]
        print(country["properties"])
    except:
        print(name + " not found")
        country["properties"]["deaths"] = 0

with open('cloropleth.geojson', 'w') as json_file:
  json.dump(data, json_file)

json_file.close()
