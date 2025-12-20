from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

HOST = "localhost"
PORT = 8000
TASKS_FILE = "tasks.txt"

tasks = []
next_id = 1


def load_tasks():
    global tasks, next_id
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            tasks = json.load(f)
            if tasks:
                next_id = max(task["id"] for task in tasks) + 1


def save_tasks():
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


class TaskHandler(BaseHTTPRequestHandler):

    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        if data is not None:
            self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        if self.path == "/tasks":
            self._send_json(tasks)
        else:
            self.send_error(404)

    def do_POST(self):
        global next_id

        # Создание задачи
        if self.path == "/tasks":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            data = json.loads(body)

            task = {
                "id": next_id,
                "title": data["title"],
                "priority": data["priority"],
                "isDone": False
            }

            tasks.append(task)
            next_id += 1
            save_tasks()

            self._send_json(task, 200)
            return

        # Завершение задачи
        if self.path.startswith("/tasks/") and self.path.endswith("/complete"):
            try:
                task_id = int(self.path.split("/")[2])
            except (IndexError, ValueError):
                self.send_error(404)
                return

            for task in tasks:
                if task["id"] == task_id:
                    task["isDone"] = True
                    save_tasks()
                    self.send_response(200)
                    self.end_headers()
                    return

            self.send_error(404)
            return

        self.send_error(404)


if __name__ == "__main__":
    load_tasks()
    server = HTTPServer((HOST, PORT), TaskHandler)
    print(f"Server running at http://{HOST}:{PORT}")
    server.serve_forever()
