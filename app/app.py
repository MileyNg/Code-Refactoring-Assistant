from flask import Flask, request, jsonify, send_from_directory
import openai
from radon.complexity import cc_visit
from radon.metrics import h_visit, mi_visit
from radon.raw import analyze

app = Flask(__name__, static_folder='static')

openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/analyze', methods=['POST'])
def analyze_code():
    code = request.json['code']
    result = analyze_refactored_code(code)
    return jsonify(result)

@app.route('/refactor', methods=['POST'])
def refactor_code():
    code = request.json['code']
    refactored_code = code
    # refactored_code = openai.Completion.create(
    #     engine="gpt-4",
    #     prompt=f"Refactor the given Python program to a more readable, efficient, and maintainable one. You can assume that the given program is semantically correct. Do not change the external behavior of the program, and keep the syntactic and semantic correctness. Python programs should be in a code block. Do not explain anything in natural language.: {code}",
    #     max_tokens=1024
    # ).choices[0].text
    return jsonify({'refactored_code': refactored_code})

# @app.route('/refactor_again', methods=['POST'])
# def refactor_again():
#     original_code = request.json['original_code']
#     refactored_code = request.json['refactored_code']
#     combined_prompt = f"Refactor this code again but better considering the following previous refactor: \nOriginal Code: {original_code}\nRefactored Code: {refactored_code}"
#     further_refactored_code = combined_prompt
#     # further_refactored_code = openai.Completion.create(
#     #     engine="gpt-4",
#     #     prompt=combined_prompt,
#     #     max_tokens=1024
#     # ).choices[0].text
#     analyze_refactored_code(further_refactored_code)
#     return jsonify({'further_refactored_code': further_refactored_code})

@app.route('/refactor_again', methods=['POST'])
def refactor_again():
    original_code = request.json['original_code']
    refactor_history = request.json['refactor_history']
    combined_prompt = f"Refactor the given Python program to a more readable, efficient, and maintainable one. You can assume that the given program is semantically correct. Do not change the external behavior of the program, and keep the syntactic and semantic correctness. Python programs should be in a code block. Do not explain anything in natural language.:\n {original_code}\n"
    for i, refactor in enumerate(refactor_history):
        j = i + 1
        combined_prompt += f"Refactor again but even better {j}:\n {refactor}\n"
    further_refactored_code = combined_prompt
    # combined_prompt = "Can you refactor the code even better:\n"
    # for i, code in enumerate(refactor_history):
    #     combined_prompt += f"Refactor {i+1}: {code}\n"
    # further_refactored_code = openai.Completion.create(
    #     engine="gpt-4",
    #     prompt=combined_prompt,
    #     max_tokens=1024
    # ).choices[0].text
    # analyze_refactored_code(further_refactored_code)    
    return jsonify({'further_refactored_code': further_refactored_code})

def calculate_cyclomatic_complexity(code):
    return sum(block.complexity for block in cc_visit(code))
   # return ComplexityVisitor.from_code(code).functions

def calculate_lines_of_code(code):
    return analyze(code).loc

def calculate_maintainability_index(code):
    return round(mi_visit(code, multi=True), 2)

def calculate_halstead_metrics(code):
    h_metrics = h_visit(code).total
    h_metrics_filtered = {
        'volume': round(h_metrics.volume, 2),
        'difficulty': round(h_metrics.difficulty, 2),
        'effort': round(h_metrics.effort, 2)
    }
    return h_metrics_filtered

def analyze_refactored_code(code):
    complexity = calculate_cyclomatic_complexity(code)
    loc = calculate_lines_of_code(code)
    maintainability_index = calculate_maintainability_index(code)
    halstead_metrics = calculate_halstead_metrics(code)
    result = {
        'cyclic_complexity': complexity,
        'loc': loc,
        'maintainability_index': maintainability_index,
        'halstead_volume': halstead_metrics['volume'],
        'halstead_difficulty': halstead_metrics['difficulty'],
        'halstead_effort': halstead_metrics['effort']
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

if __name__ == '__main__':
    app.run(debug=True)
