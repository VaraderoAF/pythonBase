from fastapi import FastAPI


app = FastAPI()


@app.get("/ping/")
def ping():
    return{"message": "pong"}


# if __name__ == '__main__':
#     uvicorn.run(app)
