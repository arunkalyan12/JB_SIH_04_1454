from urllib.parse import urlparse,urlencode
import ipaddress
import re

import whois as whois

# 1.Domain of the URL (Domain)
def getDomain(url):
  domain = urlparse(url).netloc
  if re.match(r"^www.",domain):
	       domain = domain.replace("www.","")
  return domain

"""

Checks for the presence of IP address in the URL. URLs may have IP address instead of domain name. If an IP address 
is used as an alternative of the domain name in the URL, we can be sure that someone is trying to steal personal 
information with this URL. 

If the domain is part of the URL has IP address, the value assigned to this feature is 1 (phishing) or 0 (legitimate)
"""

#check the IP address in URL (Have_IP)
def havingIP(url):
    try:
        ipaddress.ip_address(url)
        ip = 1
    except:
        ip = 0
    return ip

"""Check for presence of @ in URL as having it leads browser to ignore everything proceeding the @ symbol and real 
address follows after that symbol.

If '@' symbol is present set value assigned to this feature as 1 (phishing) or 0 (legitimate).
"""

#check for presence of '@' symbol
def haveAtSign(url):
    if "@" in url:
        at = 1
    else:
        at = 0
    return at

"""
Computes the length of the URL. Phishers use long url to hide doubtful part of address. We will set any address 
grater than equal to 54 characters then URL is classified as phishing else legitimate.

If length >= 54, value assigned to this feature as 1 (phishing) or 0 (legitimate).
"""

#Check length of url
def getLength(url):
    if len(url) < 54:
        length = 0
    else:
        length = 1
    return length

"""
Computes the depth of the URL. This calculates number of sub pages in url based on '/'.

Value of the feature is numerical based on URL.
"""

# 5.Gives number of '/' in URL (URL_Depth)
def getDepth(url):
    s = urlparse(url).path.split('/')
    depth = 0
    for j in range(len(s)):
        if len(s[j]) != 0:
            depth = depth +1
    return depth

"""Checks presence of "//" in URL. The "//" will redirect to another website and location of this is computed. If URL 
has http the "//" will come in 5th location and if https then in 6th position.

If "//" is at eny position after protocol, value assigned to this feature as 1 (phishing) or 0 (legitimate).
"""

# 6.Checking for redirection '//' in the url (Redirection)
def redirection(url):
    pos = url.rfind('//')
    if pos > 6:
        if pos > 7:
            return 1
        else:
            return 0
    else:
        return 0

"""Checks for presence of "http/https" in domain part of URL. The phishers may add "HTTPS" to domain part of a URL in 
order to trick users.
 
 If URL has "http/https" in domian port, value assigned to this feature as 1 (phishing) or 0 (legitimate).
 """

# 7.Existence of “HTTPS” Token in the Domain Part of the URL (https_Domain)
def httpDomain(url):
    domain = urlparse(url).netloc
    if 'https' in domain:
        return 1
    else:
        return 0

"""URL shortening is method of "World Wide Web" in which URL may be made considerably smaller in length and still 
lead to required webpage. If this is present there will be "HTTPS" but redirects to a page with a larger URL. 

If the URL is using Shortening Services, the value assigned to this feature is 1 (phishing) or else 0 (legitimate).
"""

#listing shortening services
shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"

# 8. Checking for Shortening Services in URL (Tiny_URL)
def tinyURL(url):
    match=re.search(shortening_services,url)
    if match:
        return 1
    else:
        return 0


"""Checking for '-' In domain of url, dash symbol is rarely used in legitimate URLs. Fishers tend to ad prefix or 
suffixes separate by (-) to domain so user feel they are dealing with legitimate page.

If the URL has '-' symbol in the domain part of the URL, the value assigned to this feature is 1 (phishing) or else 
0 (legitimate).
"""

# 9.Checking for Prefix or Suffix Separated by (-) in the Domain (Prefix/Suffix)
def prefixSuffix(url):
    if '-' in urlparse(url).netloc:
        return 1            # phishing
    else:
        return 0            # legitimate


"""
Many features can be extracted come under this category.Out of them below are features used in project.

*   DNS Record
*   Website Traffic 
*   Age of Domain
*   End Period of Domain

Each of these features are explained and the coded below:
"""

#!pip install python-whois

#importhing required packages for this section

import re
from bs4 import BeautifulSoup
#import whois
import urllib
import urllib.request
from datetime import datetime

"""
For phishing websites, either claimed identity is not recognised by WHOIS database or no records founded for hostname.

If the DNS record is empty or not found then, the value assigned to this feature is 1 (phishing) or else 0 (legitimate).
"""

# 11.DNS Record availability (DNS_Record)
# obtained in the featureExtraction function itself

"""This feature measures the popularity of the website by determining the number of visitors and the number of pages 
they visit. However, since phishing websites live for a short period of time, they may not be recognized by the Alexa 
database (Alexa the Web Information Company., 1996). By reviewing our dataset, we find that in worst scenarios, 
legitimate websites ranked among the top 100,000. Furthermore, if the domain has no traffic or is not recognized by 
the Alexa database, it is classified as “Phishing”.

If the rank of the domain < 100000, the vlaue of this feature is 1 (phishing) else 0 (legitimate).
"""

# 12.Web traffic (Web_Traffic)

import urllib

def web_traffic(url):
  try:
    #Filling the whitespaces in the URL if any
    url = urllib.parse.quote(url)
    rank = BeautifulSoup(urllib.request.urlopen(("http://data.alexa.com/data?cli=10&dat=s&url=" + url), "xml").find(
        "REACH")['RANK'])
    rank = int(rank)
  except TypeError:
        return 1
  if rank <100000:
    return 1
  else:
    return 0

"""#### **3.2.3. Age of Domain**

This feature can be extracted from WHOIS database. Most phishing websites live for a short period of time. The 
minimum age of the legitimate domain is considered to be 12 months for this project. Age here is nothing but 
different between creation and expiration time. 

If age of domain > 12 months, the vlaue of this feature is 1 (phishing) else 0 (legitimate).
"""

# 13.Survival time of domain: The difference between termination time and creation time (Domain_Age)
def domainAge(domain_name):
  creation_date = domain_name.creation_date
  expiration_date = domain_name.expiration_date
  if (isinstance(creation_date,str) or isinstance(expiration_date,str)):
    try:
      creation_date = datetime.strptime(creation_date,'%Y-%m-%d')
      expiration_date = datetime.strptime(expiration_date,"%Y-%m-%d")
    except:
      return 1
  if ((expiration_date is None) or (creation_date is None)):
      return 1
  elif ((type(expiration_date) is list) or (type(creation_date) is list)):
      return 1
  else:
    ageofdomain = abs((expiration_date - creation_date).days)
    if ((ageofdomain/30) < 6):
      age = 1
    else:
      age = 0
  return age

"""#### **3.2.4. End Period of Domain**

This feature can be extracted from WHOIS database. For this feature, the remaining domain time is calculated by 
finding the different between expiration time & current time. The end period considered for the legitimate domain is 
6 months or less  for this project. 

If end period of domain > 6 months, the vlaue of this feature is 1 (phishing) else 0 (legitimate).
"""

# 14.End time of domain: The difference between termination time and current time (Domain_End)
def domainEnd(domain_name):
  expiration_date = domain_name.expiration_date
  if isinstance(expiration_date,str):
    try:
      expiration_date = datetime.strptime(expiration_date,"%Y-%m-%d")
    except:
      return 1
  if (expiration_date is None):
      return 1
  elif (type(expiration_date) is list):
      return 1
  else:
    today = datetime.now()
    end = abs((expiration_date - today).days)
    if ((end/30) < 6):
      end = 0
    else:
      end = 1
  return end

"""## **3.3. HTML and JavaScript based Features**

Many features can be extracted that come under this category. Out of them, below mentioned were considered for this project.

*   IFrame Redirection
*   Status Bar Customization
*   Disabling Right Click
*   Website Forwarding

Each of these features are explained and the coded below:
"""

# importing required packages for this section
import requests

"""### **3.3.1. IFrame Redirection**

IFrame is an HTML tag used to display an additional webpage into one that is currently shown. Phishers can make use 
of the “iframe” tag and make it invisible i.e. without frame borders. In this regard, phishers make use of the 
“frameBorder” attribute which causes the browser to render a visual delineation. 

If the iframe is empty or repsonse is not found then, the value assigned to this feature is 1 (phishing) or else 
0 (legitimate).
"""

# 15. IFrame Redirection (iFrame)
def iframe(response):
  if response == "":
      return 1
  else:
      if re.findall(r"[<iframe>|<frameBorder>]", response.text):
          return 0
      else:
          return 1

"""

Phishers may use JavaScript to show a fake URL in the status bar to users. To extract this feature, we must dig-out 
the webpage source code, particularly the “onMouseOver” event, and check if it makes any changes on the status bar 

If the response is empty or onmouseover is found then, the value assigned to this feature is 1 (phishing) or else 
0 (legitimate).
"""

# 16.Checks the effect of mouse over on status bar (Mouse_Over)
def mouseOver(response):
  if response == "" :
    return 1
  else:
    if re.findall("<script>.+onmouseover.+</script>", response.text):
      return 1
    else:
      return 0

"""

Phishers use JavaScript to disable the right-click function, so that users cannot view and save the webpage source 
code. This feature is treated exactly as “Using onMouseOver to hide the Link”. Nonetheless, for this feature, 
we will search for event “event.button==2” in the webpage source code and check if the right click is disabled. 

If the response is empty or onmouseover is not found then, the value assigned to this feature is 1 (phishing) or else 0 (legitimate).
"""

# 17.Checks the status of the right click attribute (Right_Click)
def rightClick(response):
  if response == "":
    return 1
  else:
    if re.findall(r"event.button ?== ?2", response.text):
      return 0
    else:
      return 1

"""The fine line that distinguishes phishing websites from legitimate ones is how many times a website has been 
redirected. In our dataset, we find that legitimate websites have been redirected one time max. On the other hand, 
phishing websites containing this feature have been redirected at least 4 times. """

# 18.Checks the number of forwardings (Web_Forwards)
def forwarding(response):
  if response == "":
    return 1
  else:
    if len(response.history) <= 2:
      return 0
    else:
      return 1


# Function to extract features
def FeatureExtraction(url,label):
    features = []
    # Address bar based features (10)
    features.append(getDomain(url))
    features.append(havingIP(url))
    features.append(haveAtSign(url))
    features.append(getLength(url))
    features.append(getDepth(url))
    features.append(redirection(url))
    features.append(httpDomain(url))
    features.append(tinyURL(url))
    features.append(prefixSuffix(url))

    # Domain based features (4)
    dns = 0
    try:
        domain_name = whois.whois(urlparse(url).netloc)
    except:
        dns = 1

    features.append(dns)
    features.append(web_traffic(url))
    features.append(1 if dns == 1 else domainAge(domain_name))
    features.append(1 if dns == 1 else domainEnd(domain_name))

    # HTML & Javascript based features
    try:
        response = requests.get(url)
    except:
        response = ""

    features.append(iframe(response))
    features.append(mouseOver(response))
    features.append(rightClick(response))
    features.append(forwarding(response))
    features.append(label)

    return features

def FeatureExtraction_main(url):
    features = []
    # Address bar based features (10)
    #features.append(getDomain(url))
    features.append(havingIP(url))
    features.append(haveAtSign(url))
    features.append(getLength(url))
    features.append(getDepth(url))
    features.append(redirection(url))
    features.append(httpDomain(url))
    features.append(tinyURL(url))
    features.append(prefixSuffix(url))

    # Domain based features (4)
    dns = 0
    try:
        domain_name = whois.whois(urlparse(url).netloc)
    except:
        dns = 1

    features.append(dns)
    features.append(web_traffic(url))
    features.append(1 if dns == 1 else domainAge(domain_name))
    features.append(1 if dns == 1 else domainEnd(domain_name))

    # HTML & Javascript based features
    try:
        response = requests.get(url)
    except:
        response = ""

    features.append(iframe(response))
    features.append(mouseOver(response))
    features.append(rightClick(response))
    features.append(forwarding(response))

    return features


# converting the list to dataframe
feature_names = ['Domain', 'Have_IP', 'Have_At', 'URL_Length', 'URL_Depth', 'Redirection',
                 'https_Domain', 'TinyURL', 'Prefix/Suffix', 'DNS_Record', 'Web_Traffic',
                 'Domain_Age', 'Domain_End', 'iFrame', 'Mouse_Over', 'Right_Click', 'Web_Forwards', 'Label']

