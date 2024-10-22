# Instructions

This folder (`app4`) demonstrates how you can have a human in the loop conversing with the Autonomous Agents. This is similar to `app3` except that it uses a local LLM (Google Gemma) hosted inside of [Ollama](https://ollama.com/), that is running locally.

# Ollama and Gemma Model installation instructions
1. Visit [Ollama](https://ollama.com/) and download/install the software for your environment.
2. Choose a model of your choice. For e.g. you can install Gemma as follows `ollama pull gemma`
3. Verify that the model runs fine via `ollama run <modelname>` and running a few prompts.
4. Edit the `human-autoagent-interaction.py` file by modifying the snippet given below:
```
config_list_gemini = [
    {
    "model": "gemma",
    "base_url": "http://localhost:11434/v1",
    "api_key": "ollama",
    }
    ]
```

Change the `model` from `gemma` to a one that you have installed locally in Ollama.

# Application List
- `human-autoagent-interaction.py` : This program demonstrates how you can configure a Human Agent and an Autonomous Agent. This is the same flow as in `app3`.

The scenario is as follows:
- The Human Agent initiates a conversation with the Autonomous Agent (that is skilled at generating Quotes) and asks it to generate quote
- The Autonomous Agent replies back with a Quote
- The Human Agent (you) will now have to decide if you want to terminate the conversation, do an auto-reply (generate another quote) or mention `ok`.
- The Autonomous Agent is configured with its `is_termination_msg` as sent to looking out for ok from the Human Agent. If that happens the conversation can terminate too.

You can consider this flow as a good way by which you can decide to hand over a task to one of the Agents and then review the result of that task. If not satisfactory, you can ask the Agent to do it again or provide your feedback accordingly and continue the conversation. 

# Blog Post
Refer to the following blog post for a detailed analysis : [https://iromin.medium.com/tutorial-multi-agent-interactions-with-autogen-and-gemini-part-3-introducing-manual-human-8674fe02b7d9](https://iromin.medium.com/tutorial-multi-agent-interactions-with-autogen-and-gemini-part-4-using-local-llms-c6b2faa6a435)

# Run the Application
- Setup a Python environment via the `requirements.txt` file that is provided.
  ```
  $ python3 -m venv .venv
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  ```
- Run the program at the command line for e.g. `$ python human-autoagent-interaction.py`

