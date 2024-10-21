from autogen import ConversableAgent
import autogen

config_list_gemini = autogen.config_list_from_json("model_config.json")

article_processor_agent = ConversableAgent(
    name="Exam Paper Processor Agent",
    llm_config = {"config_list" : config_list_gemini},
    human_input_mode = "NEVER",
)

scan_answer_paper_agent = ConversableAgent(
    name="Scan All Answers Check Agent",
    system_message='''Your task is to see if the student has provided answers for each question. 
                      Each answer should be one of a or b or c or d only. 
                      No other values or empty value is allowed and will be considered as not provided an answer.
                      Your response should contain the original message and a 'Data Check' field at the end, which says 'OK' if the student has provided answers to each question and if not, it says "NOT_OK". 
                      ''',
    llm_config = {"config_list" : config_list_gemini},
    human_input_mode = "NEVER",
)

check_answer_paper_agent = ConversableAgent(
    name="Check All Answers Check Agent",
    system_message='''Your task is to see if the student has provided correct answers for each question. 
                      Your task is to evaluate if the answers are correct or not as per the answer guide provided. 
                      For each correct answer, give 1 point. 
                      Compute the total number of points obtained by the student. 
                      ''',
    llm_config = {"config_list" : config_list_gemini},
    human_input_mode = "NEVER",
)

correct_answer_sheet = """
                Question 1 : b
                Question 2 : b
                Question 3 : c
                Question 4 : d
                Question 5 : b
                """

sample_answer_sheet = """
                Name : Romin Irani
                Student Id : S123
                Answers:
                Question 1 : b
                Question 2 : c
                Question 3 : d
                Question 4 : a
                Question 5 : a
"""


article_processor_agent.initiate_chats(
    [
        {
            "recipient" : scan_answer_paper_agent,
            "message" : "process the following answer sheet : \n" + sample_answer_sheet,
            "max_turns":1,
            "summary_method":"last_msg",
        },
        {
            "recipient" : check_answer_paper_agent,
            "message" : "Use the following answer guide : \n " + correct_answer_sheet + " to evaluate the following answer sheet:\n",
            "max_turns":1,
            "summary_method":"reflection_with_llm",
        }
    ]
)
