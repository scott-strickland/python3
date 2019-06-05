import requests
ip_range = ['192.168.50.75', '192.168.50.76', '192.168.50.80']


for ip in ip_range:
    try:
        url = 'http://' + ip
        r = requests.get(url, timeout=2)
        
    except requests.exceptions.ConnectionError:
        print(ip + ' is NOT responding on TCP port 80.')
    else:
        r.status_code == '200'
        print(ip + ' is responding on TCP port 80.')
    
