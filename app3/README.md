# Instructions

This folder (`app3`) demonstrates how you can have a human in the loop conversing with the Autonomous Agents. It is documented over here: [Human in the Loop](https://microsoft.github.io/autogen/docs/tutorial/human-in-the-loop)

# Get Your Gemini AI API Key
You will need to provide your Gemini AI API Key in the `model_config.json` folder. You can get your key from https://aistudio.google.com/app/apikey. Once you have the API Key, please provide that value in the `model_config.json` file for the two Gemini model configurations.

# Application List
- `human-autoagent-interaction.py` : This program demonstrates how you can configure a Human Agent and an Autonomous Agent.

The scenario is as follows:
- The Human Agent initiates a conversation with the Autonomous Agent (that is skilled at generating Quotes) and asks it to generate quote
- The Autonomous Agent replies back with a Quote
- The Human Agent (you) will now have to decide if you want to terminate the conversation, do an auto-reply (generate another quote) or mention `ok`.
- The Autonomous Agent is configured with its `is_termination_msg` as sent to looking out for ok from the Human Agent. If that happens the conversation can terminate too.

You can consider this flow as a good way by which you can decide to hand over a task to one of the Agents and then review the result of that task. If not satisfactory, you can ask the Agent to do it again or provide your feedback accordingly and continue the conversation. 

# Blog Post
Refer to the following blog post for a detailed analysis : https://iromin.medium.com/tutorial-multi-agent-interactions-with-autogen-and-gemini-part-3-introducing-manual-human-8674fe02b7d9
  
# Run the Applications
- Setup a Python environment via the `requirements.txt` file that is provided.
  ```
  $ python3 -m venv .venv
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  ```
- Run the program at the command line for e.g. `$ python human-autoagent-interaction.py`

