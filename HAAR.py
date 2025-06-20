import cv2

# === 1. 載入訓練好的 Haar cascade 分類器 ===
cascade_path = r"C:\project\HAAR\cascade.xml"  # <== 替換成你的 XML 路徑
cascade = cv2.CascadeClassifier(cascade_path)

# === 2. 開啟攝影機 ===
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ 無法開啟攝影機，請檢查連線或 iVCam")
    exit()

print("✅ 攝影機啟動成功，按 q 鍵結束")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ 無法讀取影像")
        break

    # === 3. 前處理：灰階 + 降噪 ===
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)

    # === 4. 執行 cascade 偵測 ===
    objects = cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,     # 精細掃描
        minNeighbors=30,      # 更保守，降低誤判
        minSize=(40, 40),     # 偵測物件最小尺寸
    )

    # === 5. 過濾小誤框，只顯示可能是校徽的 ===
    for (x, y, w, h) in objects:
        area = w * h
        if area < 2500:  # 過濾太小的誤框（面積太小）
            continue

        # 繪製框與文字
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # === 6. 顯示畫面 ===
    cv2.imshow("Real-Time Object Detection - Haar Cascade", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# === 7. 清理 ===
cap.release()
cv2.destroyAllWindows()
print("👋 程式結束，攝影機已關閉")

