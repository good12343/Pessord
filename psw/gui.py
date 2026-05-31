import tkinter as tk
from utils.hashing import hash_password
from attacks.brute_force import brute_force_attack

class PasswordGuessingApp:
def __init__(self, master):
self.master = master
master.title("أداة تخمين كلمات المرور")

self.label = tk.Label(master, text="أدخل كلمة المرور التي تريد اختبارها:")
self.label.pack()

self.entry = tk.Entry(master, show="*")
self.entry.pack()

self.button = tk.Button(master, text="اختبار", command=self.test_password)
self.button.pack()

def test_password(self):
password = self.entry.get()
target_hash = hash_password(password)
brute_force_attack(target_hash, password)
