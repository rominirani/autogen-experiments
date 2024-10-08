# Instructions

This folder (`app2`) builds upon (`app1`) and shows how to terminate/exit the conversation based on a response from one of the Agents. It is documented over here: [Chat Termination](https://microsoft.github.io/autogen/docs/tutorial/chat-termination)

# Get Your Gemini AI API Key
You will need to provide your Gemini AI API Key in the `model_config.json` folder. You can get your key from https://aistudio.google.com/app/apikey. Once you have the API Key, please provide that value in the `model_config.json` file for the two Gemini model configurations.

# Application List
- `multi-agent-interaction.py` : This program demonstrates how you can configure 2 ConversableAgent's (`CFP Writer` and `CFP Reviwer`) and make them converse iteratively with each other in a feedback loop to improve a Call for Proposal/Papers (CFP). In `app1`, we were providing `max_turns` as 2 in the `initiate_chat` method. But now, we will not depend on the number of `max_turns` but depend on a specific text found in the response of the `CFP Reviewer`. So if the `CFP Reviewer` finds that the submission has incorporated most of the feedback that it has been giving for the previous iterations, then it will mention `looks good` at the end of the text.

To do that, we are making minor changes in the code compared to `app1`. 

First up, we are introducing an `is_termination` parameter in the CFP Writer as shown below:
```
cfp_writer = ConversableAgent(
    name="CFP Writer",
    system_message=SYSTEM_MESSAGE_CFP_WRITER,
    llm_config = {"config_list" : config_list_gemini},
    code_execution_config = False,
    human_input_mode = "NEVER",
    function_map = None,
    is_termination_msg=lambda msg: "looks good" in msg["content"].lower(),
)
```

And we are updated the System Prompt for the CFP Reviewer to mention `looks good` if the changes have been sufficiently and satisfactorily incorporated by the CFP Writer. Here is the updated System prompt (Note the slight addition at the end).
```
SYSTEM_MESSAGE_CFP_REVIEWER = """
Your task is to review a submission for a technical talk.
.... <rest of the text> ....
If there are no significant changes, please mention "looks good" at the end of the message.
"""
```

# Run the Applications
- Setup a Python environment via the `requirements.txt` file that is provided.
  ```
  $ python3 -m venv .venv
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  ```
- Run any of the programs at the command line for e.g. `$ python multi-agent-interaction.py`

