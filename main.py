
import http.client, urllib.request, urllib.parse, urllib.error, base64, json, requests, sys
apiKey = '2da3fcfc1ed84e639ce64260025b74d7'
user = 'Brando006'
headers = {
    # Request headers
    
    'Ocp-Apim-Subscription-Key': apiKey,
}
params = urllib.parse.urlencode({
})


class profileData:
    def __init__(self,gamerTag,serviceTag,companyName,companyId):
        self.gamerTag = gamerTag
        self.serviceTag = serviceTag
        self.companyName = companyName
        self.companyId = companyId


connectionUrl = 'https://www.haloapi.com'
requestUrl = '/profile/h5/profiles/'+ user + '/appearance?'
response = requests.get(connectionUrl+requestUrl, headers=headers)
profileDict = response.json()


##testUser = profileData(profileDict.get('GamerTag'),profileDict.get('ServiceTag'),profileDict.get('Company').get('Name'),profileDict.get('Company').get('Id'))
## for some reason the above wont work even though there is a dictionary key called Gamertag

testUser = profileData(user,profileDict.get('ServiceTag'),profileDict.get('Company').get('Name'),profileDict.get('Company').get('Id'))
print(testUser.gamerTag, testUser.serviceTag,testUser.companyId, testUser.companyName)









