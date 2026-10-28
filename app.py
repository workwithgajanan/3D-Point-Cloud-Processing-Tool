import streamlit as st
import open3d as o3d
import numpy as np
from fpdf import FPDF
import tempfile
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="3D PLY Analyzer",
    page_icon="🧊",
    layout="centered"
)

# --- Custom CSS Design ---
custom_css = """
<style>
    /* Main Background & Font */
    .stApp {
        background-color: #F8FAFC;
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Styling */
    .main-header {
        text-align: center;
        padding: 20px 0 10px 0;
    }
    .main-title {
        color: #0F172A;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 5px;
    }
    .main-subtitle {
        color: #64748B;
        font-size: 1rem;
        margin-bottom: 25px;
    }

    /* Metric Cards Styling */
    .card {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        border: 1px solid #E2E8F0;
        margin-bottom: 15px;
        transition: transform 0.2s ease;
    }
    .card:hover {
        transform: translateY(-2px);
        border-color: #3B82F6;
    }
    .card-label {
        color: #64748B;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .card-value {
        color: #1E293B;
        font-size: 1.25rem;
        font-weight: 700;
        margin-top: 4px;
    }

    /* Custom Primary Download Button */
    .stDownloadButton > button {
        width: 100% !important;
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%) !important;
        color: #FFFFFF !important;
        border-radius: 10px !important;
        padding: 12px 20px !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        border: none !important;
        box-shadow: 0 4px 10px rgba(37, 99, 235, 0.25) !important;
        transition: all 0.3s ease !important;
    }
    .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #1D4ED8 0%, #1E40AF 100%) !important;
        box-shadow: 0 6px 15px rgba(37, 99, 235, 0.4) !important;
        transform: translateY(-2px);
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- PDF Report Function ---
def generate_pdf_report(file_name, point_count, x_range, y_range, z_range):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="3D Point Cloud (PLY) Analysis Report", ln=True, align='C')
    pdf.ln(10)
    
    # Content
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"File Name: {file_name}", ln=True)
    pdf.cell(200, 10, txt=f"Total 3D Points: {point_count:,}", ln=True)
    pdf.ln(5)
    
    pdf.cell(200, 10, txt="Bounding Box Details (Spatial Dimensions):", ln=True)
    pdf.cell(200, 10, txt=f"- X Axis Range: {x_range[0]:.2f} to {x_range[1]:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"- Y Axis Range: {y_range[0]:.2f} to {y_range[1]:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"- Z Axis (Height): {z_range[0]:.2f} to {z_range[1]:.2f}", ln=True)
    
    pdf.ln(10)
    pdf.cell(200, 10, txt="Status: Processed Successfully", ln=True)
    
    return pdf.output(dest='S').encode('latin-1')

# --- Header Section ---
st.markdown("""
    <div class="main-header">
        <div class="main-title">🧊 3D PLY File Analyzer</div>
        <div class="main-subtitle">Upload your 3D Point Cloud file to inspect spatial coordinates & generate instant PDF reports.</div>
    </div>
""", unsafe_allow_html=True)

# --- File Uploader ---
uploaded_file = st.file_uploader("Choose a .ply file", type=["ply"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".ply") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_path = tmp_file.name

    try:
        pcd = o3d.io.read_point_cloud(tmp_path)
        points = np.asarray(pcd.points)
        
        if len(points) == 0:
            st.error("Error: The uploaded file contains no 3D points or is corrupted.")
        else:
            point_count = len(points)
            x_range = (np.min(points[:, 0]), np.max(points[:, 0]))
            y_range = (np.min(points[:, 1]), np.max(points[:, 1]))
            z_range = (np.min(points[:, 2]), np.max(points[:, 2]))
            
            st.markdown("---")
            st.subheader("📊 Spatial Data Summary")

            # --- Dashboard Cards (2x2 Layout) ---
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown(f"""
                    <div class="card">
                        <div class="card-label">Total 3D Points</div>
                        <div class="card-value">{point_count:,}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown(f"""
                    <div class="card">
                        <div class="card-label">X Range (Width)</div>
                        <div class="card-value">{x_range[0]:.2f} to {x_range[1]:.2f}</div>
                    </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                    <div class="card">
                        <div class="card-label">Z Range (Height)</div>
                        <div class="card-value">{z_range[0]:.2f} to {z_range[1]:.2f}</div>
                    </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                    <div class="card">
                        <div class="card-label">Y Range (Depth)</div>
                        <div class="card-value">{y_range[0]:.2f} to {y_range[1]:.2f}</div>
                    </div>
                """, unsafe_allow_html=True)

            # --- Download Button Section ---
            pdf_bytes = generate_pdf_report(uploaded_file.name, point_count, x_range, y_range, z_range)
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.download_button(
                label="📥 Download Detailed PDF Report",
                data=pdf_bytes,
                file_name=f"{uploaded_file.name}_Report.pdf",
                mime="application/pdf"
            )

    except Exception as e:
        st.error(f"Failed to process file: {e}")
    
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)