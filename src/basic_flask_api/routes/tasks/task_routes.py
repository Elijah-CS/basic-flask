from flask import Blueprint, request, jsonify
import logging

logger = logging.getLogger("basic_api.task_routes")
task_bp = Blueprint("tasks", __name__)

@task_bp.post("/api/v1/executeTask")
def task_execute():
    """
    Kick-off a Task
    ---
    tags:
        - tasks
    """
    logger.info(f"Handling request {request.path} {request.method}")

    return jsonify("Posting jobs"), 200

@task_bp.get("/api/v1/getTaskStatus")
def task_get():
    """
    Get the status of all or a specific Task
    ---
    tags:
        - tasks
    parameters:
        - in: query
          name: taskId
          required: false
          schema:
            type: str
          example: abc123
    """
    logger.info(f"Handling request {request.path} {request.method}")

    taskId = request.args.get("taskId")

    if not taskId:
        return jsonify("Got all jobs"), 200
    
    return jsonify(f"Gotten task {taskId}"), 200

@task_bp.delete("/api/v1/deleteTask")
def task_delete():
    """
    Delete a specific Task
    ---
    tags:
        - tasks
    parameters:
        - in: query
          name: taskId
          required: true
          schema:
            type: str
          example: abc123
    """
    logger.info(f"Handling request {request.path} {request.method}")

    taskId = request.args.get("taskId")

    if not taskId:
        return jsonify("Must provide taskId"), 400
    
    return jsonify(f"Deleted task {taskId}"), 200