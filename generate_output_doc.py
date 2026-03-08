import os
import glob
from docx import Document
from docx.shared import Inches

OUTPUT_DIR = "CG-Lab-Outputs"
IMAGE_ORDER = ["output_console.png", "output_gui.png", "output_zoomed.png"]

def generate_doc_for_lab(lab_folder):
    lab_name = lab_folder.rstrip('/')

    images_found = []
    for img_name in IMAGE_ORDER:
        img_path = os.path.join(lab_folder, img_name)
        if os.path.exists(img_path):
            images_found.append(img_path)

    # catch any extra output_*.png not in standard order
    for img in sorted(glob.glob(os.path.join(lab_folder, 'output_*.png'))):
        if img not in images_found:
            images_found.append(img)

    if not images_found:
        print(f"  [SKIP] No output images in {lab_folder}")
        return

    print(f"  [BUILD] {lab_name} -> {len(images_found)} image(s)")

    doc = Document()

    section = doc.sections[0]
    section.top_margin    = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin   = Inches(1)
    section.right_margin  = Inches(1)

    for img_path in images_found:
        para = doc.add_paragraph()
        run = para.add_run()
        try:
            run.add_picture(img_path, width=Inches(5.5))
        except Exception as e:
            print(f"    [WARN] {img_path}: {e}")
            para.add_run(f"[Image not found: {os.path.basename(img_path)}]")
        doc.add_paragraph()  # spacing between images

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, f"{lab_name}-output_print.docx")
    doc.save(out_path)
    print(f"  [SAVED] {out_path}")

if __name__ == "__main__":
    print("Scanning for lab folders...")
    lab_folders = sorted(glob.glob("Lab-*/"))
    if not lab_folders:
        print("No lab folders found. Run from repo root.")
        exit(1)
    for lab in lab_folders:
        generate_doc_for_lab(lab)
    print("\nDone! Check CG-Lab-Outputs/")
