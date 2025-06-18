# LLM User Prompt Injection Lab

This project is designed to evaluate the robustness of large language models (LLMs) against adversarial user prompts that attempt to bypass or override strict system policies, such as refund or return policies in customer support scenarios.

## Features
- **Test Matrix:** Runs a matrix of system and user prompts through multiple LLMs (OpenAI GPT-4, Google Gemini) to observe and compare their responses.
- **Prompt Injection Scenarios:** Includes a variety of user prompts simulating real-world attempts to trick, confuse, or override the assistant.
- **Policy Enforcement:** System prompts include strict return/refund policies to test the LLMs' adherence.

## Directory Structure
```
llm-user-prompt-injection-lab/
├── json_injection_test.py         # Main script to run the test matrix
├── policy/
│   └── return_policy.txt         # The strict return/refund policy
├── system_prompts/
│   ├── basic.txt                 # Example system prompt
│   └── defensive.txt             # Defensive system prompt
├── user_prompts/
│   └── ...                       # Adversarial user prompts
├── requirements.txt              # Python dependencies
├── .env.template                 # Template for environment variables
└── README.md                     # This file
```

## Setup
1. **Clone the repository**
2. **Create and activate a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up environment variables:**
   - Copy `.env.template` to `.env` and fill in your OpenAI and Gemini API keys.

## Usage
Run the main script to execute the test matrix:
```sh
python json_injection_test.py > output.txt
```

- The script will print the responses from each model for every combination of system and user prompt.
- Output can be redirected to a file for analysis:
  ```sh
  python json_injection_test.py > output.txt
  ```

## Adding Prompts
- **System prompts:** Add `.txt` files to `system_prompts/`.
- **User prompts:** Add `.txt` files to `user_prompts/`.

## Notes
- Make sure your API keys have access to the models you wish to test.
- The `.env` file should never be committed to version control; use `.env.template` for sharing variable names.
- The project is intended for research and educational purposes.

## License
See [LICENSE](LICENSE). 