import argparse
import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI

import uvicorn

from api.routes import router
from api.utils.rabbitmq_manager_factory import RabbitMQFactory
from api.utils.rabbitmq_manager_factory import RabbitMQManager as FactoryRabbitMQManager
from api.utils.rabbitmq_manager_singleton import RabbitMQManagerSingleton

parser = argparse.ArgumentParser(description="Run FastAPI server with specified environment.")
parser.add_argument("--env", default="development", choices=["development", "homolog", "production"], help="Environment to use.")
args = parser.parse_args()
load_dotenv(f".env.{args.env}")

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    global rabbitmq_manager_singleton
    rabbitmq_manager_singleton = RabbitMQManagerSingleton()
    await rabbitmq_manager_singleton.get_rabbitmq_manager().create_connection()

@app.on_event("shutdown")
async def shutdown_event():
    global rabbitmq_manager_singleton
    await rabbitmq_manager_singleton.get_rabbitmq_manager().close_connection()

app.include_router(router=router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)
