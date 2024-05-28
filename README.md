
# Code Generation with OpenAI

This project uses OpenAI's language model to generate code snippets based on user-provided tasks and programming languages using Langchain Expressin Language.

## Requirements

- Python 3.7+

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/code-generation-openai.git
    cd code-generation-openai
    ```

2. **Install the required Python libraries:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Create a `.env` file:**

    ```sh
    touch .env
    ```

4. **Add your OpenAI API key to the `.env` file:**

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

Run the script with the desired task and programming language:

```sh
python main.py --task "your task" --language "your language"
```

### Arguments

- `--task`: The task you want the language model to perform. (Default: "Oops! you forgot to give a task")
- `--language`: The programming language for the code generation. (Default: "Oops! you forgot to give a language")

## Example

```sh
python generate_code.py --task "create a REST API" --language "Python"
```

This will generate Python code to create a REST API.
