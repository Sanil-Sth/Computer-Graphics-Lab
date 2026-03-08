import os
import glob
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────

# Output folder where all docx files will be saved
OUTPUT_DIR = "CG-Lab-Outputs"

# The exact order images should appear in the doc
IMAGE_ORDER = ["output_console.png", "output_gui.png", "output_zoomed.png"]

# ─────────────────────────────────────────────
# HELPER: Add a bordered box around a paragraph
# (mimics the box style in DSA lab output)
# ─────────────────────────────────────────────
def add_border_to_paragraph(paragraph):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')

    for side in ['top', 'left', 'bottom', 'right']:
        border = OxmlElement(f'w:{side}')
        border.set(qn('w:val'), 'single')
        border.set(qn('w:sz'), '6')
        border.set(qn('w:space'), '4')
        border.set(qn('w:color'), '000000')
        pBdr.append(border)

    pPr.append(pBdr)

# ─────────────────────────────────────────────
# HELPER: Set paragraph spacing
# ─────────────────────────────────────────────
def set_spacing(paragraph, before=0, after=0):
    pPr = paragraph._p.get_or_add_pPr()
    spacing = OxmlElement('w:spacing')
    spacing.set(qn('w:before'), str(before))
    spacing.set(qn('w:after'), str(after))
    pPr.append(spacing)

# ─────────────────────────────────────────────
# MAIN: Generate docx for a single lab folder
# ─────────────────────────────────────────────
def generate_doc_for_lab(lab_folder):

    # e.g. "Lab-01-DDA-Line/" -> "Lab-01-DDA-Line"
    lab_name = lab_folder.rstrip('/')

    # Find which images exist in this lab folder, in the correct order
    images_found = []
    for img_name in IMAGE_ORDER:
        img_path = os.path.join(lab_folder, img_name)
        if os.path.exists(img_path):
            images_found.append(img_path)

    # Also catch any output_*.png not in the standard order list
    all_outputs = glob.glob(os.path.join(lab_folder, 'output_*.png'))
    for img in sorted(all_outputs):
        img_filename = os.path.basename(img)
        if img_filename not in IMAGE_ORDER and img not in images_found:
            images_found.append(img)

    # Skip if no output images found
    if not images_found:
        print(f"  [SKIP] No output images found in {lab_folder}")
        return

    print(f"  [BUILD] {lab_name} → {len(images_found)} image(s) found")

    # Create the Word document
    doc = Document()

    # Set narrow margins (matching DSA lab style)
    section = doc.sections[0]
    section.top_margin    = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin   = Inches(1)
    section.right_margin  = Inches(1)

    # For each image, add: "OUTPUT :" label + bordered image block
    for i, img_path in enumerate(images_found):

        # "OUTPUT :" heading
        label = doc.add_paragraph()
        label_run = label.add_run("OUTPUT :")
        label_run.bold = True
        label_run.font.size = Pt(12)
        set_spacing(label, before=100, after=40)

        # Image inside a bordered paragraph
        img_para = doc.add_paragraph()
        img_para.alignment = WD_ALIGN_PARAGRAPH.LEFT
        add_border_to_paragraph(img_para)
        set_spacing(img_para, before=40, after=40)

        run = img_para.add_run()
        try:
            run.add_picture(img_path, width=Inches(5.5))
        except Exception as e:
            print(f"    [WARN] Could not add image {img_path}: {e}")
            img_para.add_run(f"[Image not found: {os.path.basename(img_path)}]")

        # Spacer between images (except after last one)
        if i < len(images_found) - 1:
            spacer = doc.add_paragraph()
            set_spacing(spacer, before=0, after=100)

    # ─── Save the docx ───
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_filename = f"{lab_name}-output_print.docx"
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    doc.save(output_path)
    print(f"  [SAVED] {output_path}")

# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("🔍 Scanning for lab folders...")

    # Find all Lab-* folders, sorted so they go Lab-01, Lab-02, ...
    lab_folders = sorted(glob.glob("Lab-*/"))

    if not lab_folders:
        print("No lab folders found. Make sure you run this from the repo root.")
        exit(1)

    for lab in lab_folders:
        generate_doc_for_lab(lab)

    print("\n✅ Done! Check the CG-Lab-Outputs/ folder.")
