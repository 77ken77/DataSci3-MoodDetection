# CaptureMood.py
import cv2
import os

# === CONFIG ===
moods = ["Happy", "Sad", "Angry", "Confused"]
base_dir = "captured_moods"   # Folder to save images
num_images_per_mood = 50      # Adjust as needed
capture_delay = 3             # Seconds between captures

# === CREATE FOLDERS ===
for mood in moods:
    os.makedirs(os.path.join(base_dir, mood), exist_ok=True)

# === INIT WEBCAM ===
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

print("\n📸 Mood Capture Started!")
print("Press [SPACE] to capture an image, [ESC] to quit.\n")

for mood in moods:
    print(f"➡️ Capturing images for mood: {mood}")
    print("Position your face and press SPACE to capture...")

    saved = 0
    while saved < num_images_per_mood:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        cv2.putText(frame, f"Mood: {mood} ({saved}/{num_images_per_mood})",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        cv2.imshow("Mood Capture", frame)

        key = cv2.waitKey(1)

        if key == 27:  # ESC key to exit
            print("❌ Exiting early...")
            cap.release()
            cv2.destroyAllWindows()
            exit()

        if key == 32:  # SPACE to save frame
            file_path = os.path.join(base_dir, mood, f"{mood.lower()}_{saved}.jpg")
            cv2.imwrite(file_path, frame)
            saved += 1

    print(f"✅ Finished capturing for mood: {mood}\n")

print("🎉 Done capturing all moods.")
cap.release()
cv2.destroyAllWindows()
