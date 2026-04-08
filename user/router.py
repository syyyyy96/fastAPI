from fastapi import APIRouter, Path, Query, status,  HTTPException

from database.connection import SessionFactory
from user.models import User
from user.request import UserCreateRequest, UserUpdateRequest
from user.response import UserResponse


# user핸들러 함수들을 묶어서 관리하는 객체
router = APIRouter(tags=["User"]) # or APIRouter(prefix="/users")

# 임시 데이터베이스
users = [
    {"id": 1, "name": "alex", "job": "student"},
    {"id": 2, "name": "bob", "job": "sw engineer"},
    {"id": 3, "name": "chris", "job": "barista"},
]

# 전체 사용자 목록 조회 API
# GET /users
@router.get("/users", status_code=status.HTTP_200_OK)
def get_users_handler():
    return users


# 사용자 정보 검색 API
# GET /users/search?name=alex
# GET /users/search?job=student
@router.get("/users/search")
def search_user_handler(
    name: str | None = Query(None),
    job: str | None = Query(None),
):
    if name is None and job is None:
        return {"msg": "조회에 사용할 QueryParam이 필요합니다."}
    return {"name": name, "job": job}


# 단일 사용자 데이터 조회 API
# GET /users/{user_id} -> {user_id}번 사용자 데이터 조회
@router.get("/users/{user_id}")
def get_user_handler(
    user_id: int = Path(..., ge=1),
):
    for user in users:
        if user["id"] == user_id:
            return user
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User Not Found",
    )

# 회원 추가 API 
# POST / users
@router.post(
        "/users", 
        status_code=status.HTTP_201_CREATED,
        response_model=UserResponse,
)
def create_user_handler(
    # 1) 사용자 데이터를 넘겨 받는다 + 형식에 맞는지 데이터 유효성 검사 
    body : UserCreateRequest
):
    # Context manager를 벗어나는 순간 자동으로 close() 호출 
    with SessionFactory() as session:
        new_user = User(name=body.name, job=body.job)
        session.add(new_user)
        session.commit() # 변경사항 저장 
        session.refresh(new_user) # id, created_at 읽어옴
        return new_user

    # 2) 사용자 데이터를 저장한다
    # new_user = {
    #    "id" : len(users) + 1,
    #    "name" : body.name,
    #    "job" : body.job,
#}
    #users.append(new_user)
    
    # 3) 응답을 반환한다. 
    #return new_user

    # return {"name": body.name, "job": body.job}
    


# 회원 정보 수정 API
# PUT : 전체 교체(replace)
# PATCH : 일부 수정(partial update) --> v 
# PATCH / users/ {user_id}
@router.patch(
        "/users/{user_id}",
        response_model=UserResponse,
)
def update_user_handler(
    # 1) 입력값 정의 : 클라이언트로부터 수정할 데이터를 넘겨 받는다 
    user_id : int,
    body : UserUpdateRequest,
):
    # 2) 처리 : user_id로 사용자 조회 -> 데이터 수정 
    for user in users:
        # user_id로 사용자 조회
        if user["id"] == user_id:
            # 데이터 수정 
            user["job"] == body.job
            # 3) 반환 
            return user
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User Not Found",
    )

# 회원 삭제 API
# DELETE / users/ {user_id}
@router.delete(
        "/users/{user_id}",
        status_code=status.HTTP_204_NO_CONTENT, # 삭제 후 반환할 데이터가 있다면 200으로 바꿔야함 
)
def delete_user_handler(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return 
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User Not Found",
    )








# /articles
# / posts
# / comments




