from flask import Flask, request, jsonify, send_from_directory
import openai
from radon.complexity import cc_visit
from radon.metrics import mi_visit
from radon.raw import analyze
from radon.metrics import h_visit

app = Flask(__name__, static_folder='static')

openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze_code():
    code = request.json['code']
    complexity = calculate_cyclomatic_complexity(code)
    loc = calculate_lines_of_code(code)
    maintainability_index = calculate_maintainability_index(code)
    halstead_metrics = calculate_halstead_metrics(code)
    result = {
        'complexity': complexity,
        'loc': loc,
        'maintainability_index': maintainability_index,
        'halstead_metrics': halstead_metrics
    }
    print("Analysis Results:", result)
    return jsonify(result)

@app.route('/refactor', methods=['POST'])
def refactor_code():
    code = request.json['code']
    refactored_code = code + "HI"
    # refactored_code = openai.Completion.create(
    #     engine="gpt-4",
    #     prompt=f"Refactor the given Python program to a more readable, efficient, and maintainable one. You can assume that the given program is semantically correct. Do not change the external behavior of the program, and keep the syntactic and semantic correctness. Python programs should be in a code block. Do not explain anything in natural language.: {code}",
    #     max_tokens=1024
    # ).choices[0].text
    return jsonify({'refactored_code': refactored_code})

@app.route('/refactor_again', methods=['POST'])
def refactor_again():
    original_code = request.json['original_code']
    refactored_code = request.json['refactored_code']
    combined_prompt = f"Refactor this code considering the following previous refactor: \nOriginal Code: {original_code}\nRefactored Code: {refactored_code}"
    further_refactored_code = combined_prompt
    # further_refactored_code = openai.Completion.create(
    #     engine="gpt-4",
    #     prompt=combined_prompt,
    #     max_tokens=1024
    # ).choices[0].text
    analyze(further_refactored_code)
    return jsonify({'further_refactored_code': further_refactored_code})

# @app.route('/refactor_again', methods=['POST'])
# def refactor_again():
#     original_code = request.json['original_code']
#     refactor_history = request.json['refactor_history']
#     combined_prompt = "Can you refactor the code even better:\n"
#     for i, code in enumerate(refactor_history):
#         combined_prompt += f"Refactor {i+1}: {code}\n"
#     further_refactored_code = openai.Completion.create(
#         engine="gpt-4",
#         prompt=combined_prompt,
#         max_tokens=1024
#     ).choices[0].text
#     analyze_code_internal(further_refactored_code)
#     return jsonify({'further_refactored_code': further_refactored_code})

def calculate_cyclomatic_complexity(code):
    return sum(block.complexity for block in cc_visit(code))

def calculate_lines_of_code(code):
    return analyze(code).loc

def calculate_maintainability_index(code):
    return mi_visit(code, multi=True)

def calculate_halstead_metrics(code):
    return h_visit(code)

def analyze(code):
    complexity = calculate_cyclomatic_complexity(code)
    loc = calculate_lines_of_code(code)
    maintainability_index = calculate_maintainability_index(code)
    halstead_metrics = calculate_halstead_metrics(code)
    analysis_results = {
        'complexity': complexity,
        'loc': loc,
        'maintainability_index': maintainability_index,
        'halstead_metrics': halstead_metrics
    }
    print_analysis_results(analysis_results)
    return jsonify(analysis_results)

def print_analysis_results(results):
    print("\nAnalysis Results:")
    print(f"Cyclomatic Complexity: {results['complexity']}")
    print(f"Lines of Code: {results['loc']}")
    print(f"Maintainability Index: {results['maintainability_index']}")
    print(f"Halstead Metrics: {results['halstead_metrics']}")

if __name__ == '__main__':
    app.run(debug=True)
