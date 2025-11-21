import json

notebook_path = '/home/sanjaa/Documents/CJAY/code/muis_digital_image_processing/Lab5/object_detction_&blurring_realtime.ipynb'

with open(notebook_path, 'r') as f:
    nb = json.load(f)

# Helper to create a code cell
def create_code_cell(source):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": source if isinstance(source, list) else [l + '\n' for l in source.split('\n')]
    }

# Helper to create a markdown cell
def create_markdown_cell(source):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": source if isinstance(source, list) else [l + '\n' for l in source.split('\n')]
    }

new_cells = []

# Keep the first few cells (imports and loading image)
# Cell 0: Markdown title
new_cells.append(nb['cells'][0])
# Cell 1: Markdown task 1
new_cells.append(nb['cells'][1])
# Cell 2: Imports
new_cells.append(nb['cells'][2])
# Cell 3: Markdown task 2
new_cells.append(nb['cells'][3])
# Cell 4: Load image
new_cells.append(nb['cells'][4])
# Cell 5: Markdown task 3 (Display function)
new_cells.append(nb['cells'][5])

# Cell 6: Display function implementation
display_code = """def display(img):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    new_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    ax.imshow(new_img)

display(img)"""
new_cells.append(create_code_cell(display_code))

# Cell 7: Markdown task 4 (Load Cascade)
new_cells.append(create_markdown_cell("Даалгавар: haarcascade_russian_plate_number.xml-г дуудаж plate_cascade хувьсагчид хадгал"))

# Cell 8: Load Cascade implementation
load_cascade_code = """plate_cascade = cv2.CascadeClassifier('../images/haarcascades/haarcascade_russian_plate_number.xml')"""
new_cells.append(create_code_cell(load_cascade_code))

# Cell 9: Markdown task 5 (Detect Plate)
new_cells.append(create_markdown_cell("Даалгавар: detect_plate нэртэй фүнкц бич. Фүнкц нь зураг хүлээж аваад машины дугаарыг илрүүлж тэр хэсгийг бүрсийлгэж буцаадаг байна."))

# Cell 10: Detect Plate implementation
detect_plate_code = """def detect_plate(img):
    plate_img = img.copy()
    roi = img.copy()
    plate_rects = plate_cascade.detectMultiScale(plate_img, scaleFactor=1.3, minNeighbors=3)
    
    for (x,y,w,h) in plate_rects:
        roi = plate_img[y:y+h, x:x+w]
        blurred_roi = cv2.medianBlur(roi, 7)
        plate_img[y:y+h, x:x+w] = blurred_roi
        
    return plate_img"""
new_cells.append(create_code_cell(detect_plate_code))

# Cell 11: Markdown task 6 (Run detection)
new_cells.append(create_markdown_cell("Даалгавар: Үр дүнгээ шалга."))

# Cell 12: Run detection implementation
run_detection_code = """result = detect_plate(img)
display(result)"""
new_cells.append(create_code_cell(run_detection_code))

nb['cells'] = new_cells

with open(notebook_path, 'w') as f:
    json.dump(nb, f, indent=1)

print("Notebook updated successfully")
