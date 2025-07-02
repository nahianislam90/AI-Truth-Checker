AI Truth Checker
A simple desktop application that checks if a statement is likely true or false, using semantic similarity and negation detection against a custom knowledge base.

What Does This Project Do?
This tool lets you enter a claim or statement. The app checks it against a loaded knowledge base (truth_base.txt) to find the most similar fact. It then decides if the claim is likely true or false, taking into account both meaning and the presence of negation words (like "not", "never", etc.).

Key Features
Semantic Similarity: Matches user claims to facts based on meaning, not just exact wording.

Negation Detection: Detects if a claim is the opposite of a known fact (e.g., "X is not a symptom" vs. "X is a symptom").

Custom Knowledge Base: Easily update the truth_base.txt file with your own facts.

User-Friendly Interface: Simple GUI for entering claims and viewing results.

Prerequisites
Python 3.9 or later (not Python 3.13 due to Tkinter compatibility issues)

pip (Python package installer)

PyTorch (for CPU) (required by sentence-transformers)

Basic knowledge of running Python scripts

You’ll use these imports in the code:

python
from sentence_transformers import SentenceTransformer, util
Installation
Clone the repository:

git clone https://github.com/nahianislam90/ai-truth-checker.git
cd ai-truth-checker
Create and activate a virtual environment (recommended):

python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
Install dependencies:

pip install torch sentence-transformers
Add your facts to truth_base.txt (or use the provided example).

Usage
Run the app:

python app.py
Enter a claim in the GUI and click "Verify Truth".
demo:![ai lie truth](https://github.com/user-attachments/assets/e2c35231-ab17-4355-97c2-e6a3098cdf52)
![ai lie dectetor](https://github.com/user-attachments/assets/09a8aa33-7230-497e-be86-381bbdcde1b9)


View the result: The app will tell you if the claim is likely true, false, or if there’s a negation mismatch.
