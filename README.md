Experiments with Microsoft's [Autogen Framework](https://github.com/microsoft/autogen). 

The intention is to configure [Google Gemini models](https://ai.google.dev/gemini-api/docs/models/gemini) to work with Autogen.

List of programs:
- `main.py` : A starter template to configure 2 Agents with one asking a question/prompt of the other.
- `writer-reviewer.py` : A couple of agents interacting with each other to produce a quality CFP. One of them is the CFP Writer and the other one is a CFP Reviewer. The Writer writes an initial CFP and submits it to the reviewer to improve upon. The Reviewer reviews the CFP, provides a list of suggestions to improve and this is given back to the Writer, in an iterative fashion. 
