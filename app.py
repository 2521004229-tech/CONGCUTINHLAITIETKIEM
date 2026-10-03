import streamlit as st
 st.image("IMG_3011.jpeg")

# ==============================
# CẤU HÌNH TRANG
# ==============================
st.set_page_config(
    page_title="Tính lãi gửi tiết kiệm",
    page_icon="💰",
    layout="centered"
)

# ==============================
# TIÊU ĐỀ
# ==============================
st.title("💰 TÍNH LÃI GỬI TIẾT KIỆM")
st.write("Nhập thông tin tiền gửi để tính số tiền lãi và tổng tiền nhận.")

st.divider()

# ==============================
# NHẬP THÔNG TIN
# ==============================

# Số tiền gửi
tien_gui = st.number_input(
    "💵 Số tiền gửi (VNĐ)",
    min_value=0.0,
    value=10000000.0,
    step=500000.0,
    format="%.0f"
)

# Kỳ hạn
ky_han = st.number_input(
    "📅 Kỳ hạn (tháng)",
    min_value=1,
    max_value=120,
    value=12,
    step=1
)

# Lãi suất
lai_suat = st.number_input(
    "📈 Lãi suất (%/năm)",
    min_value=0.0,
    max_value=30.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

# Hình thức nhận lãi
hinh_thuc = st.selectbox(
    "💳 Hình thức nhận lãi",
    [
        "Cuối kỳ",
        "Hàng tháng",
        "Hàng quý"
    ]
)

st.divider()

# ==============================
# NÚT TÍNH
# ==============================

if st.button("🧮 TÍNH LÃI", use_container_width=True):

    if tien_gui <= 0:
        st.error("⚠️ Vui lòng nhập số tiền gửi lớn hơn 0.")
    
    elif lai_suat < 0:
        st.error("⚠️ Lãi suất không được nhỏ hơn 0.")
    
    else:
        # Lãi suất dạng thập phân
        lai_suat_nam = lai_suat / 100

        # Thời gian gửi tính theo năm
        thoi_gian_nam = ky_han / 12

        # ==============================
        # TÍNH TỔNG TIỀN LÃI
        # ==============================

        tong_tien_lai = tien_gui * lai_suat_nam * thoi_gian_nam

        # ==============================
        # TÍNH LÃI ĐỊNH KỲ
        # ==============================

        if hinh_thuc == "Cuối kỳ":
            tien_lai_dinh_ky = tong_tien_lai
            so_ky = 1
            ten_ky = "cuối kỳ"

        elif hinh_thuc == "Hàng tháng":
            tien_lai_dinh_ky = tong_tien_lai / ky_han
            so_ky = ky_han
            ten_ky = "tháng"

        else:  # Hàng quý
            so_quy = ky_han / 3
            tien_lai_dinh_ky = tong_tien_lai / so_quy
            so_ky = so_quy
            ten_ky = "quý"

        # ==============================
        # TỔNG TIỀN NHẬN
        # ==============================

        tong_tien_nhan = tien_gui + tong_tien_lai

        # ==============================
        # HIỂN THỊ KẾT QUẢ
        # ==============================

        st.success("✅ Tính toán thành công!")

        st.subheader("📊 KẾT QUẢ")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "💰 Tiền lãi định kỳ",
                f"{tien_lai_dinh_ky:,.0f} VNĐ"
            )

        with col2:
            st.metric(
                "📈 Tổng tiền lãi",
                f"{tong_tien_lai:,.0f} VNĐ"
            )

        st.metric(
            "💵 Tổng tiền gốc + lãi",
            f"{tong_tien_nhan:,.0f} VNĐ"
        )

        st.divider()

        # ==============================
        # CHI TIẾT
        # ==============================

        st.subheader("📋 Thông tin khoản gửi")

        st.write(f"**Số tiền gửi:** {tien_gui:,.0f} VNĐ")
        st.write(f"**Kỳ hạn:** {ky_han} tháng")
        st.write(f"**Lãi suất:** {lai_suat:.2f}%/năm")
        st.write(f"**Hình thức nhận lãi:** {hinh_thuc}")

        if hinh_thuc == "Cuối kỳ":
            st.info(
                f"Bạn nhận khoảng **{tong_tien_lai:,.0f} VNĐ tiền lãi** "
                f"vào cuối kỳ."
            )

        elif hinh_thuc == "Hàng tháng":
            st.info(
                f"Mỗi tháng bạn nhận khoảng "
                f"**{tien_lai_dinh_ky:,.0f} VNĐ tiền lãi**."
            )

        else:
            st.info(
                f"Mỗi quý bạn nhận khoảng "
                f"**{tien_lai_dinh_ky:,.0f} VNĐ tiền lãi**."
            )

# ==============================
# GHI CHÚ
# ==============================

st.divider()

st.caption(
    "📌 Công thức tính mang tính tham khảo: "
    "Tiền lãi = Tiền gửi × Lãi suất năm × Số tháng / 12. "
    "Lãi suất thực tế có thể khác tùy ngân hàng và sản phẩm tiền gửi."
)
