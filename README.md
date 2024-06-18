# How to run code

- add .env with Openai API key as OPENAI_API_KEY in /app folder
- run app.py 


### Imports 

- flask
- openai
- radon


## Prepare test data and automated testing of these

- /documents
    - /009: raw source code files from Aizu Online Judge (http://developers.u-aizu.ac.jp/index)
    - *_submission_records_0000000_0999999.csv*: includes submission records with meta data
    - *analysis_\**: includes all the metrics data for each test code 
- /script
    - *prepare_test_code.py*: filters all functioning Python3 code out of the raw source code files and saves them in /test_code folder
    - *validate_test_code.py*: tests whether all the Python3 code in /test_code folder actually work -> manually: removing none funtioning code
    - *evaluation_test*: automation of refactoring of a selection of test codes (currently 9 files); saves all the mertrics for evaluation in /documents/*analysis_\*.csv*
    - *create_plot.py*: creates plots (*\<plotname\>.png*) for evaluation
- /test-code
    - /Python2: Python2 source code files
    - /Python3: Python3 source code files
    - /selected: a selection of manually random picked Python3 code files for testing 
    - *test_code\*.py*: a bad Python3 code generated from ChatGPT for testing
