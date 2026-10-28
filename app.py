import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

# ตั้งค่า stdout/stderr ให้รองรับภาษาไทยในทุกระบบ
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ข้อมูลนักศึกษา
STUDENT_NAME = "กรินทร์ ปัญญามัง"
PORT = 5000

# พิมพ์ข้อความตามโจทย์ข้อที่ 1
print("Hello from Codespaces!")

# ฟังก์ชันอ่านค่าจากไฟล์ .env แบบไม่ต้องลง library เพิ่ม
def load_env(filepath=".env"):
    env_vars = {}
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    env_vars[key.strip()] = val.strip()
    return env_vars

env_data = load_env()

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        db_url = env_data.get("DATABASE_URL", "Not Found (Check .env)")
        api_key = env_data.get("API_KEY", "Not Found (Check .env)")

        html = f"""<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lab 3: Cloud Development - {STUDENT_NAME}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1f2937, #111827);
            color: #f3f4f6;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }}
        .card {{
            background: #ffffff;
            color: #1f2937;
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            max-width: 500px;
            width: 100%;
            text-align: center;
        }}
        h1 {{
            color: #2563eb;
            font-size: 24px;
            margin-bottom: 8px;
        }}
        .badge {{
            display: inline-block;
            background: #e0e7ff;
            color: #4338ca;
            padding: 6px 12px;
            border-radius: 9999px;
            font-size: 14px;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        .info-box {{
            background: #f9fafb;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            padding: 15px;
            text-align: left;
            margin-top: 15px;
            font-size: 14px;
        }}
        .info-title {{
            font-weight: bold;
            color: #4b5563;
            margin-bottom: 6px;
        }}
        code {{
            background: #e5e7eb;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
            word-break: break-all;
        }}
        .status {{
            color: #16a34a;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="card">
        <h1>Hello from Codespaces!</h1>
        <div class="badge">ผู้จัดทำ: {STUDENT_NAME}</div>
        
        <div class="info-box">
            <div class="info-title">🚀 สถานะเซิร์ฟเวอร์ (ข้อ 5: Port Forwarding):</div>
            <div>พอร์ต: <code>{PORT}</code> | สถานะ: <span class="status">กำลังทำงานปกติ (Running)</span></div>
        </div>

        <div class="info-box">
            <div class="info-title">🔒 ตรวจสอบ Environment Variables (ข้อ 3):</div>
            <div>DATABASE_URL: <code>{db_url}</code></div>
            <div>API_KEY: <code>{api_key}</code></div>
            <small style="color: #6b7280; display: block; margin-top: 6px;">* ค่าเหล่านี้โหลดมาจากไฟล์ <code>.env</code> (ซ่อนด้วย <code>.gitignore</code>)</small>
        </div>
    </div>
</body>
</html>"""
        self.wfile.write(html.encode("utf-8"))

def run_server():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"Server is running on port {PORT}...")
    print(f"ผู้จัดทำ: {STUDENT_NAME}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
