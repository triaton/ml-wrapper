from fastapi import FastAPI
import base64
from pydantic import BaseModel

class ParseImageDto(BaseModel):
    data: str

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'The API server is working!'}

@app.post('/api/parse')
async def send_email(payload: ParseImageDto):
    raw_data = payload.data
    parsed = base64.b64decode(raw_data)
    # TODO: integrate your ml part here
    # for now I am sending the parsed image into a byte string
    return {'success': True, 'data': str(parsed)}
