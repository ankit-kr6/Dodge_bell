Dodge Game – Pandit Ji Edition

A fast‑paced, fun, Hindi‑style dodging game built using Python + Pygame!
Control Pandit Ji, dodge the falling bells (Ghanti), and survive as long as you can.
The speed gradually increases, and your score is saved at the end.


---
Game Overview

In this game:

You move Pandit Ji left & right.

Bells fall from the top.

Every bell you dodge increases your score.

If a bell hits you → OH SHIT! Game Over! 

Your name & score are saved in scores.txt.



---

🖼 Screenshots (Add later)

You can add your own gameplay screenshots here:

📸 Start Screen
📸 Running Game
📸 Game Over Screen


---

⚙ Features

Smooth movement

Increasing difficulty

Player name input

Score saving system

Clean UI with custom colors

Uses your own images: Pandit.jpg, Bell.jpg



---

📁 Folder Structure

Dodge-Game/
│-- game.py
│-- Pandit.jpg
│-- Bell.jpg
│-- scores.txt   (auto-created)
│-- README.md


---

🔧 Installation

1️⃣ Install Python

Download from: https://www.python.org

2️⃣ Install Pygame

pip install pygame

3️⃣ Run the Game

python game.py


---

🎯 Controls

Key	Action

⬅ Left Arrow	Move Left
➡ Right Arrow	Move Right



---

⚙ Game Configuration

🎲 Ball Frequency (Updated to 20)

The game creates a new ball every 20 frames:

ball__frequency = 20

Lower number → more balls
Higher number → fewer balls

🚀 Dynamic Difficulty (Auto Speed Increase)

Score > 50 → Speed 7

Score > 100 → Speed 9

Score > 150 → Speed 12



---

📝 Score Saving

When the game ends, your name & score are added to:

scores.txt

Format:

PlayerName : Score


---

🎨 Customization Options

You can easily modify:

Player image

Bell image

Speed and frequency

Background colors

Text fonts and sizes

Game title on the window


Just edit the variables inside the code.


---

❤ Credits

Developed by ANKIT KUMAR MANDAL


