from autogen import ConversableAgent
import autogen

config_list_gemini = autogen.config_list_from_json("model_config.json")

agent = ConversableAgent(
    name="My Agent",
    llm_config = {"config_list" : config_list_gemini},
    code_execution_config = False,
    human_input_mode = "NEVER",
    function_map = None
)

reply = agent.generate_reply(messages=[{"content": "Who are you?", "role": "user"}])
print(reply)
