# SemiProject v1b

## 프로젝트에 사용한 모듈들
+ FastAPI, uvicorn
+ Jinja2
+ sqlalchemy

## 프로젝트 기본구조
+ 설정(db server) : dbfactory, settings
+ model ( db - table) : Member
+ schema (유효성검사) : NewMember
+ service (CRUD - 기능구현) : MemberService
+ route (url - 접점제공) : member_router
+ frontend (데이터 입력 / 전송) : join.html
