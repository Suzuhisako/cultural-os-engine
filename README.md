# 🌍 Cultural OS Scenario Analysis Engine

A highly interactive web dashboard built to analyze, map, and classify complex cross-border scenarios. The app combines a clean, local frontend environment with the power of **Google AI Studio (Gemini 2.5 Flash)** and live **Google Search Grounding** to cross-reference real-time cultural norms, legal compliance rules, and operational risks across target jurisdictions.

---

## ✨ Features

* **Live Google Search Grounding:** Bypasses static model cutoff limits by executing real-time web searches to verify current country-specific laws and cultural shifts.
* **Dual-Layer Scenario Numbering:** Uses a hybrid tracking layout featuring a gap-free visual counter on the main timeline alongside unshakeable backend database anchors (`ID-x`).
* **Resilient API Architecture:** Equipped with defensive `try/except` error-handling blocks that capture global server capacity surges gracefully without interrupting local services.
* **Persistent History Logs:** Shuffles, logs, and safely deletes processed scenario records instantly using a clean JSON-driven backend logic structure.
* **Two-Column Masterpiece Layout:** Beautifully styled template optimized for scanning multi-variant analysis matrix data points seamlessly.
* **Pre-Loaded Sample Matrices:** Includes 2 built-in, high-quality cultural scenario cards out of the box to instantly demonstrate the dashboard layout without requiring an initial API credit.

---

## 🛠️ Technology Stack

* **Backend:** Python, Flask
* **AI Core:** `google-genai` SDK (Connecting to Google AI Studio)
* **Default Engine:** `gemini-2.5-flash` (Optimized for fast structural logic and free-tier grounding quotas)
* **Frontend:** HTML5, Tailwind CSS, Native JavaScript

---

## 🚀 Getting Started

Follow these step-by-step instructions to get a local development copy of this application running on your computer.

### 1. Prerequisites
Make sure you have Python 3.10+ installed on your system. You will also need a free API Key from [Google AI Studio](https://aistudio.google.com/).

### 2. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME


3. Install Dependencies
Install the necessary package requirements using pip:

Bash
pip install flask google-genai
4. Configure Your Environment Variable
The application looks for your AI Studio credential token safely stored inside your system configuration variables.

On Linux/macOS:

Bash
export GEMINI_API_KEY="your_api_key_here"
On Windows (Command Prompt):

DOS
set GEMINI_API_KEY=your_api_key_here
On Windows (PowerShell):

PowerShell
$env:GEMINI_API_KEY="your_api_key_here"
5. Launch the Application
Start the Flask local development server:

Bash
python app.py
Open your web browser and navigate to: http://127.0.0.1:5000

🎨 Layout & Architecture Highlights
Hybrid Scenario Visual Tracker
The application balances user experience with database accuracy by detaching layout sorting from technical tracking values. When scenarios are created or deleted, a dynamic JavaScript loop re-indexes the cards sequentially (Scenario #1, #2, #3) while preserving the original system anchor badge (ID-42) next to the tracking matrix link.

Grounding & Mime-Type Design Constraint
To bypass the API design rule where explicit "text/html" response definitions block search integrations, this application uses Option A Architecture. The core generation engine utilizes the Google Search tool constraint while using a targeted precision_prompt to cleanly construct beautiful markup blocks dynamically.

📄 License
This project is open-source and available under the MIT License.  




