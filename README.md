geoipLookup
===========
This is a command-line Python utility to lookup GeoIP attributes for a list of IP addresses. It uses the Maxminds binary databases (GeoIPCity.dat and GeoIPOrg.dat from https://www.maxmind.com/) and outputs the results in pipe delimited format.

Here's how I'm using this:

    cat ips.txt | python geoipLookup.py > geoipLookupResults.txt

where ips.txt is a text file containing a list of IP addresses. The output looks like this:

```
ip|org|isp|region_name|city|postal_code|country_code|country_code3|country_name|area_code|metro_code|latitude|longitude
54.74.74.12|Amazon.com|Amazon Technologies||Dublin|None|IE|IRL|Ireland|0|None|53.3331|-6.2489
192.168.1.1||||||||||||
79.74.74.12|Tiscali UK Limited|Tiscali UK Limited||None|None|GB|GBR|United Kingdom|0|None|51.5|-0.13
```

The pipe-delimited results can then easily be loaded into a database. The API calls to the binary database files are *much* faster than loading GeoIP lookup data into database tables and querying against them.
