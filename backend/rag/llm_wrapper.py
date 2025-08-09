from langchain.chat_models import init_chat_model

def get_llm():
    return init_chat_model("claude-3-5-sonnet-latest", model_provider="anthropic")
