# main.py

from agent.loop import run_agent


def main():
    print("\n" + "="*70)
    print("🎓 SELF EVALUATION AGENT".center(70))
    print("="*70 + "\n")

    while True:
        print("Options:")
        print("  1. Start evaluation")
        print("  2. Exit")

        choice = input("\nSelect (1-2): ").strip()

        if choice == "1":
            subject = input("\nWhat subject should I evaluate you on? ").strip()
            if not subject:
                print("Please enter a subject!")
                continue

            num_q = input("How many questions? (default 5): ").strip()
            num_questions = int(num_q) if num_q.isdigit() else 5

            run_agent(subject, num_questions)

        elif choice == "2":
            print("\n👋 Goodbye!")
            break

        else:
            print("Invalid option, please select 1 or 2.")


if __name__ == "__main__":
    main()