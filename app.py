from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Function to check syntax
def check_syntax(language, code):
    try:
        if language == "python":
            result = subprocess.run(["python3", "-m", "py_compile", "-"], input=code, text=True, capture_output=True, check=True)
        elif language == "cpp":
            result = subprocess.run(["g++", "-fsyntax-only", "-xc++", "-"], input=code, text=True, capture_output=True, check=True)
        elif language == "java":
            result = subprocess.run(["javac", "-"], input=code, text=True, capture_output=True, check=True)
        elif language == "javascript":
            try:
                compile(code, "<string>", "exec")
                return {"result": "✅ No syntax errors found!", "error": False}
            except SyntaxError as e:
                return {"result": f"❌ Syntax Error: {e}", "error": True}
        else:
            return {"result": "❌ Unsupported language!", "error": True}

        return {"result": "✅ No syntax errors found!", "error": False}
    except subprocess.CalledProcessError as e:
        return {"result": f"❌ Syntax Error: {e.stderr}", "error": True}

@app.route("/check-syntax", methods=["POST"])
def check():
    data = request.get_json()
    language = data.get("language")
    code = data.get("code")
    
    if not language or not code:
        return jsonify({"result": "❌ Missing input!", "error": True})

    result = check_syntax(language, code)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
