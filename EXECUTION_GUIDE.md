# 🎯 EXECUTION GUIDE - Step by Step

Follow these exact steps to build and test your LeetCode agent.

## ✅ STEP 1: Setup Environment (5 minutes)

### 1a. Create .env file
In the project folder, create a file named `.env` with:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxx
LOG_LEVEL=INFO
DEBUG_MODE=False
```

**Get your API key:**
1. Go to https://platform.openai.com/api-keys
2. Create new secret key
3. Copy and paste into .env

### 1b. Verify your setup
```powershell
# You should already have these from earlier terminal sessions:
pip list | findstr "openai requests python-dotenv"
```

---

## ✅ STEP 2: Quick Validation Test (2 minutes)

Run the quick sanity check:
```powershell
cd "c:\Users\GoudaHam\OneDrive - Unisys\Desktop\leetcode-agent"
python test_agent.py quick
```

**Expected Output:**
```
✅ Running Quick Sanity Checks...
✅ Config loads successfully
✅ Logger works
✅ Executor works
```

---

## ✅ STEP 3: Run Unit Tests (3 minutes)

```powershell
python -m unittest test_agent.py -v
```

**Expected Output:** Multiple test results, mostly PASS (some mock tests)

---

## ✅ STEP 4: Run the Main Agent (Real Test!) ⭐

This is the REAL test - it will:
- Fetch today's LeetCode problem
- Generate a solution using OpenAI
- Validate the code

```powershell
python agent.py
```

**Expected Output:**
```
============================================================
🚀 Starting LeetCode Agent
============================================================

📝 Step 1: Fetching daily problem...
✅ Fetched problem: [Problem Name] (Difficulty)

🤖 Step 2: Generating solution...
✅ Solution generated successfully

✔️  Step 3: Validating syntax...
✅ Code syntax is valid

============================================================
📊 Summary
============================================================

📌 Problem: [Problem Name]
📊 Difficulty: [Easy/Medium/Hard]
📋 Slug: [slug]

🔧 Solution Preview...
```

---

## ✅ STEP 5: Check Output Files

After running, you'll find a new file:
```
solution_20260727_120000.json
```

Open it to see:
- Full problem details
- Complete solution code
- Metadata

---

## 🐛 TROUBLESHOOTING

### Error: "OPENAI_API_KEY is not set"
**Solution:** Make sure `.env` file exists in the project folder with your API key

### Error: "Module not found"
**Solution:**
```powershell
pip install openai requests python-dotenv
```

### Error: "Network error"
**Solution:** Check internet connection, wait a moment, try again

### Error: "Invalid API key"
**Solution:** 
- Check your API key at https://platform.openai.com/api-keys
- Make sure it's fresh (not expired)
- Regenerate if needed

---

## 🎓 HOW TO EXTEND (Future Improvements)

### Add test case validation:
In `agent.py`, modify `solve()` method:
```python
# After generating solution
test_cases = [
    (input_data, expected_output),
    # Add more test cases
]
results = self.executor.execute_with_test_cases(solution, test_cases)
```

### Add solution refinement:
If solution has errors, automatically regenerate:
```python
attempts = 0
while not CodeExecutor.validate_syntax(solution) and attempts < 3:
    solution = self.generator.generate_solution(problem)
    attempts += 1
```

### Add performance analysis:
Save execution times and complexity analysis with solution

### Add Discord webhook:
Send daily solutions to Discord channel automatically

---

## 📊 SUCCESS METRICS

Your agent is working when:
✅ `.env` file is correctly configured
✅ `python test_agent.py quick` passes all checks
✅ `python -m unittest test_agent.py` has mostly passing tests
✅ `python agent.py` fetches and solves a problem
✅ `solution_*.json` files are created with solutions

---

## 🎯 FINAL CHECKLIST

- [ ] .env file created with OPENAI_API_KEY
- [ ] `python test_agent.py quick` passes
- [ ] `python -m unittest test_agent.py` runs
- [ ] `python agent.py` successfully runs
- [ ] `solution_*.json` file is created
- [ ] Verify JSON file contains problem and solution
- [ ] Review generated solution quality

Once all ✅, your agent is production-ready!
