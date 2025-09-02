# 🚀 FakeDataForge  

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()  
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-orange.svg)]()  
[![Status](https://img.shields.io/badge/Project-Active-success.svg)]()  

**FakeDataForge** is a modular CLI toolkit for **data generation, file conversion, and visualization**.  
It helps developers, testers, and data engineers quickly create realistic datasets, convert between formats, and inspect data right from the terminal.  

---

## ✨ Features  

✅ **Fake Data Generator**  
- Generate synthetic datasets with primary/foreign key relationships.  
- Customize number of rows, column types, and relationships.  
- Output directly to CSV for easy integration.  

✅ **File Converter**  
- Convert files between **CSV, Parquet, and Excel (XLS/XLSX)** formats.  
- Simple one-line commands, powered by **Pandas** + **PyArrow**.  

✅ **Data Visualization**  
- Preview datasets in a clean **tabular terminal view**.  
- (coming soon)Support for filtering, sorting, and pagination.  

---

## 🛠️ Tech Stack  

- **Python 3.8+**  
- [Faker](https://faker.readthedocs.io/) → Synthetic data generation  
- [Pandas](https://pandas.pydata.org/) → File handling & conversion  
- [PyArrow](https://arrow.apache.org/) → Parquet support  
- [Typer](https://typer.tiangolo.com/) → Modern CLI framework  

---

## 📦 Installation  

Clone the repo and install in editable mode:  

```bash
git clone https://github.com/yourusername/FakeDataForge.git
cd FakeDataForge
pip install -e .
```

## 🚀 Usage  

### 1️⃣ Generate Fake Data  
```bash
fakegen 
```
👉 Generates a dataset with 1,000 rows based on your schema.


2️⃣ Convert Files
```
convertfile data.csv --output data.parquet
```

👉 Converts CSV to Parquet. Supported formats: csv, parquet, xls, xlsx.

3️⃣ Visualize Data
```
visualize data.csv
```

👉 Opens a pretty terminal table view of the file.



## 🌟 Why FakeDataForge?

⚡ **All-in-one tool** for test data workflows.  

🛠️ **Modular & Extensible** – easy to add new features.  

📊 **Practical for Devs & Data Engineers** – no more manual file conversions.  


---

## 📌 Roadmap
- [x] Fake data generation (CSV)  
- [x] File conversion (CSV ↔ Parquet ↔ Excel)  
- [x] File visualization in terminal (pretty tables)  
- [ ] REST API interface (optional future)  
- [ ] Dockerized version  

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!  
Feel free to fork, open PRs, or suggest ideas.  

---

## 👩‍💻 Author
**Sapna Singh Khatik**  
📧 [sapnasinghkhatik@gmail.com](mailto:sapnasinghkhatik@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/sapna-singh-khatik/)

---

## 📜 License
Licensed under the **MIT License** – feel free to use, modify, and share.  

---

⚡ *FakeDataForge – Making data workflows faster, easier, and smarter.* ⚡
