import os
import argparse
from dotenv import load_dotenv
from operator import itemgetter
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

def load_environment_variables():
    """Load environment variables from the .env file."""
    load_dotenv()

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Generate and test code using OpenAI models.")
    parser.add_argument("--task", default="print a statement saying 'Oops! you forgot to give a task'", help="Task description for code generation.")
    parser.add_argument("--language", default="print a statement saying 'Oops! you forgot to give a language'", help="Programming language for code generation.")
    return parser.parse_args()

def initialize_openai_model():
    """Initialize the OpenAI model."""
    return OpenAI(
        model_name='gpt-3.5-turbo-instruct',
        openai_api_key=os.getenv('OPENAI_API_KEY'),
        max_tokens=-1
    )

def create_prompt_templates():
    """Create prompt templates for code generation and testing."""
    code_generation_prompt = PromptTemplate(
        template='You are a {language} expert with 5+ years of experience in this field. Write a {language} code that will do {task}.',
        input_variables=["language", 'task']
    )

    code_testing_prompt = PromptTemplate(
        input_variables=['language', 'code', 'task'],
        template='''
For the task "{task}", please check if the following {language} code is correct. 
If it is correct, just return the same code. If not, please return the corrected code. 
Remember, only output the code and nothing else.

code:
{code}

Output only the code:
'''
    )

    return code_generation_prompt, code_testing_prompt

def create_chains(llm, code_generation_prompt, code_testing_prompt):
    """Create chains for code generation and testing."""
    code_generation_chain = code_generation_prompt | llm
    code_testing_chain = code_testing_prompt | llm

    return code_generation_chain, code_testing_chain

def execute_chain(chain, args):
    """Execute the chain with the given arguments."""
    result = chain.invoke({
        "language": args.language,
        "task": args.task
    })
    return result

def main():
    load_environment_variables()
    args = parse_arguments()
    llm = initialize_openai_model()
    code_generation_prompt, code_testing_prompt = create_prompt_templates()
    code_generation_chain, code_testing_chain = create_chains(llm, code_generation_prompt, code_testing_prompt)

    # Create the overall chain
    chain = {
        'language': itemgetter('language'),
        'task': itemgetter('task'),
        'code': code_generation_chain
    } | code_testing_chain

    result = execute_chain(chain, args)
    print(result)

if __name__ == "__main__":
    main()
