from app.models.review import Review
from app import create_app, db
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity

# Initialize the app and context
app = create_app()

with app.app_context():
    # 1. create a User
    user = User(first_name="Alice", last_name="Wonder", email="alice@test.com", password="password123")
    db.session.add(user)
    db.session.commit()
    print(f"✅ User created: {user.first_name} (ID: {user.id})")

    # 2. Create a Place
    place = Place(title="Wonderland", description="Magic place", price=100.0, latitude=10.0, longitude=20.0, owner_id=user.id)
    db.session.add(place)
    db.session.commit()
    print(f"✅ Place created: {place.title} (ID: {place.id})")

    # 3. Create an Amenity
    amenity = Amenity(name="Invisibility Cloak")
    db.session.add(amenity)
    db.session.commit()
    print(f"✅ Amenity created: {amenity.name} (ID: {amenity.id})")

    # 4. Link them!
    print("🔗 Linking Amenity to Place...")
    place.add_amenity(amenity)
    db.session.commit()

    # 5. Verify
    # We reload the place from the DB to be sure
    fetched_place = Place.query.get(place.id)
    if len(fetched_place.amenities) > 0:
        print(f"🎉 SUCCESS! The place '{fetched_place.title}' has amenities: {[a.name for a in fetched_place.amenities]}")
    else:
        print("❌ FAILED. No amenities found.")
