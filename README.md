# 🤖 LeetCode Solving Agent

A professional Python agent that fetches daily LeetCode problems and generates solutions using OpenAI.

## 🎯 Features

- ✅ Fetches daily LeetCode problem automatically
- ✅ Generates optimal Python solutions using GPT-4
- ✅ Validates solution syntax
- ✅ Professional logging and error handling
- ✅ Comprehensive test suite
- ✅ Easy configuration management

## 📋 Project Structure

```
├── config.py              # Configuration management
├── logger_config.py       # Logging setup
├── fetcher.py            # LeetCode problem fetcher
├── solution_generator.py # AI-powered solution generator
├── code_executor.py      # Solution validator and executor
├── agent.py              # Main orchestrator
├── test_agent.py         # Test suite
├── .env                  # Environment variables (create this!)
└── README.md             # This file
```

## 🚀 Quick Start

### 1. Create and Activate Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install openai requests python-dotenv
```

### 3. Setup Environment Variables

Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_actual_api_key_here
LOG_LEVEL=INFO
DEBUG_MODE=False
```

### 4. Run Quick Tests

```bash
python test_agent.py quick
```

### 5. Run the Agent

```bash
python agent.py
```

## 📊 How It Works

1. **Fetch**: Retrieves the daily LeetCode problem via GraphQL API
2. **Generate**: Uses OpenAI to create an optimal Python solution
3. **Validate**: Checks syntax and can execute test cases
4. **Save**: Stores results in JSON format with timestamp

## 🧪 Testing

### Run All Tests
```bash
python -m unittest test_agent.py
```

### Run Quick Sanity Check
```bash
python test_agent.py quick
```

### Run Individual Test Classes
```bash
python -m unittest test_agent.TestCodeExecutor
```

## 📝 Output Example

When you run `python agent.py`, you'll see:
```
============================================================
🚀 Starting LeetCode Agent
============================================================

📝 Step 1: Fetching daily problem...
✅ Fetched problem: Two Sum (Easy)

🤖 Step 2: Generating solution...
✅ Solution generated successfully

✔️  Step 3: Validating syntax...
✅ Code syntax is valid

============================================================
📊 Summary
============================================================

📌 Problem: Two Sum
📊 Difficulty: Easy
📋 Slug: two-sum

🔧 Solution Preview (first 500 chars):
[Your solution code here...]

✅ Solution generated and saved!
💾 Results saved to solution_20260727_120000.json
```

## 🔧 Configuration Options

Edit `config.py` to customize:

| Variable | Default | Description |
|----------|---------|-------------|
| OPENAI_MODEL | gpt-4o-mini | OpenAI model to use |
| TEMPERATURE | 0.3 | Lower = more deterministic |
| LOG_LEVEL | INFO | Logging level (DEBUG, INFO, WARNING, ERROR) |

## 🐛 Troubleshooting

**Problem: `OPENAI_API_KEY is not set`**
- Solution: Make sure `.env` file exists with your API key

**Problem: `Module not found error`**
- Solution: Activate virtual environment and reinstall: `pip install -r requirements.txt`

**Problem: Network errors**
- Solution: Check internet connection or try again later

## 📚 Future Enhancements

- [ ] Add retry logic for failed attempts
- [ ] Support for multiple languages
- [ ] Interactive problem selector
- [ ] Solution performance analysis
- [ ] Difficulty progression tracking
- [ ] Discord bot integration

## 👨‍💻 Author : Hampanna Gouda

LeetCode Agent Team
