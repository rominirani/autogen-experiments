from autogen import ConversableAgent
import autogen
import agentops

config_list_gemini = autogen.config_list_from_json("model_config.json")
agentops.init(api_key="YOUR AGENTOPS API KEY", default_tags=["my-multi-agent-101-tag"])

quote_writer = ConversableAgent(
    name="Quote Generator",
    system_message="Your task is to provide famous quotes",
    llm_config = {"config_list" : config_list_gemini},
    code_execution_config = False,
    human_input_mode = "NEVER",
)

quote_reviewer = ConversableAgent(
    name="Joke Reviewer",
    system_message="Your task is to review a famous quote and provide your comments briefly in a list.",
    llm_config = {"config_list" : config_list_gemini},
    code_execution_config = False,
    human_input_mode = "NEVER",
)

reply = quote_writer.generate_reply(messages=[{"content": "Give me a quote by Albert Einstein", "role": "user"}])

quote_writer.initiate_chat(quote_reviewer,message=reply['content'], max_turns=2)

agentops.end_session("Success")
