from auth import create_access_token
from datetime import timedelta

def generate_token():
    token = create_access_token({"sub": "testuser"}, timedelta(minutes=30))
    print("Generated token:", token)

# python -c "import utils; utils.generate_token()"
