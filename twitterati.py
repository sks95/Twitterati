import tweepy  # open src library to access Twitter API

# declare variables of your Twitter developer account
consumer_key = ""
consumer_secret = ""
access_token = ""
access_toke_secret = ""

# creating a tweepy api object with 4 variables defined above
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_toke_secret)

api = tweepy.API(auth)
usr_id = input("Enter id to be searched: ")

try:
    # Check for invalid user id
    user = api.get_user(usr_id)
    print("Screen name: ", user.screen_name)
    print("User name: ", user.name)
    print("Descrition: ", user.description)
    print("Location: ", user.location)
    print("Time zone: ", user.time_zone)
    print("Number of followers: ", user.followers_count)
    print("Number of friends: ", user.friends_count)
    print("Number of statuses: ", user.statuses_count)
    print("User URL: ", user.url)

# If id is invalid
except Exception as e:
    print(e)
