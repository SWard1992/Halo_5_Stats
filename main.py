
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
print(len(playlistList))
for gameType in playlistList:
    print(gameType.name,gameType.description)

"""mStatsUrl = '/stats/h5/servicerecords/arena?players=' + testUser.gamerTag
response = requests.get(connectionUrl+mStatsUrl, headers=headers)
matchStatsDict = response.json()
print(matchStatsDict.keys())
print(matchStatsDict.get('Results'))
"""










