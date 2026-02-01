import requests

# --- CONFIGURATION ---
BASE_URL = "http://127.0.0.1:5000/api/v1"
AUTH_URL = f"{BASE_URL}/auth"
USER_URL = f"{BASE_URL}/users/"

# User credentials
EMAIL = "login@test.com"
PASSWORD = "securePass123"
FIRST_NAME = "Auth"
LAST_NAME = "User"

def register_user():
    """Registers the test user if not already present."""
    print("--- 1. Registering User ---")
    data = {
        "email": EMAIL,
        "password": PASSWORD,
        "first_name": FIRST_NAME,
        "last_name": LAST_NAME
    }
    response = requests.post(USER_URL, json=data)
    if response.status_code == 201:
        print("✅ User created successfully.")
    elif response.status_code == 400 and "Email already registered" in response.text:
        print("ℹ️  User already exists. Proceeding to login.")
    else:
        print(f"❌ Registration failed: {response.status_code}")
        print(response.json())
        exit(1)

def get_fresh_token():
    """Logs in and returns a valid access token."""
    print("\n--- 2. Logging In ---")
    login_url = f"{AUTH_URL}/login"
    response = requests.post(login_url, json={
        "email": EMAIL,
        "password": PASSWORD
    })
    
    if response.status_code == 200:
        token = response.json().get('access_token')
        print(f"🔑 Authentication Successful! Got token.")
        return token
    else:
        print(f"❌ Login Failed: {response.status_code}")
        print(response.json())
        exit(1)

def test_create_place(token):
    """Test: Create a place (Allowed for authenticated user)"""
    print("\n--- 3. Testing Place Creation (Authenticated) ---")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    url = f"{BASE_URL}/places/"
    data = {
        "title": "Auto-Token Place",
        "description": "Created with an automatically generated token",
        "price": 75.0,
        "latitude": 12.34,
        "longitude": 56.78,
        "owner_id": "ignored" 
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 201:
        print("✅ SUCCESS: Place created!")
        print(f"   Place ID: {response.json().get('id')}")
        print(f"   Owner ID: {response.json().get('owner_id')}")
    else:
        print(f"❌ FAILED: {response.status_code}")
        print(response.json())

def test_create_amenity_as_user(token):
    """Test: Create an Amenity (Restricted to Admin)"""
    print("\n--- 4. Testing Amenity Creation (Regular User) ---")
    print("ℹ️  This user is NOT an admin. We expect a 403 Forbidden.")
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    url = f"{BASE_URL}/amenities/"
    data = {"name": "VIP Lounge"}
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 403:
        print("✅ SUCCESS: Request was correctly blocked (403 Forbidden).")
    elif response.status_code == 201:
        print("⚠️  WARNING: Request succeeded (It shouldn't have)!") 
    else:
        print(f"ℹ️ RESULT: {response.status_code}")
        print(response.json())

if __name__ == "__main__":
    register_user()
    fresh_token = get_fresh_token()
    test_create_place(fresh_token)
    test_create_amenity_as_user(fresh_token)
