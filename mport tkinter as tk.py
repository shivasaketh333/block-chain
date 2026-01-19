import tkinter as tk
import hashlib
import time

# ---------------- BLOCK STRUCTURE ----------------
class Block:
    def __init__(self, index, value, prev_hash):
        self.index = index
        self.value = value
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data = str(self.index) + str(self.value) + self.timestamp + self.prev_hash
        return hashlib.sha256(data.encode()).hexdigest()

# ---------------- BLOCKCHAIN ----------------
class SimpleBlockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, 0, "0")
        self.chain.append(genesis)

    def add_block(self, value):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), value, prev_block.hash)
        self.chain.append(new_block)

blockchain = SimpleBlockchain()

# ---------------- GUI FUNCTIONS ----------------
def set_value():
    try:
        value = int(entry.get())
        blockchain.add_block(value)
        display_ledger()
        entry.delete(0, tk.END)
    except:
        pass

def get_value():
    latest = blockchain.chain[-1].value
    status_label.config(text=f"Stored Value: {latest}")

def display_ledger():
    ledger_box.delete("1.0", tk.END)
    for block in blockchain.chain:
        ledger_box.insert(tk.END, f"Block #{block.index}\n")
        ledger_box.insert(tk.END, f"Stored Value: {block.value}\n")
        ledger_box.insert(tk.END, f"Timestamp: {block.timestamp}\n")
        ledger_box.insert(tk.END, f"Prev Hash: {block.prev_hash}\n")
        ledger_box.insert(tk.END, f"Hash: {block.hash}\n")
        ledger_box.insert(tk.END, "-"*70 + "\n")

# ---------------- TKINTER UI ----------------
root = tk.Tk()
root.title("Simple Storage Smart Contract")
root.geometry("720x500")

tk.Label(root, text="Simple Storage Smart Contract", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Enter Value").pack()
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Set Value (Transaction)", command=set_value).pack(pady=3)
tk.Button(root, text="Get Value", command=get_value).pack(pady=3)

status_label = tk.Label(root, text="")
status_label.pack(pady=5)

tk.Label(root, text="Dummy Blockchain Ledger", font=("Arial", 12, "bold")).pack(pady=10)

ledger_box = tk.Text(root, width=90, height=15)
ledger_box.pack()

display_ledger()

root.mainloop()
