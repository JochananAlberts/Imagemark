# Watermarking App Project

# Project Structure

This project is organized as follows:

📂 Imagemark
│── 📂 assets              # Store fonts, default images, icons  
│── 📂 src                 # Main application source code  
│   ├── main.py            # Entry point of the application  
│   ├── ui.py              # PySide6 UI layout and logic  
│   ├── image_processor.py # Handles watermarking logic  
│   ├── utils.py           # Helper functions (resizing, file handling)  
│── 📂 tests               # Unit tests
│── README.md              # Project description and usage guide  
│── requirements.txt       # Dependencies (PySide6, Pillow)


# TODO Day 1: Project Setup & UI Design
--------------------------------------
- ✅ Set up the project folder and initialize Git
- ✅ Install required libraries (`PySide6`, `Pillow`)
- ✅ Design the layout:
    - Image on the left
    - Controls (buttons, sliders, text input) on the right
- ❌ Create a basic PySide6 GUI with a file upload button

# TODO Day 2: Load & Display Images
------------------------------------
- ❌ Implement image loading and resizing to fit the UI
- ❌ Show the image on a `QLabel`
- ❌ Ensure it scales up/down while maintaining aspect ratio

# TODO Day 3: Adding Watermark Text
-----------------------------------
- ❌ Add a text input field for the watermark
- ❌ Overlay watermark on the image
- ❌ Ensure changes appear immediately when typing
- ❌ Allow users to change the font style and size

# TODO Day 4: Watermark Positioning & Customization
---------------------------------------------------
- ❌ Add arrow buttons to move the watermark
- ❌ Implement font size adjustment
- ❌ Allow users to change watermark transparency

# TODO Day 5: Final Touches & Saving Images
-------------------------------------------
- ❌ Add a "Save" button to export the watermarked image
- ❌ Ensure saved images match the preview
- ❌ Test different images to check stability

# TODO Day 6: Bug Fixing & Optimization
--------------------------------------
- ❌ Fix any UI glitches
- ❌ Optimize code for responsiveness
- ❌ Refactor code for readability

# TODO Day 7: Documentation & Polish
-----------------------------------
- ❌ Finish the `README.md` with usage instructions
- ❌ Add comments & clean up code
- ❌ Push the final project to GitHub
