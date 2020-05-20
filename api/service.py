import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json
import requests
import sys

from playlistdata import playlistData
from profiledata import profileData
from h5weapons import H5Weapons

apiKey = '2da3fcfc1ed84e639ce64260025b74d7'
defaultUser = 'Brando006'
headers = {
    # Request headers

    'Ocp-Apim-Subscription-Key': apiKey,
}
params = urllib.parse.urlencode({
})

connectionUrl = 'https://www.haloapi.com'

def getRequestUrl(user):
    return f'/profile/h5/profiles/{user}/appearance?'

def getProfileDict(user):
    response = requests.get(f'{connectionUrl}{getRequestUrl(user)}', headers=headers) 
    return response.json()

##testUser = profileData(profileDict.get('GamerTag'),profileDict.get('ServiceTag'),profileDict.get('Company').get('Name'),profileDict.get('Company').get('Id'))
# for some reason the above wont work even though there is a dictionary key called Gamertag

def getUserData(user):
    profileDict = getProfileDict(user)
    testUser = profileData(user, profileDict.get('ServiceTag'), profileDict.get('Company').get('Name'), profileDict.get('Company').get('Id'))
    return f"Gamertag: {testUser.gamerTag}, ServiceTag: {testUser.serviceTag}, CompanyId: {testUser.companyId}, CompanyName: {testUser.companyName}"

# playlistURL = '/metadata/h5/metadata/playlists'
# response = requests.get(connectionUrl+playlistURL, headers=headers)
# playlists = response.json()
# playlistList = []
# count = 0
# for x in playlists:
#     match = playlistData(playlists[count].get('name'), playlists[count].get('description'), playlists[count].get('isRanked'), playlists[count].get(
#         'imageUrl'), playlists[count].get('gameMode'), playlists[count].get('isActive'), playlists[count].get('id'), playlists[count].get('contentId'))
#     playlistList.append(match)
#     count = count + 1
# print(len(playlistList))
# for gameType in playlistList:
#     print(gameType.name, gameType.description)

"""mStatsUrl = '/stats/h5/servicerecords/arena?players=' + testUser.gamerTag
response = requests.get(connectionUrl+mStatsUrl, headers=headers)
matchStatsDict = response.json()
print(matchStatsDict.keys())
print(matchStatsDict.get('Results'))
"""
