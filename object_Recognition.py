from ultralytics import YOLO
import cv2
import os

# تحميل نموذج YOLOv8
model = YOLO("yolov8n.pt")

# إنشاء مجلد output إذا لم يكن موجودًا
os.makedirs("output", exist_ok=True)

# أسماء الصور
image_files = [
    "animals.jpg",
    "office.jpg",
    "street.jpg"
]

# المرور على جميع الصور
for image_name in image_files:

    # مسار الصورة
    image_path = os.path.join("images", image_name)

    # قراءة الصورة
    image = cv2.imread(image_path)

    if image is None:
        print(f"❌ Could not open {image_name}")
        continue

    # التعرف على الأجسام
    results = model(image)

    # رسم النتائج
    result_image = results[0].plot()

    # حفظ الصورة
    output_path = os.path.join("output", image_name)
    cv2.imwrite(output_path, result_image)

    print(f"✅ {image_name} processed successfully.")

    # عرض الصورة
    cv2.imshow("Object Recognition", result_image)

    print("Press any key to continue to the next image...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("\n🎉 All images have been processed successfully!")