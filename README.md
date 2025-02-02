# Roll-the-Dice


1. ติดตั้ง ffmpeg ผ่าน Homebrew (สำหรับ macOS)
หากยังไม่ได้ติดตั้ง ffmpeg ด้วย Homebrew, ให้ทำตามคำแนะนำนี้:

ติดตั้ง Homebrew (ถ้ายังไม่ได้ติดตั้ง):
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

ติดตั้ง ffmpeg ผ่าน Homebrew:
brew install ffmpeg

ตรวจสอบว่า ffmpeg ถูกติดตั้งหรือไม่: ใช้คำสั่งนี้ใน Terminal:
ffmpeg -version

ถ้า ffmpeg ติดตั้งสำเร็จ คุณจะเห็นข้อมูลเวอร์ชันของ ffmpeg

2. ติดตั้ง ffmpeg ใน Python
ถ้าไม่ใช้ Homebrew หรือวิธีอื่นๆ, คุณสามารถติดตั้ง ffmpeg ใน Python environment โดยใช้คำสั่งนี้:
pip install ffmpeg
