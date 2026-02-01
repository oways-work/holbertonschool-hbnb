import requests
import uuid

BASE_URL = "http://127.0.0.1:5000/api/v1"

def run_test():
    # 1. Create a User (Author of the review)
    print("🔹 Creating Reviewer User...")
    user_payload = {
        "first_name": "Reviewer",
        "last_name": "One",
        "email": f"reviewer_{uuid.uuid4()}@test.com",
        "password": "password123"
    }
    user_res = requests.post(f"{BASE_URL}/users/", json=user_payload)
    if user_res.status_code != 201:
        print(f"❌ User creation failed: {user_res.text}")
        return
    user_id = user_res.json()['id']
    print(f"✅ User Created: {user_id}")

    # 2. Create a Place (To be reviewed)
    # We need an owner for the place first
    owner_payload = {
        "first_name": "Owner",
        "last_name": "Two",
        "email": f"owner_{uuid.uuid4()}@test.com",
        "password": "password123"
    }
    owner_res = requests.post(f"{BASE_URL}/users/", json=owner_payload)
    owner_id = owner_res.json()['id']

    print("🔹 Creating Place...")
    place_payload = {
        "title": "Cozy Cabin",
        "description": "Nice place",
        "price": 50.0,
        "latitude": 10.0,
        "longitude": 20.0,
        "owner_id": owner_id
    }
    
    # Need to login to create place? (If protected). Assuming open for now based on previous tests.
    # Getting token for Owner just in case
    auth_res = requests.post(f"{BASE_URL}/auth/login", json={"email": owner_payload['email'], "password": "password123"})
    token = auth_res.json()['access_token']
    headers = {"Authorization": f"Bearer {token}"}

    place_res = requests.post(f"{BASE_URL}/places/", json=place_payload, headers=headers)
    if place_res.status_code != 201:
        print(f"❌ Place creation failed: {place_res.text}")
        return
    place_id = place_res.json()['id']
    print(f"✅ Place Created: {place_id}")

    # 3. Post a Review
    print("🔹 Posting a Review...")
    review_payload = {
        "text": "Amazing stay! Highly recommended.",
        "rating": 5,
        "user_id": user_id,
        "place_id": place_id
    }
    
    # Using User's token (Reviewer)
    auth_res_user = requests.post(f"{BASE_URL}/auth/login", json={"email": user_payload['email'], "password": "password123"})
    user_token = auth_res_user.json()['access_token']
    user_headers = {"Authorization": f"Bearer {user_token}"}

    review_res = requests.post(f"{BASE_URL}/reviews/", json=review_payload, headers=user_headers)
    if review_res.status_code != 201:
        print(f"❌ Review creation failed: {review_res.text}")
        return
    print(f"✅ Review Created!")

    # 4. Fetch Reviews for the Place
    print("🔹 Fetching Reviews for the Place...")
    reviews_res = requests.get(f"{BASE_URL}/places/{place_id}/reviews")
    reviews_data = reviews_res.json()
    
    if len(reviews_data) > 0 and reviews_data[0]['text'] == "Amazing stay! Highly recommended.":
        print("🎉 SUCCESS! Review successfully retrieved from place.")
    else:
        print(f"❌ FAILED. Reviews found: {reviews_data}")

if __name__ == "__main__":
    run_test()
