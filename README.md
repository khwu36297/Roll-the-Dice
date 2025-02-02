# Roll-the-Dice

## การติดตั้ง FFmpeg ผ่าน Homebrew (สำหรับ macOS)

หากคุณยังไม่ได้ติดตั้ง **FFmpeg** ผ่าน Homebrew คุณสามารถทำตามขั้นตอนด้านล่างนี้:

### 1. ติดตั้ง Homebrew (ถ้ายังไม่ได้ติดตั้ง)
เปิด Terminal แล้วรันคำสั่งนี้:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
### 2. ติดตั้ง FFmpeg ผ่าน Homebrew:
หลังจากติดตั้ง Homebrew เสร็จแล้ว ใช้คำสั่งนี้เพื่อติดตั้ง FFmpeg:
```bash
brew install ffmpeg
```
### 3. ตรวจสอบการติดตั้ง FFmpeg:
ตรวจสอบว่า FFmpeg ถูกติดตั้งเรียบร้อยแล้วหรือไม่ โดยใช้คำสั่งนี้ใน Terminal:
```bash
ffmpeg -version
```
## การติดตั้ง FFmpeg ใน Python

หากคุณไม่ต้องการใช้ Homebrew หรือวิธีอื่นๆ, คุณสามารถติดตั้ง FFmpeg ใน Python environment ได้โดยใช้คำสั่งนี้:
```bash
pip install ffmpeg
```
## Dice Roll Simulation Video

![Dice Roll Simulation](https://github.com/your-username/your-repo-name/blob/main/dice_rolls_simulation.mp4)
