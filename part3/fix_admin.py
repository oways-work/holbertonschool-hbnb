from app import create_app, db
from app.models.user import User
from flask_bcrypt import Bcrypt

# Initialize the app context to access the REAL database
app = create_app()
bcrypt = Bcrypt(app)

with app.app_context():
    print(f"Connected to database: {app.config['SQLALCHEMY_DATABASE_URI']}")

    # 1. Find the existing admin user
    admin = User.query.filter_by(email='admin@hbnb.io').first()
    
    # 2. If admin exists, delete them to start fresh
    if admin:
        print("Found existing Admin user. Deleting...")
        db.session.delete(admin)
        db.session.commit()

    # 3. Create a NEW Admin user with a fresh password hash
    # We generate the hash right here to ensure it works
    hashed_password = bcrypt.generate_password_hash('admin1234').decode('utf-8')
    
    new_admin = User(
        email='admin@hbnb.io',
        password=hashed_password,
        first_name='Admin',
        last_name='HBNB',
        is_admin=True
    )
    
    db.session.add(new_admin)
    db.session.commit()
    print("✅ SUCCESS: Admin user reset! Login with 'admin@hbnb.io' / 'admin1234'")
