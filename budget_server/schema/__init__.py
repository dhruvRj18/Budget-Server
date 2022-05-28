from .user import (
    UserCreateSchema,
    UserReturnSchema,
)
from .budget import (
    CreateBudgetSchema,
    BudgetReturnScema
)

user_create_schema = UserCreateSchema()
user_return_schema = UserReturnSchema()
users_return_schema = UserReturnSchema(many=True)
create_budget_schema = CreateBudgetSchema()
budget_return_schema = BudgetReturnScema()

__all__ = [
    users_return_schema,
    user_return_schema,
    user_create_schema,
    create_budget_schema,
    budget_return_schema,
]
