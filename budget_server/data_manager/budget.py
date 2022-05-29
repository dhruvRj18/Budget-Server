from typing import Dict, Optional, List

from marshmallow import ValidationError
from mongoengine import NotUniqueError

from budget_server.odm import Budget


def create_budget(budget:Dict)-> Optional[Budget]:
    try:
        return Budget(**budget).save()
    except (NotUniqueError,ValidationError):
        return None

def read_budget_entries() -> List[Budget]:
    return Budget.objects().order_by('-date')