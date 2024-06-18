import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
from radon.complexity import cc_visit
from radon.metrics import h_visit, mi_visit
from radon.raw import analyze

app = Flask(__name__, static_folder="static")

load_dotenv(dotenv_path=".env")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

chat_history = []

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/analyze", methods=["POST"])
def analyze_code():
    code = request.json["code"]
    result = analyze_refactored_code(code)
    return jsonify(result)

@app.route("/refactor", methods=["POST"])
def refactor_code():
    code = request.json["code"]
    global chat_history
    chat_history = []
    chat_history.append({"role": "system", "content": "You are a code refactoring assistant, skilled in refactoring code without changing its functionality. You only give a refactored functioning python code without any explanation or anything else."})
    chat_history.append({"role": "user", "content": f"Refactor the given Python program to a more readable, efficient, and maintainable one. You can assume that the given program is semantically correct. Do not change the external behavior of the program, and keep the syntactic and semantic correctness. Do not explain anything in natural language.: {code}"})
    try:
        response = client.chat.completions.create(
            model = "gpt-4",
            messages = chat_history
        )
        refactored_code = response.choices[0].message
        chat_history.append({"role": "assistant", "content": refactored_code.content})
        return jsonify({"refactored_code": refactored_code.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/refactor_again", methods=["POST"])
def refactor_again():
    chat_history.append({"role": "user", "content": f"Refactor again but even better."})
    try:
        response = client.chat.completions.create(
            model = "gpt-4",
            messages = chat_history
        )
        further_refactored_code = response.choices[0].message
        analysis = analyze_refactored_code(further_refactored_code.content)
        chat_history.append({"role": "assistant", "content": further_refactored_code.content})
        return jsonify({"further_refactored_code": further_refactored_code.content, "analysis": analysis})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def calculate_cyclomatic_complexity(code):
    return sum(block.complexity for block in cc_visit(code))

def calculate_lines_of_code(code):
    return analyze(code).loc

def calculate_maintainability_index(code):
    return round(mi_visit(code, multi=True), 2)

def calculate_halstead_metrics(code):
    h_metrics = h_visit(code).total
    h_metrics_filtered = {
        "volume": round(h_metrics.volume, 2),
        "difficulty": round(h_metrics.difficulty, 2),
        "effort": round(h_metrics.effort, 2)
    }
    return h_metrics_filtered

def analyze_refactored_code(code):
    complexity = calculate_cyclomatic_complexity(code)
    loc = calculate_lines_of_code(code)
    maintainability_index = calculate_maintainability_index(code)
    halstead_metrics = calculate_halstead_metrics(code)
    result = {
        "cyclic_complexity": complexity,
        "loc": loc,
        "maintainability_index": maintainability_index,
        "halstead_volume": halstead_metrics["volume"],
        "halstead_difficulty": halstead_metrics["difficulty"],
        "halstead_effort": halstead_metrics["effort"]
    }
    print_analysis_results(result)
    return result

def print_analysis_results(results):
    print("\nAnalysis Results:")
    print(f"Cyclomatic Complexity: {results['cyclic_complexity']}")
    print(f"Lines of Code: {results['loc']}")
    print(f"Maintainability Index: {results['maintainability_index']}")
    print(f"Halstead Volume: {results['halstead_volume']}")
    print(f"Halstead Difficulty: {results['halstead_difficulty']}")
    print(f"Halstead Effort: {results['halstead_effort']}")

if __name__ == "__main__":
    app.run(debug=True)
