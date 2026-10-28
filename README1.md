# 3D Point Cloud Processing & Metadata Extraction Tool 🌐

An interactive, web-based analytical application designed to parse, analyze, and extract spatial metadata from 3D point cloud datasets. The tool natively supports `.las`, `.laz`, and `.ply` file formats, processing spatial coordinates, density attributes, bounding box metrics, and generating executive summary PDF reports on demand.

---

## 🛠️ Technology Stack & Deep Tool Breakdown

This application leverages specialized open-source geospatial, analytical, and visualization libraries. Below is the detailed breakdown of how each tool operates within the architecture:

### 1. User Interface & Workflow Engine
* **`streamlit`** (Web Framework): 
  * Powers the real-time, responsive interactive dashboard.
  * Handles multi-file upload workflows (`.las`, `.laz`, `.ply`) with dynamic drag-and-drop support.
  * Controls session state management for efficient rendering of large datasets without re-execution overhead.
  * Renders inline metric cards, interactive dataframes, progress bars, and plot canvases.

### 2. Point Cloud Data Parsing & Spatial Libraries
* **`laspy` [with `lazrs` / `laszip` backend]**:
  * **Purpose**: Primary parser for ASPRS LiDAR data formats (`.las` and compressed `.laz`).
  * **Deep Functionality**: Reads header blocks, extracts X, Y, Z coordinate channels, classification codes, return numbers, intensity values, and GPS time tags without loading full uncompressed payloads into memory when probing metadata.
* **`plyfile`**:
  * **Purpose**: Parser for Polygon File Format (`.ply`) datasets.
  * **Deep Functionality**: Extracts custom ASCII and Binary header elements, vertex lists, face indices, element properties, and color channels (RGB).

### 3. Numerical Processing & Analytics Core
* **`numpy`**:
  * Executes fast vector computations, array manipulations, dynamic minimum/maximum spatial bounding box recalculations, and density matrix transformations.
* **`pandas`**:
  * Converts extracted spatial metadata and attribute tables into structured DataFrames.
  * Manages tabular filtering, summary stats generation, and export structures.

### 4. Data Visualization & Profiling
* **`matplotlib` & `seaborn`**:
  * Renders 2D height distribution histograms, coordinate density heatmaps, and spatial bounding envelopes.
  * Generates clean chart figures embedded directly inside the Streamlit view and exported into PDF summaries.

### 5. Automated PDF Report Generation
* **`reportlab`**:
  * **Purpose**: Programmatic PDF document creation engine.
  * **Deep Functionality**: Compiles dynamic spatial metadata summary tables, project statistics, and embedded visualization plots into structured executive PDF reports available for instant download.

---

## 📌 Features

* **Multi-Format 3D File Support**: Native parsing for ASPRS LiDAR (`.las`), compressed LiDAR (`.laz`), and Polygon File Format (`.ply`).
* **Deep Spatial Parameter Extraction**:
  * Total point counts, spatial bounding boxes ($\Delta X, \Delta Y, \Delta Z$), point density per $m^2 / m^3$.
  * Coordinate range bounds ($X_{min}, X_{max}, Y_{min}, Y_{max}, Z_{min}, Z_{max}$).
  * Sensor elevation profiling and spatial extent summary.
* **Automated PDF Export**: One-click generation of formatted executive summary documents containing charts and data summaries.
* **Interactive Data Table Preview**: Dynamic viewing and filtering of tabular point attribute distributions.

---

## 📋 System Requirements & Prerequisites

### 1. System Specifications
| Component | Minimum Requirement | Recommended Specification |
| :--- | :--- | :--- |
| **Operating System** | Windows 10/11, macOS, or Ubuntu 20.04+ | Windows 11 / Linux Server |
| **Python Version** | Python 3.8 | Python 3.10 / 3.11 |
| **RAM** | 4 GB | 8 GB – 16 GB (for processing heavy `.las`/`.laz` files) |
| **Storage** | 500 MB free disk space | 2 GB+ SSD storage |

### 2. Complete Python Dependencies (`requirements.txt`)

Below are the explicit requirements used by this project:

```text
streamlit>=1.28.0
laspy[lazrs]>=2.5.0
plyfile>=1.0.0
reportlab>=4.0.0
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0
openpyxl>=3.1.0
```

---

## 🚀 Quick Start & Setup Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/3d-point-cloud-tool.git
cd 3d-point-cloud-tool
```

### Step 2: Create a Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Packages
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 📂 Project Directory Structure

```text
3d-point-cloud-tool/
├── app.py                      # Main Streamlit web application & UI pipeline
├── requirements.txt            # Complete list of Python package dependencies
├── README.md                   # Detailed project documentation
├── utils/
│   ├── __init__.py
│   ├── las_parser.py           # Parsing logic for .las / .laz files using laspy
│   ├── ply_parser.py           # Parsing logic for .ply files using plyfile
│   └── pdf_generator.py        # PDF document layout generation using ReportLab
└── assets/
    └── sample_pointcloud.las   # Sample data for testing
```

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).