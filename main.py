from fastapi import FastAPI

# 127.0.0.1:000 서버 실행
app = FastAPI()

# @ ->  python 데코레이터 : 파이썬 함수에 추가적인 기능을 부여하는 문법

# GEt / 요청이 들어오면, root_handler라는 함수를 실행하라 
@app.get("/")
def root_handler():
    return {"ping": "pong"}


# Get / hello 요청이 들어오면, hello_handler() 실행 
@app.get("/hello")
def hello_handler():
    return {"message" : "Hello from FastAPI!"}


# 전체 사용자 목록 조회 API
# GET /users
@app.get("/users")
def get_users_handler():
    return [??????
        {"id": 1, "name": "alex", "job": "student"},
        {"id": 2, "name": "bob", "job": "sw engineer"},
        {"id": 3, "name": "chris", "job": "barista"},
    ]

users = []????
        {"id": 1, "name": "alex", "job": "student"},
        {"id": 2, "name": "bob", "job": "sw engineer"},
        {"id": 3, "name": "chris", "job": "barista"},
]

# 단일 사용자 데이터 조회 API
# GET/ users/1 -> 1번 사용자 데이터 조회 
@app.get("/users/1")
def get_user_one_handler():
    return{"id": 1, "name": "alex", "job": "student"}

# GET/ users/2 -> 2번 사용자 데이터 조회 
@app.get("/users/2")
def get_user_one_handler():
    return{"id": 2, "name": "bob", "job": "sw engineer"}

# GET/ users/3 -> 3번 사용자 데이터 조회 
@app.get("/users/3")
def get_user_one_handler():
    return{"id": 3, "name": "chris", "job": "barista"}

# GET/ users/{user_id} -> {user_id}번 사용자 데이터 조회 
@app.get("/users/{user_id")
def get_user_handler(user_id: int):
    for user in users:
        if user ["id"]: == user_id:
        return user
    
    # return None
