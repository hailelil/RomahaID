import os

# Define services and their basic structure
services = {
    "marda-identity": ["app/main.py", "app/models.py", "app/schemas.py", "app/crud.py", "app/api.py", "app/db.py", "app/__init__.py", "Dockerfile", "requirements.txt", "README.md"],
    "senai-profile": ["app/main.py", "app/models.py", "app/schemas.py", "app/crud.py", "app/api.py", "app/db.py", "app/__init__.py", "Dockerfile", "requirements.txt", "README.md"],
    "honey-card-generator": ["app.py", "utils/pdf_generator.py", "static/cards/.gitkeep", "requirements.txt", "Dockerfile", "README.md"],
    "honey-verify": ["app/main.py", "app/models.py", "app/schemas.py", "app/crud.py", "app/api.py", "app/db.py", "app/__init__.py", "Dockerfile", "requirements.txt", "README.md"],
    "roman-auth-server": ["docker-compose.yml", "keycloak-config/.gitkeep", "README.md"]
}

# Base FastAPI main.py content
fastapi_main_content = '''from fastapi import FastAPI

app = FastAPI(title="Romaha ID - Service")

@app.get("/health")
def health_check():
    return {"status": "ok"}
'''

# Base Flask app.py for Card Generator
flask_app_content = '''from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=6000, debug=True)
'''

# Create folders and files
for service, files in services.items():
    print(f"\n🚀 Creating service: {service}")
    for path in files:
        full_path = os.path.join("services", service, path)
        folder = os.path.dirname(full_path)
        os.makedirs(folder, exist_ok=True)

        # Initialize files
        if not os.path.exists(full_path):
            if path.endswith("main.py") and "honey-card-generator" not in service:
                content = fastapi_main_content
            elif path == "app.py":
                content = flask_app_content
            elif path.endswith(".gitkeep"):
                content = ""
            elif path.endswith("README.md"):
                content = f"# {service.replace('-', ' ').title()}\n\nService description.\n"
            else:
                content = "# TODO: implement\n"

            with open(full_path, "w") as f:
                f.write(content)

            print(f"✅ Created: {full_path}")

print("\n✅ All services scaffolded successfully!")
