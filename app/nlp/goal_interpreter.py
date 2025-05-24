from langchain.chat_models import ChatOpenAI

class GoalInterpreter:
    def __init__(self, model_name="gpt-4"):
        self.llm = ChatOpenAI(model_name=model_name)

    def interpret(self, user_input, context={}):
        return self.llm.predict(f"User goal: {user_input}\nContext: {context}")