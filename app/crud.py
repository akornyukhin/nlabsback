from sqlalchemy.orm import Session

import models

def get_users(db: Session):
    return db.query(models.User).all()