import os

neg_dir = r"C:\project\negatives"
output_file = "bg.txt"

with open(output_file, "w") as f:
    for filename in os.listdir(neg_dir):
        if filename.lower().endswith((".jpg", ".png")):
            full_path = os.path.join(neg_dir, filename)
            f.write(full_path + "\n")

print(f"{output_file} 已生成，包含 {neg_dir} 裡的負樣本圖片路徑。")
