geoip_lookup
============
This is a command-line Python utility to geolocate IP addresses using [Maxmind's](https://www.maxmind.com/) binary database (GeoIP2-City.mmdb).

The command takes 4 arguments:

* `--ip-address-file`: file containing IP addresses to lookup
* `--ip-address-whitelist-file`: file containing whitelisted IP addresses
* `--maxmind-db`: the Maxmind database file (i.e. the path to GeoIP2-City.mmdb)
* `--output-csv`: output CSV file

Here's an example:

    ./geoip_lookup.py --ip-address-file ip_addresses.txt --maxmind-db GeoIP2-City.mmdb --ip-address-whitelist-file ip_whitelist.txt --output-csv results.csv
