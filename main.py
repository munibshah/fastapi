from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World! Welcome", "message": "Welcome to FastAPI!"}


class WebhookPayload(BaseModel):
    EndTime: str

@app.post("/webhook/")
async def receive_webhook(data: WebhookPayload):
    # Extracting EndTime from the payload
    end_time = data.EndTime
    print(f"Received EndTime: {end_time}")
    return {"message": "Data received successfully", "EndTime": end_time}

