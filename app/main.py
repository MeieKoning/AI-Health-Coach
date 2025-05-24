from app.nlp.goal_interpreter import GoalInterpreter
from app.data.tracker import Tracker
from app.voice.tts_output import TTSOutput
from app.rl.habit_optimizer import HabitRLAgent

def main():
    goal = input("Enter your health goal: ")
    interpreter = GoalInterpreter()
    tts = TTSOutput()
    tracker = Tracker()
    rl_agent = HabitRLAgent()

    interpretation = interpreter.interpret(goal)
    print("Coach:", interpretation)
    tts.speak(interpretation)
    tracker.log("goal", goal)

    metrics = {"calories": 2300, "form_score": 65}  # Example metrics
    state = rl_agent.get_state(metrics)
    action = rl_agent.choose_action(state)
    print(f"RL Agent Action: {action}")
    tts.speak(f"Coach Suggestion: {action}")

    reward = 1  # Example: user followed advice
    rl_agent.update(state, action, reward)

if __name__ == "__main__":
    main()