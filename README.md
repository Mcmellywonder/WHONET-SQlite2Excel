# WHONET SQLite to Excel Converter 🧬📊

This Python application provides a simple graphical interface to convert `.SQLite` database files from WHONET into Excel spreadsheets. 
It is designed for ease of use by researchers, lab technicians, and data analysts working with antimicrobial resistance data.

## 🚀 Features

- Upload `.SQLite` files from WHONET
- Validate file format before conversion
- Convert each table in the database to separate Excel files
- Automatically creates an output folder to store converted files
- Simple GUI built with Tkinter

## 📁 Folder Structure


## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mcmellywonder/WHONET-SQlite2Excel.git
   cd whonet-sqlite-to-excel
   ```
   or
   ```   bash
         https://github.com/Mcmellywonder/WHONET-SQlite2Excel
   ```

3. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🧑‍💻 How to Use

### Step-by-Step Instructions

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Upload File**
   - Click the “Browse” button to select a `.SQLite` or `.db` file exported from WHONET.

3. **Validate**
   - The app checks if the file is a valid SQLite database.

4. **Convert**
   - Click “Convert” to start the process.
   - Each table in the database will be saved as a separate Excel file.

5. **Download**
   - Converted files are automatically saved in the `output/` folder.
   - A success message will confirm completion.

## 📦 Dependencies

- `pandas` – for data manipulation and Excel export
- `openpyxl` – for writing Excel files
- `tkinter` – for GUI interface (built-in with Python)

## 📸 Screenshots

_Add screenshots of the GUI here (optional)_

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

```

Would you like help customizing this for your GitHub username or adding screenshots and sample files to the repo?
