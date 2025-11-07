def lambda_handler(event, context=None):
    name = event.get("name", "World")
    return {
        "statusCode": 200,
        "body": f"Hello, {name}! This is a Serverless Function."
    }

# Chạy thử cục bộ
if __name__ == "__main__":
    event = {"name": "Alice"}
    print(lambda_handler(event))
