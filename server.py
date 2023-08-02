import argparse
from dotenv import load_dotenv
import uvicorn
from api.main import app
from config.environment import get_config

def load_environment(env):
    load_dotenv(f".env.{env}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run FastAPI server with specified environment.")
    parser.add_argument("--env", default="development", choices=["development", "homolog", "production"], help="Environment to use.")
    args = parser.parse_args()

    load_environment(args.env)

    config = get_config(args.env)

    uvicorn.run(app, host="0.0.0.0", port=8000)