class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class UserWithAddress(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    age: Optional[int] = None
    address: Address

# Thử nghiệm với UserWithAddress Model
create_user_with_address({
    "username": "john_doe",
    "email": "john@example.com",
    "full_name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip_code": "12345"
    }
})
