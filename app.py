import streamlit as st
from utils import Product, Inventory

if "inventory" not in st.session_state:
    st.session_state.inventory=Inventory()

st.title("📦 Inventory Management System")

menu=["Add New Item","View Inventory", "Update Item", "Remove Item", "Reports"]
choice=st.sidebar.selectbox("Menu",menu)

inventory=st.session_state.inventory

if choice=="Add New Item":
    st.subheader("➕ Add Product")
    name=st.text_input("Product Name")
    category=st.text_input("Category")
    price=st.number_input("Price",min_value=0.0, step=0.01)
    quantity=st.number_input("Quantity",min_value=0, step=1)

    if st.button("Add Product"):
        if name and category:
            new_product=Product(name, category, price, quantity)
            success=inventory.add_product(new_product)
            if success:
                st.success(f"✅ {name} added successfully!")
            else:
                st.warning("⚠️ Product already exists")
    else:
        st.error("⚠️ Please Fill all fields.")

elif choice=="View Inventory":
    st.subheader("📋 Current Inventory")
    if inventory.products:
        data=[
            {
                "Name":p.name,
                "Category":p.category,
                "Price":p.price,
                "Quantity":p.quantity,

            }
            for p in inventory.products
        ]
        st.table(data)
    else:
        st.info("No products in inventory yet.")
elif choice=="Update Item":
    st.subheader("✏️ Update Product")
    product_names=[p.name for p in inventory.products]

    if product_names:
        selected=st.selectbox("Select Product", product_names)

        update_option=st.radio("What do you want to update?",["Category","Price","Quantity"])
        if update_option=="Category":
            new_category=st.text_input("Enter new category")
            if st.button("Update Category"):
                if inventory.update_category(selected, new_category):
                    st.success("✅ Category updated!")
        elif update_option=="Price":
            new_price=st.number_input("Enter new price",min_value=0.0,step=0.01)
            if st.button("Update Price"):
                if inventory.update_price(selected, new_price):
                    st.success("✅ Price Updated!")
        elif update_option=="Quantity":
            new_qty=st.number_input("Add quantity",min_value=0, step=1)
            if st.button("Update Quantity"):
                if inventory.update_stock(selected, new_qty):
                    st.success("✅ Quantity updated!")
    else:
        st.warning("⚠️ No Products available to update.")

elif choice=="Remove Item":
    st.subheader("🗑️ Remove Product")
    product_names=[p.name for p in inventory.products]
    if product_names:
        selected=st.selectbox("Selected Product to Remove",product_names)
        if st.button("Delete Product"):
            if inventory.delete_product(selected):
                st.success(f"✅ {selected} removed successfully!")
    else:
        st.warning("⚠️ No products available to delete.")
elif choice=="Reports":
    st.subheader("📊 Inventory Reports")

    total_value=inventory.get_total_value()
    st.metric("💰 Total Inventory Value",f"{total_value:.2f}")

    st.write("📂 Products by category")
    summary=inventory.get_category_summary()
    if summary:
        st.bar_chart(summary)
    else:
        st.info("No Categories to display.")
    st.write("⚠️ Low Stock Products (<5 units)")
    low_stock=inventory.get_low_stock()
    if low_stock:
        low_data=[{"Name":p.name, "Quantity":p.quantity} for p in low_stock]
        st.table(low_data)
    else:
        st.success("✅ No low stock products!")

