import os
import openai
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI and Gemini API keys
openai.api_key = os.getenv("OPENAI_API_KEY")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Directory paths
BASE_DIR = os.path.dirname(__file__)
POLICY_PATH = os.path.join(BASE_DIR, "policy", "return_policy.txt")
SYSTEM_PROMPT_DIR = os.path.join(BASE_DIR, "system_prompts")
USER_PROMPT_DIR = os.path.join(BASE_DIR, "user_prompts")

# Load return policy
with open(POLICY_PATH, "r") as f:
    policy_text = f.read().strip()

# Load system prompts
system_prompts = {}
for filename in os.listdir(SYSTEM_PROMPT_DIR):
    with open(os.path.join(SYSTEM_PROMPT_DIR, filename), "r") as f:
        key = filename.replace(".txt", "")
        system_prompts[key] = f.read().strip() + "\n\n---\n" + policy_text

# Load user prompts
user_prompts = {}
for filename in os.listdir(USER_PROMPT_DIR):
    with open(os.path.join(USER_PROMPT_DIR, filename), "r") as f:
        key = filename.replace(".txt", "")
        user_prompts[key] = f.read().strip()

# Define models
models = {
    "gpt-4": lambda sys, usr: openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": sys}, {"role": "user", "content": usr}],
        temperature=0.0
    )["choices"][0]["message"]["content"],

    "gemini-pro": lambda sys, usr: genai.chat.Completion(
        model="gemini-pro",
        messages=[{"role": "system", "parts": [sys]}, {"role": "user", "parts": [usr]}]
    ).text
}

# Run test matrix
for sys_name, sys_prompt in system_prompts.items():
    for user_name, user_prompt in user_prompts.items():
        print(f"\n### System: {sys_name} | User: {user_name}")
        for model_name, run in models.items():
            print(f"\n[{model_name} Response]:")
            try:
                result = run(sys_prompt, user_prompt)
                print(result)
            except Exception as e:
                print(f"Error: {e}")
