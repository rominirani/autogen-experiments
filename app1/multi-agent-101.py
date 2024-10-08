from autogen import ConversableAgent
import autogen

config_list_gemini = autogen.config_list_from_json("model_config.json")

joke_writer = ConversableAgent(
    name="Joke Writer",
    system_message="Your task is to write a joke on Gen AI.",
    llm_config = {"config_list" : config_list_gemini},
    code_execution_config = False,
    human_input_mode = "NEVER",
    function_map = None
)

joke_reviewer = ConversableAgent(
    name="Joke Reviewer",
    system_message="Your task is to review a joke on Gen AI and provide your comments briefly in a list and you must ask for another joke.",
    llm_config = {"config_list" : config_list_gemini},
    code_execution_config = False,
    human_input_mode = "NEVER",
    function_map = None
)

reply = joke_writer.generate_reply(messages=[{"content": "Generate a joke on Gen AI", "role": "user"}])

joke_writer.initiate_chat(joke_reviewer,message=reply['content'], max_turns=2)