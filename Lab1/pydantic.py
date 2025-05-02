from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    account_id: int
    user = User(
    name = "Salah",
    email = "salah@gmail.com",
    account_id = 12345
)
    user_data = {
    'name': 'Salah',
    'email': 'salah@gmail.com',
    'account_id': 12345
}

user = User(**user_data)