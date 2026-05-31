def dictionary_attack(target_hash, wordlist):
for word in wordlist:
hashed_word = hashlib.sha256(word.encode()).hexdigest()
if hashed_word == target_hash:
print(f"كلمة المرور الصحيحة: {word}")
return
