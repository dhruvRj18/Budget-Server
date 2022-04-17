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
            bank_name=user_updated['bank_name'],
            contact=user_updated['contact'],
            current_balance=user_updated['current_balance'],
            display_name=user_updated['display_name'],
            email=user_updated['email'],
            image_url=user_updated['image_url'],
            primary_bank=user_updated['primary_bank'],
            initial_balance = user_updated['initial_balance'],
            password = user_updated['password']
        )
    except Exception as e:
        print(e)
        return None

def delete_user(user:Dict)->str:
    user.delete()
    return user.delete()
