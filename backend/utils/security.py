# When we gonna hash our passwords
from passlib.context import CryptContext

# Let initialise the password hashing 
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

# Let define our hash function
def hash_password(password:str) -> str:
    return pwd_context.hash(password[:72])

# Now let verify  that the password had been hash correctly 

def verify_password(plain_password:str,hashed_password:str) -> bool:
    return pwd_context.verify(plain_password[:72],hashed_password)