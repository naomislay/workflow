import tweepy


# Set up your Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create a Twitter API object
api = tweepy.API(auth)

# Define the username (screen name) of the Twitter account you want to retrieve data from
screen_name = "OrangeMaroc"

try:
    # Get the user's Twitter profile
    user = api.get_user(screen_name=screen_name)

    # Retrieve the number of tweets, likes (favorites), and followers
    tweets_count = user.statuses_count
    likes_count = user.favourites_count
    followers_count = user.followers_count

    # Print the retrieved information
    print(f"Username: @{screen_name}")
    print(f"Number of Tweets: {tweets_count}")
    print(f"Number of Likes (Favorites): {likes_count}")
    print(f"Number of Followers: {followers_count}")

except tweepy.error.TweepError as e:
    print(f"Error: {e}")
