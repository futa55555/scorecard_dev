# backend/seeds/member_profiles.py

from backend import models

def seed_member_profiles(db):
    member_profiles = [
        
    ]
    db.add_all(member_profiles)
    db.commit()
