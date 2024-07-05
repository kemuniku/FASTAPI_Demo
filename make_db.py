# submissionを追加するAPI
from fastapi import FastAPI, Depends
from settings import SessionLocal
from models import SubmissionModel
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

f = open('submissions.csv', 'r',encoding="utf-8")
i = 0
db = SessionLocal()
for s in f:
    
    i += 1
    splits = s.rstrip().split(",")
    if splits[0] == "id":
        continue
    #print(splits)
    if splits[9] == "":
        splits[9] = "-1"
    # 受け取ったtitleからモデルを作成
    db_model = SubmissionModel(id=int(splits[0]),
                               epoch_second=int(splits[1]),
                               problem_id=splits[2],
                               contest_id=splits[3],
                               user_id=splits[4],
                               language = splits[5],
                               point = splits[6],
                               length = int(splits[7]),
                               result = splits[8],
                               execution_time =int(splits[9]))
    # データベースに登録（インサート）
    db.add(db_model)
    # 変更内容を確定
    if i %100000 == 0:
        print(i)
        db.commit()
        db = SessionLocal()
