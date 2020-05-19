
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json
import requests
import sys

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

class playlistData:
    def __init__(self, name, description, isRanked, imageUrl, gameMode, isActive, id, contentId):
        self.name = name
        self.description = description
        self.isRanked = isRanked
        self.imageUrl = imageUrl
        self.gameMode = gameMode
        self.isActive = isActive
        self.id = id
        self.contentId = contentId

playlistURL = '/metadata/h5/metadata/playlists'
response = requests.get(connectionUrl+playlistURL, headers=headers)
playlists = response.json() 
playlistList = []
count = 0
for x in playlists:
    match = playlistData(playlists[count].get('name'),playlists[count].get('description'),playlists[count].get('isRanked'),playlists[count].get('imageUrl'),playlists[count].get('gameMode'),playlists[count].get('isActive'),playlists[count].get('id'),playlists[count].get('contentId'))
    playlistList.append(match)
    count = count + 1
##print(len(playlistList))

mStatsUrl = '/stats/h5/servicerecords/arena?players=' + testUser.gamerTag
response = requests.get(connectionUrl+mStatsUrl, headers=headers)
matchStatsDict = response.json()
##print(matchStatsDict.keys())
##print(matchStatsDict.get('Results'))



class H5Weapons:
    def __init__(self,name,description,weaponType,largeIconImageUrl,smallIconImageUrl,isUsableByPlayer,weaponId,contentId):
        self.name = name
        self.description = description
        self.weaponType = weaponType
        self.largeIconImageUrl = largeIconImageUrl
        self.smallIconImageUrl = smallIconImageUrl
        self.isUsableByPlayer = isUsableByPlayer
        self.weaponId = weaponId
        self.contentId = contentId

weaponListURL = '/metadata/h5/metadata/weapons'
weaponResponse = requests.get(connectionUrl+weaponListURL, headers=headers)
weaponsList = weaponResponse.json()
weaponsDict = []
wCount = 0
for w in weaponsList:
    weapon = H5Weapons(weaponsList[wCount].get('name'),weaponsList[wCount].get('description'),weaponsList[wCount].get('type'),weaponsList[wCount].get('largeIconImageUrl'),weaponsList[wCount].get('smallIconImageUrl'),weaponsList[wCount].get('isUsableByPlayer'),weaponsList[wCount].get('id'),weaponsList[wCount].get('contentId'))
    weaponsDict.append(weapon)
    wCount += 1
for s in weaponsDict:
    if s.name == 'Sniper Rifle':
        print(s.name,s.description,s.weaponType,s.weaponId)
        break




