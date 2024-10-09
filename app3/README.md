# Instructions

This folder (`app3`) demonstrates how you can have a human in the loop conversing with the Autonomous Agents. It is documented over here: [Human in the Loop](https://microsoft.github.io/autogen/docs/tutorial/human-in-the-loop)

# Get Your Gemini AI API Key
You will need to provide your Gemini AI API Key in the `model_config.json` folder. You can get your key from https://aistudio.google.com/app/apikey. Once you have the API Key, please provide that value in the `model_config.json` file for the two Gemini model configurations.

# Application List
- `human-autoagent-interaction.py` : This program demonstrates how you can configure a Human Agent and an Autonomous Agent.

The scenario is as follows:
- The Human Agent initiates a conversation with the Autonomous Agent (that is skilled at generating Quotes) and asks it to generate quote
- The Autonomous Agent replies back with a Quote
- The Human Agent (you) will now have to decide if you want to terminate the conversation, do an auto-reply (generate another quote) or mention ok

  
# Run the Applications
- Setup a Python environment via the `requirements.txt` file that is provided.
  ```
  $ python3 -m venv .venv
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  ```
- Run the program at the command line for e.g. `$ python human-autoagent-interaction.py`

