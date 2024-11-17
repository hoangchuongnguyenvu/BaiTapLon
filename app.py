import streamlit as st

st.set_page_config(
    page_title="Computer Vision App",
    layout="wide"
)

st.markdown("""
    <style>
        /* Tùy chỉnh sidebar */
        section[data-testid="stSidebar"] > div {
            padding: 1rem;
            background-color: #f8f9fa;
        }
        
        /* Tùy chỉnh expander */
        .st-emotion-cache-j5r0tf {
            background-color: white;
            border-radius: 10px;
            padding: 1rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        /* Tùy chỉnh radio buttons */
        div.st-emotion-cache-1qg05tj {
            padding: 0.5rem;
        }
        
        /* Style cho từng option */
        div.st-emotion-cache-1qg05tj label {
            padding: 0.7rem 1rem;
            margin: 0.3rem 0;
            border-radius: 7px;
            transition: all 0.2s ease;
            cursor: pointer;
        }
        
        /* Hiệu ứng hover */
        div.st-emotion-cache-1qg05tj label:hover {
            background-color: #f0f4f8;
            transform: translateX(5px);
        }
        
        /* Option được chọn */
        div.st-emotion-cache-1qg05tj label[data-checked="true"] {
            background-color: #ff4b4b15;
            color: #ff4b4b;
            font-weight: 500;
            border-left: 3px solid #ff4b4b;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    with st.sidebar.expander("💻 Computer Vision Applications", expanded=True):
        navigation = st.radio(
            label="Navigation",
            options=[
                "Ứng dụng tách nền bằng thuật toán GrabCut",
                "Phân đoạn ký tự bằng Watershed Segmentation",
                "Phát hiện khuôn mặt với Haar Features",
                "Ứng dụng xác nhận khuôn mặt",
                "Phát hiện Keypoint trên Synthetic Sequences",
                "So khớp Keypoint dựa trên tiêu chí Lowe",
                "Tìm kiếm ảnh chứa đối tượng truy vấn",
                "Object Tracking"
            ],
            label_visibility="collapsed"
        )
    
    if navigation == "Object Tracking":
        from apps.ObjectTracking import main as show_tracking
        show_tracking()
    else:
        st.title("Tính năng đang được phát triển...")
        st.info("Vui lòng quay lại sau!", icon="ℹ️")

if __name__ == "__main__":
    main()