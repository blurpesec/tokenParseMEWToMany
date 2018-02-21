import json, requests, urllib
#Method 1 - Static
#mewJson = open('./tokens-eth.json').read()
#x = json.loads(mewJson);

#Method 2 - HTTP requests
url = 'https://raw.githubusercontent.com/MyEtherWallet/ethereum-lists/master/tokens/tokens-eth.json'
r = requests.get(url)
x = json.loads(r.content)

for count in range(0,500):
    try:
        print(x[count]['address'] + ' json is being created')
        addr = x[count]['address']
        tokenFile = addr + '.json'
        tokenFilePath = './tokens/' + tokenFile
        with open(tokenFilePath, "w") as outfile:
            json.dump(x[count], outfile, indent=4)
    except IndexError:
        print('End of json')
        break
