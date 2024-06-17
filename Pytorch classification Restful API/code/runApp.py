import uvicorn
from app import app
import nest_asyncio

nest_asyncio.apply()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)