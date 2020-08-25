'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''

# v1

def domain_name(url):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]

# v2
'''
from urllib.parse import urlparse

def domain_name(url):
    
    r = urlparse(url)
    
    if r.scheme == '':
        r = urlparse(f"http://{url}")
        
    return r.hostname.lstrip('www.').split('.')[0]
'''
