# 🎓 SkillMirror AI
### An Autonomous Self-Evaluation Agent powered by Claude

SkillMirror is an agentic AI system that evaluates your knowledge on any subject. You pick the topic, Claude drives everything — breaking it into subtopics, generating questions, collecting answers, grading them, and tracking your progress over time.

No hardcoded pipelines. Claude reasons and decides every step.

---

## 🧠 How It Works

```
You choose a subject
        ↓
Claude analyzes topics
        ↓
Claude generates questions
        ↓
You answer one by one
        ↓
Claude grades every answer
        ↓
Results saved + history compared
        ↓
Full report with scores & feedback
```

Claude is the brain. The tools are just messengers.

---

## 📁 Project Structure

```
skill_mirror/
├── config/
│   ├── __init__.py
│   └── settings.py           # Model, tokens, system prompt
├── tools/
│   ├── __init__.py
│   ├── topic_tools.py        # analyze_topics, generate_questions
│   ├── question_tools.py     # ask_user_question
│   ├── grading_tools.py      # grade_answer
│   ├── history_tools.py      # fetch_history, save_evaluation_result
│   └── flag_tools.py         # flag_incomplete_evaluation
├── agent/
│   ├── __init__.py
│   ├── tool_definitions.py   # Claude's tool manual (schemas)
│   ├── tool_executor.py      # Routes tool calls to functions
│   └── loop.py               # The agentic loop
├── data/
│   └── evaluation_history.json  # Persistent history stored here
├── main.py                   # Entry point
├── __init__.py
├── .env                      # Your API key (never commit this)
├── .gitignore
└── requirements.txt
```

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/devanshmittalexe/SkillMasterAI.git
cd SkillMasterAI/skill_mirror
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Anthropic API key
Create a `.env` file inside `skill_mirror/`:
```
ANTHROPIC_API_KEY=your_api_key_here
```
Get your key at [console.anthropic.com](https://console.anthropic.com)

### 5. Run it
```bash
python main.py
```

---

## 🚀 Example Session

```
======================================================================
                       🎓 SELF EVALUATION AGENT
======================================================================
Options:
  1. Start evaluation
  2. Exit

Select (1-2): 1
What subject should I evaluate you on? Chernobyl Disaster
How many questions? (default 5): 3

  🔧 Agent calling: analyze_topics
  🔧 Agent calling: generate_questions
  🔧 Agent calling: ask_user_question

──────────────────────────────────────────────────────────────────────
  Question 1 | Topic: Causes of the Disaster | Difficulty: MEDIUM
──────────────────────────────────────────────────────────────────────

  What design flaw in the RBMK-1000 reactor contributed to the explosion?

  Your answer: The positive void coefficient made it unstable at low power

  🔧 Agent calling: grade_answer
  🔧 Agent calling: fetch_history
  🔧 Agent calling: save_evaluation_result

📢 AGENT REPORT
  Score: 9/10 — Excellent answer!
  Overall: 78% | Strong: Reactor Design | Weak: Timeline of Events
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11+ | Core language |
| Anthropic SDK | Claude API access |
| python-dotenv | Environment variable management |
| JSON | Persistent history storage |
| Git | Version control |

---

## 🔑 Key Concepts Learned

Building this project teaches:

- **Agentic AI** — how LLMs drive multi-step workflows using tools
- **Tool Use** — giving Claude a manual and letting it decide when to call what
- **Version Control** — proper Git branching with `dev → QA → main`
- **Project Structure** — separating concerns across files and modules
- **Prompt Engineering** — writing system prompts that enforce strict workflows

---

## 🗺️ Roadmap

- [x] Agentic evaluation loop
- [x] Persistent history tracking
- [x] Multi-topic question generation
- [ ] Adaptive difficulty (harder questions if scoring well)
- [ ] Per-question feedback during quiz
- [ ] ASCII progress charts
- [ ] Web UI

---

## ⚠️ Important

- Never commit your `.env` file — it contains your API key
- Each evaluation session costs approximately $0.05–$0.20 depending on question count
- History is stored locally in `data/evaluation_history.json`

---

## 📄 License

MIT License — feel free to use, modify, and build on this project.

---

*Built step by step as a learning project for Agentic AI + Version Control*