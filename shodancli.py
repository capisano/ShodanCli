#!/usr/bin/python
# -*- coding: utf-8 -*-
#original source from ninj4c0d3r
import Queue
import requests
import sys
import argparse
import shodan
import subprocess
# PATH
from os import path

# # # # ## 
#        #
# CONFIG #
#        #
# # # # ##

# KEY API
SHODAN_API_KEY = ""
api = shodan.Shodan(SHODAN_API_KEY)

# BANNER
def banner():
    print ("""
 _______ __             __               ______ _____   _______ 
|     __|  |--.-----.--|  |.---.-.-----.|      |     |_|_     _|
|__     |     |  _  |  _  ||  _  |     ||   ---|       |_|   |_ 
|_______|__|__|_____|_____||___._|__|__||______|_______|_______|
                                                                
""")


    
def helper():
    print ("By: dkr and @capisano ")
    print ("usage ./shodancli.py --shodan dork")
    print ""
    
 
def validateapi():
    if SHODAN_API_KEY == "":
        print ("INVALID SHODAN API KEY:")
        print ("Create a Account and Generate a new API KEY in https://account.shodan.io/login")
        sys.exit()    
    
    
# SHODAN SEARCH
def shodanSearch(dork):
    validateapi()
    
    try:
        results = api.search(dork)

        # PRINT RESULT
        print ""
        print ("###############[SHODAN RESULT]####################")
        print ""
        print 'Results Found: %s' % results['total']
        print ""
        
        if results['total'] == 0:
            sys.exit()
            
        for result in results['matches']:
                print ("###################[%s]#####################") % result['ip_str']
                print ""
                print '[HEADER] %s' % result['data']
                print '[IP] %s' % result['ip_str']
                print '[PORT] %s' % result['port']
                print '[Country] %s' % result['location']['country_code']
                print '[Region] %s' % result['location']['region_code']
                print '[City] %s' % result['location']['city']
                print ''
                response = raw_input('Continue ? [enter]: ')
                print ''
                print ''
    except shodan.APIError, e:
        print 'Error: %s' % e

def main():
    banner()
    
    target = ''
    passlist = ''
    username = ''

    #argumentos
    parser = argparse.ArgumentParser(description = "ShodanCli", add_help = False)
    parser.add_argument('-h', '--help', action=helper(), help='usage')
    parser.add_argument('-s', '--shodan',help='Give a dork to Shodan')
    args = parser.parse_args()

    if args.shodan != None:
        shodanSearch(args.shodan)

    try:    
        bruteforce(target,port)
    except:
        sys.exit()

main()
