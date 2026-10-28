# ใบงานฝึกปฏิบัติ 3: การใช้เครื่องมือพัฒนาบนคลาวด์และการทำงานร่วมกันแบบเรียลไทม์

**ผู้จัดทำ:** กรินทร์ ปัญญามัง  
**ชื่อโปรเจกต์ (Repository):** `lab3-cloud-dev`

---

## 📌 สรุปการปฏิบัติงานตามใบงาน

### ข้อที่ 1: การเปิดใช้งานและตั้งค่าสภาพแวดล้อมบน GitHub Codespaces
1. สร้างไฟล์ `app.py` 
2. พิมพ์ข้อความ `"Hello from Codespaces!"` 
3. รันโปรแกรมด้วยคำสั่ง:
   ```bash
   python app.py
   ```

### ข้อที่ 2: การใช้ VS Code Live Share สำหรับเขียนโค้ดร่วมกันแบบเรียลไทม์
1. ติดตั้ง Extension **Live Share** บน VS Code
2. คลิกปุ่ม **Live Share** (ด้านซ้ายล่าง) แล้วกด **Share** เพื่อคัดลอก Invite Link
3. ส่งลิงก์ให้เพื่อนในกลุ่มเข้าร่วมแบบ Guest เพื่อเขียนโค้ดและสังเกต Cursor พร้อมกัน

### ข้อที่ 3: การจัดการแชร์ Environment Variables (ความปลอดภัยบน Cloud)
1. สร้างไฟล์ `.env` สำหรับเก็บข้อมูลลับ เช่น:
   ```env
   DATABASE_URL=mongodb://localhost:27017/mydb
   API_KEY=secret_12345
   ```
2. สร้างไฟล์ `.gitignore` และระบุ `.env` ไว้ด้านใน เพื่อป้องกันไม่ให้ Git อัปโหลดไฟล์ความลับขึ้น GitHub
3. ตรวจสอบด้วยคำสั่ง:
   ```bash
   git status
   ```
   *ผลลัพธ์: จะไม่พบไฟล์ `.env` ในรายการ untracked files ยืนยันว่าถูกซ่อนสำเร็จ*

### ข้อที่ 4: การใช้งานเครื่องมือจัดการโปรเจกต์บน Cloud (GitHub Projects / Trello)
1. เปิดแท็บ **Projects** บน GitHub Repository แล้วคลิก **New Project (Board)**
2. สร้างการ์ดงาน (Task) 4 การ์ด:
   - `Setup Project`
   - `Create UI`
   - `Connect API`
   - `Testing`
3. มอบหมายงาน (Assign) ให้สมาชิกในกลุ่ม
4. ย้ายสถานะการ์ดจาก `To Do` → `In Progress` → `Done`

### ข้อที่ 5: การรันและทดสอบเว็บแอปพลิเคชันผ่าน Cloud Port Forwarding
1. รันเว็บเซิร์ฟเวอร์ใน Codespaces:
   ```bash
   python app.py
   ```
2. ไปที่แท็บ **PORTS** ด้านล่างของหน้าต่าง Codespaces (จะพบพอร์ต `5000`)
3. คลิกขวาที่พอร์ต 5000 แล้วเปลี่ยน **Port Visibility** เป็น **Public**
4. คัดลอก **Forwarded Address (URL)** ส่งให้เพื่อนหรือเปิดดูผลลัพธ์ผ่านเว็บเบราว์เซอร์

---

## 🚀 วิธีการนำโปรเจกต์นี้ขึ้น GitHub (Push to GitHub)

### วิธีที่ 1: ใช้คำสั่งผ่าน Git Terminal (แนะนำ)

1. **สร้าง Repository ใหม่บน GitHub**
   - ไปที่ [https://github.com/new](https://github.com/new)
   - ตั้งชื่อ Repository ว่า `lab3-cloud-dev`
   - เลือกว่าเป็น **Public**
   - **ไม่ต้อง** ติ๊กถูกที่ช่อง "Add a README file" หรือ ".gitignore"
   - คลิกปุ่ม **Create repository**

2. **เปิด Terminal ในโฟลเดอร์นี้ แล้วรันคำสั่งตามลำดับ:**
   ```bash
   # 1. จัดเตรียมไฟล์ทั้งหมดเพื่อ Commit
   git add .

   # 2. บันทึกประวัติการเปลี่ยนแปลง
   git commit -m "feat: complete lab 3 assignment by Krin Panyamang"

   # 3. ตั้งชื่อกิ่งหลักเป็น main
   git branch -M main

   # 4. เชื่อมต่อ Local Repo เข้ากับ GitHub (แทนที่ USERNAME ด้วยชื่อบัญชี GitHub ของคุณ)
   git remote add origin https://github.com/USERNAME/lab3-cloud-dev.git

   # 5. อัปโหลดไฟล์ขึ้น GitHub
   git push -u origin main
   ```

---

### วิธีที่ 2: อัปโหลดผ่านหน้าเว็บไซต์ GitHub โดยตรง (แบบง่าย)

1. ไปที่ [https://github.com/new](https://github.com/new) แล้วสร้าง Repository ชื่อ `lab3-cloud-dev`
2. ในหน้า Repo เปล่า ให้คลิกลิงก์คำว่า **"uploading an existing file"**
3. ลากไฟล์จากโฟลเดอร์นี้ ได้แก่:
   - `app.py`
   - `.gitignore`
   - `.env.example`
   - `README.md`
   *(⚠️ ข้อควรระวัง: อย่าลากไฟล์ `.env` ขึ้นไป เพื่อความปลอดภัยตามโจทย์ข้อ 3)*
4. เลื่อนลงมากดปุ่มสีเขียว **Commit changes**

