__author__ = 'gperkinson'
import socket
import dns.resolver
import dns.reversename

# Basic query
for rdata in dns.resolver.query('www.yahoo.com', 'CNAME'):
    print rdata.target
for rdata in dns.resolver.query('www.yahoo.com', 'MX'):
    print rdata.target
n = dns.reversename.from_address("8.8.8.8")
print n
print dns.reversename.to_address(n)

#reply=dns.resolver.query('www.yahoo.com', 'MX')
#for rdata in reply:
#    print 'Host', rdata.exchange, 'has pref', rdata.preference

