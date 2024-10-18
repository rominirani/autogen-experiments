# Instructions

This folder (`app6`) demonstrates additional features like conversation history, summarization, costs of a conversation between agents. 

# Get Your Gemini AI API Key
You will need to provide your Gemini AI API Key in the `model_config.json` folder. You can get your key from https://aistudio.google.com/app/apikey. Once you have the API Key, please provide that value in the `model_config.json` file for the two Gemini model configurations.

# Application List
- `multi-agent-101.py` : This program demonstrates two agents `Quote Writer` and `Quote Reviewer` communicating with each other.

The goal is to understand the following parts of the code that demonstrate the features that we are talking about (summary, chat_history and cost):
```
print(result.summary)
print(result.chat_history)
print(result.cost)
```

Refer to the blog post over here for a detailed analysis: 
  
# Run the Applications
- Setup a Python environment via the `requirements.txt` file that is provided.
  ```
  $ python3 -m venv .venv
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  ```
- Run the program at the command line for e.g. `$ python multi-agent-101.py`

