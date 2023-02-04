from app.database import SessionLocal
from app.models import User
import json

db = SessionLocal()

data = json.load(open("users.json"))

for user in data:
    newUser = User(
        firstName = user["FirstName"],
        lastName = user["LastName"],
        age = user["Age"],
        city = user["City"],
        portrait = user["Portrait"]
    )
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

db.close()