from fastapi import APIRouter

router = APIRouter()

'''
Endpoint for user registration
'''
@router.post("auth/register")
def register():
    pass

'''
Endpoint for user to login
'''
@router.post("auth/login")
def login():
    pass

'''
Endpoint to automatically login the user
'''
@router.get("auth/me")
def currentUser():
    pass
