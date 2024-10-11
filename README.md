Experiments demonstrating [Autogen](https://github.com/microsoft/autogen) framework. 

1. [`app1`](app1) : Multi-turn conversation between 2 agents, CFP Writer and CFP Reviewer that converse with each other to improve a CFP. Their conversation lasts the number of `max_turns` mentioned while setting up i.e. initiating the chat. 
2. [`app2`](app2) : Multi-turn conversation between 2 agents with an explicit termination done by the framework if the CFP Reviewer mentions "looks good". It does not depend on the `max_turns` parameter while initiating the chat. 
3. [`app3`](app3) : Conversation between a Human Agent and an Autonomous Agent. The Human asks the Autonomous Agent to do a task and then reviews it. The Human can then either terminate the conversation or ask the Autonomous Agent to do the task again. 
4. [`app4`](app4) : This is the same example as `app3` , except that instead of invoking the Gemini models online, we use Ollama locally with the Google Gemma model as the LLM. 
