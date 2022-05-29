from typing import Dict, List, Optional

from mongoengine.errors import (
    NotUniqueError,
    ValidationError,
)
from  budget_server.odm import User

def create_user(user:Dict)-> Optional[User]:
    try:
        return User(**user).save()
    except (NotUniqueError,ValidationError):
        return None


def get_users() -> List[User]:
    return User.objects()

def get_user_by_id(user_id:str)-> Optional[User]:
    try:
        return User.objects(id=user_id)
    except Exception as e:
        return None

def update_user_by_id(user:Dict,user_updated:Dict)-> Optional[User]:
    try:
        return user.update(
            bank_name=user_updated['bankName'],
            current_balance=user_updated['currentBalance'],
            display_name=user_updated['name'],
            email=user_updated['email'],
            profileImageFilePath=user_updated['profileImageFilePath'],
            primary_bank=user_updated['primaryBank'],
            initial_balance = user_updated['initialBalance'],
        )
    except Exception as e:
        print(e)
        return None

def delete_user(user:Dict)->str:
    user.delete()
    return user.delete()
