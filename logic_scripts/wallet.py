# pyzbar: Scans barcodes and QR codes.pillow: Image library needed for pyzbar to read image files.
# pip install pyzbar pillow

# sudo apt update, sudo apt install -y tesseract-ocr, pip install pytesseract

import cv2
from pyzbar.pyzbar import decode


def scan_barcodes():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        for barcode in decode(frame):
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type
            print(f"Found {barcode_type} barcode: {barcode_data}")
            # Draw rectangle and text around the barcode
            points = barcode.polygon
            pts = [(p.x, p.y) for p in points]
            cv2.polylines(frame, [np.array(pts, dtype=np.int32)], True, (0, 255, 0), 2)
            cv2.putText(
                frame,
                barcode_data,
                (pts[0][0], pts[0][1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 0, 0),
                2,
            )

        cv2.imshow("Barcode Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


scan_barcodes()
