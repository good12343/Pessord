import time

def brute_force_attack(target_hash, password):
start_time = time.time()
for i in range(1000000): # مثال تحميل
hashed_password = hashlib.sha256(str(i).encode()).hexdigest()
if hashed_password == target_hash:
print(f"كلمة المرور الصحيحة: {i}")
print(f"الوقت المستغرق: {time.time() - start_time:.6f} ثانية")
return
