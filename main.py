# main.py

from openai_engine import OpenAIEngine
from dummy_engine import DummyEngine
from engine_manager import AIEngineManager

# Replace with your real OpenAI key
OPENAI_API_KEY = "sk-..."

def main():
    # Initialize manager and engines
    manager = AIEngineManager()
    manager.register_engine("openai", OpenAIEngine(api_key=OPENAI_API_KEY))
    manager.register_engine("dummy", DummyEngine())

    print("🤖 Multi-AI Engine is ready!")
    print("Available engines:", manager.list_engines())

    while True:
        engine_key = input("🔑 Enter engine (e.g., openai / dummy): ").strip().lower()
        if engine_key == "exit":
            print("👋 Goodbye!")
            break

        prompt = input("📝 Enter your prompt: ").strip()
        response = manager.get_response(engine_key, prompt)
        print(f"💬 Response:\n{response}\n")

if __name__ == "__main__":
    main()
