#!/usr/bin/env python

import argparse
import geoip2.database
import pandas as pd
import sys

parser = argparse.ArgumentParser(description='Geolocate IP addresses')
parser.add_argument('--ip-address-file', dest='ip_address_file', action='store', help='file containing a IP addresses to lookup')
parser.add_argument('--ip-address-whitelist-file', dest='ip_address_whitelist_file', action='store', help='file whitelisted IP addresses')
parser.add_argument('--maxmind-db', dest='maxmind_db', action='store', help='Maxmind database file')
parser.add_argument('--output-csv', dest='output_csv', action='store', help='output CSV file')
args = parser.parse_args()

reader = geoip2.database.Reader(args.maxmind_db)

whitelist = set()
with open(args.ip_address_whitelist_file) as ip_address_whitelist_file:
    for line in ip_address_whitelist_file:
        ip = line.strip()
        whitelist.add(ip)

successful_lookups = 0
failed_lookups = 0

failed_lookup_ips = list()

ip_lookup_list = list()
with open(args.ip_address_file) as ip_address_file:

    for line in ip_address_file:

        try:
            ip = line.strip()
        except:
            ip = None

        lookup_failed = False
        response = None
        try:
            response = reader.city(ip)
        except:
            lookup_failed = True
            failed_lookups += 1

        try:
            city = response.city.name.encode('utf8')
        except:
            city = None

        try:
            subdivision = response.subdivisions.most_specific.name.encode('utf8')
        except:
            subdivision = None

        try:
            country = response.country.name.encode('utf8')
        except:
            country = None

        whitelisted = False
        if ip in whitelist:
            whitelisted = True

        record = {'ip': ip, 'city': city, 'subdivision': subdivision, 'country': country, 'whitelisted': whitelisted, 'lookup_failed': lookup_failed}
        ip_lookup_list.append(record)
        successful_lookups += 1


sys.stdout.write("successful lookups: {0}; failed lookups: {1}".format(successful_lookups, failed_lookups) + "\n")
sys.stdout.write("results output to {0}".format(args.output_csv))

dataframe = pd.DataFrame(ip_lookup_list, columns=['ip', 'city', 'subdivision', 'country', 'whitelisted', 'lookup_failed'])

dataframe.to_csv(args.output_csv, header=True, index=False, encoding='utf-8')

