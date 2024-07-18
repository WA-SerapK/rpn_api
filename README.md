# RPN API

## Description

The RPN (Reverse Polish Notation) API is a Flask application that allows you to manage stacks and apply basic arithmetic operations (addition, subtraction, multiplication, division) on these stacks.

## Prerequisites

- Python 3.9+

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/rpn_api.git
   cd rpn_api
   ```

2. Install the dependencies:
    ```
   pip install -r requirements.txt
   ```

3. Run the application:
    ```
   flask --app main run
   ```
   If you want to enable debug mode, add --debug to the command:
   ```
   flask --app main run --debug
   ```

4. Run the tests:
    ```
   pytest --cov=app tests/
   ```
   
5. Run pylint on your project:
   ```
   pylint app
   ``` 