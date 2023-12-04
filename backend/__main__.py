from uvicorn import run
from os import getenv
from dotenv import load_dotenv

load_dotenv()

port = int(getenv('PORT'))

if __name__ == '__main__':
    run("app:api", port=port)