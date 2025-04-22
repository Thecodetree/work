import requests
import schedule
import time
import random

# LinkedIn developer account needed
# Access tokens needed continually
# Use Linkedin's OAuth2.0 flow to receive access tokens
# Remember that linkedin tokens expire
# Author_Urn is your linkedin profile urn 
# Python packages: requests, schedule, time needed
# pip install requests schedule needed

# Add your actual credentials & tokens below

Access_Token = "your access Token here"
Author_Urn = "urn: li:person:your profile id here"

Affirmations = [
    "Your first affirmation here"
    "Hey BOO Boo Insert your affirmation here"
    "I am inserting my affirmation here Yogi"
]

def post_affirmation():
    Affirmation = random.choice(Affirmations)
    print(f"[{datetime.now()}] Posting affirmation: {Affirmation}")
    
    headers = {
        "Authorization": f'Bearer {Access_Token}',
        "Content-Type": "Application/json",
        "X-Restli-Protocol-Version": "2.0.0"}
    
    post_data = {
        "author": Author_Urn
        "lifecyclestate": "Published",
        "SpecificContent": {
            "com.linkedin.ugc.ShareContent": {
                "ShareCommentary": {
                    "text": Affirmation},
                "shareMediaCategory": "None"}
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "Public"}
    }
    
    response = requests.post(
        "https://api.linkedin.com/v2/ugcPosts",
        headers=headers,
        json=post_data)
    
    if response.status_code ==201:
        print("Affirmation has posted successfully.")
    else: print(f"Failed to post affirmation. Status code: {response.status_code}")
    
    # This posts the affirmation once a day
    schedule.every().day.at("7:00").do(post_affirmation)
    
    # This keeps the scripts running
    while True:
            schedule.run_pending()
            time.sleep(60)