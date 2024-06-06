from src.main.process_handle import main


def run(request):
    print(request)
    request_json = request.get_json()
    print(request_json)

    if request_json:
        document_id = request_json.get("document_id")
        action = request_json.get("action")
        if document_id and action:
            print(f"Received document_id: {document_id} with action: {action}")
            main(request_json)
            return f"Received document_id: {document_id} with action: {action}"
        else:
            print("Invalid request, missing 'document_id' or 'action'", 400)
            return "Invalid request, missing 'document_id' or 'action'", 400
    print("Invalid request", 400)
    return "Invalid request", 400

    return


# request = {"document_id": "QqG4NilZFYfq5T7hwlA1", "action": "analyze"}

# if __name__ == "__main__":
#     main(request)
