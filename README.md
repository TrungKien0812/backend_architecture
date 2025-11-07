# backend_architecture
cd serverless
python handler.py
cd microservices
uvicorn user_service:app --port 8001 --reload
uvicorn product_service:app --port 8002 --reload
cd [other files]
uvicorn main:app --reload
