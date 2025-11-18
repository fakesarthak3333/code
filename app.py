import streamlit as st

# 1. Website ka Title
st.set_page_config(page_title="store", page_icon="🛒")
st.title("🥦 Instant Store")
st.write("based on python!")

# 2. 'Session State' (Yaani Cart ki memory)
if 'cart' not in st.session_state:
    st.session_state.cart = []

# 3. Hamare Products (Naam aur Price)
products = [
    {"name": "Basmati Rice 🍚", "price": 120},
    {"name": "Toor Dal 🥣", "price": 150},
    {"name": "Sunflower Oil 🌻", "price": 180},
    {"name": "Sugar 🍬", "price": 45},
    {"name": "Aata 🌾", "price": 40},
    {"name": "Namak 🧂", "price": 20},
]

# 4. Screen ko 2 hisson mein baato (Left: Items, Right: Bill)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🛒 Items Kharido")
    
    # Har product ke liye ek card aur button banayein
    for item in products:
        # Ek line mein teen cheezein: Naam, Price, Button
        c1, c2, c3 = st.columns([3, 2, 2])
        
        c1.write(f"**{item['name']}**")
        c2.write(f"₹{item['price']}")
        
        # Button dabane par kya hoga
        if c3.button(f"Add", key=item['name']):
            st.session_state.cart.append(item)
            st.success(f"{item['name']} added!")
            st.rerun() # Page refresh karo taaki bill update ho

with col2:
    st.subheader("🧾 Aapka Bill")
    
    if len(st.session_state.cart) > 0:
        total = 0
        # Cart mein jo bhi hai use dikhao
        for i, cart_item in enumerate(st.session_state.cart):
            st.write(f"{i+1}. {cart_item['name']} - ₹{cart_item['price']}")
            total += cart_item['price']
        
        st.markdown("---")
        st.markdown(f"### Total: ₹{total}")
        
        # Cart Khali karne ka button
        if st.button("Clear Cart ❌"):
            st.session_state.cart = []
            st.rerun()
            
    else:
        st.info("Cart khali hai abhi.")