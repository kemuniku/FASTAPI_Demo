from fastapi import FastAPI, Depends
import uvicorn

from schemas import PostSubmission
from models import SubmissionModel
from settings import SessionLocal

from sqlalchemy.orm import Session


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# データベースからToDo一覧を取得するAPI
@app.get("/todo")
def get_todo(
        db: Session = Depends(get_db)
    ):
    # query関数でmodels.pyで定義したモデルを指定し、.all()関数ですべてのレコードを取得
    return db.query(SubmissionModel).all()

# submissionを追加するAPI
@app.post("/submission")
def post_todo(
        submission: PostSubmission, 
        db: Session = Depends(get_db)
    ):
    # 受け取ったtitleからモデルを作成
    db_model = SubmissionModel(id=submission.id,
                               epoch_second=submission.epoch_second,
                               problem_id=submission.problem_id,
                               contest_id=submission.contest_id,
                               user_id=submission.user_id,
                               language = submission.language,
                               point = submission.point,
                               length = submission.length,
                               result = submission.result,
                               execution_time = submission.execution_time)
    # データベースに登録（インサート）
    db.add(db_model)
    # 変更内容を確定
    db.commit()

    return {"message": "success"}

# ToDoを削除するAPI
@app.delete("/todo/{id}")
def delete_todo(
        id: int,
        db: Session = Depends(get_db)
    ):
    delete_todo = db.query(SubmissionModel).filter(SubmissionModel.id==id).one()
    db.delete(delete_todo)
    db.commit()

    return {"message": "success"}

@app.delete("/submission/alldelete")
def delete_all(
    db: Session = Depends(get_db)
    ):
    db.query(SubmissionModel).delete()
    db.commit()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")