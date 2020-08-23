import time
import requests


print("What is the ID of the user you're trying to fetch?")
userID = input()

print(f"Searching roblox for a user with the ID of {userID}")
time.sleep(2.5)


def getRequest(self, rbxID):
    ourRequest = requests.get(f"https://api.roblox.com/users/{rbxID}")
    jsonRequest = ourRequest.json()

    errorBoolean = returnError(jsonRequest)
    if not errorBoolean:
        userPrecense = "Online"

        if not jsonRequest["IsOnline"] == True:
            userPrecense = "Offline"

        return {
            "username": jsonRequest["Username"],
            "id": jsonRequest["Id"],
            "precense": userPrecense
        }


def returnError(res):
    err = res.get("errors")
    if not err:
        return False
    else:
        print("User not Found!")
        exit()


request = getRequest((), userID)
print(request)
