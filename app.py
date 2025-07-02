import tkinter as tk
from tkinter import messagebox
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')
book_sentences = []
book_embeddings = []


def has_negation(text):
    neg_words = [
        "not", "never", "no", "fail", "failure", "bad", "worse", "poor", "none",
        "cannot", "can't", "don't", "doesn't", "isn't", "aren't", "won't", "shouldn't", "couldn't"
    ]
    return any(word in text.lower() for word in neg_words)


def load_book():
    global book_sentences, book_embeddings
    try:
        with open("truth_base.txt", "r", encoding="utf-8") as f:
            book_sentences = [line.strip() for line in f if line.strip()]
        book_embeddings = model.encode(book_sentences, convert_to_tensor=True)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load truth_base.txt: {e}")


def check_claim():
    if len(book_embeddings) == 0:
        messagebox.showwarning("Error", "Knowledge base is empty!")
        return

    claim = entry.get("1.0", tk.END).strip()
    if not claim:
        messagebox.showwarning("Input Error", "Enter a claim to verify")
        return

    claim_embed = model.encode(claim, convert_to_tensor=True)
    scores = util.cos_sim(claim_embed, book_embeddings)  # Shape: (1, N)

    # Get best match index and score
    best_match_idx = scores.argmax().item()
    best_score = scores[0, best_match_idx].item()  # Fixed indexing
    best_fact = book_sentences[best_match_idx]

    # Negation bias logic
    if best_score > 0.6:
        claim_neg = has_negation(claim)
        fact_neg = has_negation(best_fact)
        if claim_neg != fact_neg:
            result = f"❌ Likely FALSE (Negation mismatch)\nSimilarity: {best_score*100:.2f}%\nMatched: \"{best_fact}\""
            result_label.config(fg="red")
        else:
            result = f"✅ Likely TRUE\nSimilarity: {best_score*100:.2f}%\nMatched: \"{best_fact}\""
            result_label.config(fg="green")
    else:
        result = f"❌ Likely FALSE\nSimilarity: {best_score*100:.2f}%"
        result_label.config(fg="red")

    result_label.config(text=result)


# GUI setup
root = tk.Tk()
root.title("📚 AI Truth Verifier")
root.geometry("600x500")
root.config(bg="#f0f8ff")

tk.Label(root, text="AI Fact Checker", font=(
    "Arial", 18, "bold"), bg="#f0f8ff").pack(pady=10)

input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=10)
tk.Label(input_frame, text="Enter claim to verify:",
         font=("Arial", 11), bg="#f0f8ff").pack()
entry = tk.Text(input_frame, height=4, width=60, font=("Arial", 10))
entry.pack(pady=5)

tk.Button(root, text="🔍 Verify Truth", command=check_claim,
          bg="#e85d75", fg="white", font=("Arial", 12), width=15).pack(pady=15)

result_label = tk.Label(root, text="", font=(
    "Arial", 12), bg="#f0f8ff", wraplength=500)
result_label.pack(pady=10)

load_book()  # Load knowledge base at startup

root.mainloop()
