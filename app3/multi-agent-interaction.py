from autogen import ConversableAgent
import autogen

# Configure Gemini models
config_list_gemini = autogen.config_list_from_json("model_config.json")

human = ConversableAgent(
    name="Human",
    llm_config=False,
    human_input_mode="ALWAYS",
    default_auto_reply="Give me another quote",
)

quote_agent = ConversableAgent(
    name="quote_agent",
    system_message="You are an expert at providing quotes on life.",
    llm_config={"config_list": config_list_gemini},
    is_termination_msg=lambda msg: "ok" in msg["content"],  # terminate if the human responds ok
    human_input_mode="NEVER",  # never ask for human input
)

reply = human.initiate_chat(
    quote_agent,
    message="Provide me a quote that is from one of the Greek philosophers on Life")
