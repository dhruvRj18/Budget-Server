from typing import Dict, Optional

from marshmallow import ValidationError
from mongoengine import NotUniqueError

from budget_server.odm import Budget


def create_budget(budget:Dict)-> Optional[Budget]:
    try:
        return Budget(**budget).save()
    except (NotUniqueError,ValidationError):
        return None