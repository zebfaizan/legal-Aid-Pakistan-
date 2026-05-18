import streamlit as st

st.set_page_config(page_title="Legal Aid Pakistan", page_icon="⚖️", layout="wide")
st.title("🇵🇰 Legal Aid Pakistan")
st.markdown("### Aapka legal masla hal karne mein madad")

# Warning
st.warning("⚠️ Ye tool sirf legal information ke liye hai. Kisi bhi legal action se pehle lawyer se zaroor rabta karein.")

# Session state initialize
if 'domain' not in st.session_state:
    st.session_state.domain = None
    st.session_state.step = 1
    st.session_state.answers = {}
    st.session_state.complete = False
    st.session_state.result = None

def reset_app():
    st.session_state.domain = None
    st.session_state.step = 1
    st.session_state.answers = {}
    st.session_state.complete = False
    st.session_state.result = None

# ============================================
# DOMAIN SELECTION
# ============================================
if st.session_state.domain is None:
    st.subheader("🔥 Apna masla chunein:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("👮 Police FIR nahi le rahe", use_container_width=True):
            st.session_state.domain = "fir"
            st.rerun()
    
    with col2:
        if st.button("💰 Tankhwah nahi mil rahi", use_container_width=True):
            st.session_state.domain = "salary"
            st.rerun()
    
    with col3:
        if st.button("💔 Talaq / Khula ka masla", use_container_width=True):
            st.session_state.domain = "divorce"
            st.rerun()

# ============================================
# DOMAIN 1: POLICE FIR
# ============================================
elif st.session_state.domain == "fir" and not st.session_state.complete:
    
    # Step 1
    if st.session_state.step == 1:
        st.subheader("📌 Sawaal 1/5")
        st.write("**Kya offense cognizable hai?** (qatal, daka, zina-bil-jabar, chori, maar-peet)")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Haan (Yes)", use_container_width=True):
                st.session_state.answers['Q1'] = 'Haan'
                st.session_state.step = 2
                st.rerun()
        with col2:
            if st.button("❌ Nahi (No)", use_container_width=True):
                st.session_state.answers['Q1'] = 'Nahi'
                st.session_state.result = "Ye offense cognizable nahi hai. Police ko FIR lene ki zaroorat nahi. Aap Private Complaint Magistrate Court mein kar sakte ho."
                st.session_state.complete = True
                st.rerun()
    
    # Step 2
    elif st.session_state.step == 2:
        st.subheader("📌 Sawaal 2/5")
        st.write("**Kya aap ne police station mein LIKHIT application di aur RECEIPT li?**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("✅ Di aur receipt li", use_container_width=True):
                st.session_state.answers['Q2'] = 'Di aur receipt li'
                st.session_state.step = 3
                st.rerun()
        with col2:
            if st.button("⚠️ Di lekin receipt nahi li", use_container_width=True):
                st.session_state.answers['Q2'] = 'Di lekin receipt nahi li'
                st.session_state.result = "Pehle police station ja kar receipt lo. Receipt dena police ka farz hai (Section 154 CrPC). Receipt milne ke baad dubara start karein."
                st.session_state.complete = True
                st.rerun()
        with col3:
            if st.button("❌ Nahi di", use_container_width=True):
                st.session_state.answers['Q2'] = 'Nahi di'
                st.session_state.result = "PEHLA STEP: Police station ja kar likhit application do. Application mein date, time, location, incident likho. Receipt zaroor lena. Phir dubara aana."
                st.session_state.complete = True
                st.rerun()
    
    # Step 3
    elif st.session_state.step == 3:
        st.subheader("📌 Sawaal 3/5")
        st.write("**Application diye kitne din ho gaye?**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📅 3 se kam din", use_container_width=True):
                st.session_state.answers['Q3'] = '3 se kam din'
                st.session_state.result = "Police ke paas 3 din ka time hai. Abhi wait karo. Agar 3 din baad bhi action na ho to dubara aana."
                st.session_state.complete = True
                st.rerun()
        with col2:
            if st.button("📅 3 se 7 din", use_container_width=True):
                st.session_state.answers['Q3'] = '3 se 7 din'
                st.session_state.step = 4
                st.rerun()
        with col3:
            if st.button("📅 7 din se zyada", use_container_width=True):
                st.session_state.answers['Q3'] = '7 din se zyada'
                st.session_state.step = 4
                st.rerun()
    
    # Step 4
    elif st.session_state.step == 4:
        st.subheader("📌 Sawaal 4/5")
        st.write("**Police ne kya kiya?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ FIR register kar di", use_container_width=True):
                st.session_state.answers['Q4'] = 'FIR register kar di'
                st.session_state.result = "🎉 Mubarak ho! FIR register ho gayi. Ab apna case number yaad rakho aur police ko follow up karo. Agar investigation mein delay ho to SP se shikayat karo."
                st.session_state.complete = True
                st.rerun()
        with col2:
            if st.button("❌ Kuch nahi kiya / mana kar diya", use_container_width=True):
                st.session_state.answers['Q4'] = 'Kuch nahi kiya'
                st.session_state.step = 5
                st.rerun()
    
    # Step 5
    elif st.session_state.step == 5:
        st.subheader("📌 Sawaal 5/5")
        st.write("**Kya aap ne SP (Superintendent of Police) ko application di hai?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Haan, di hai", use_container_width=True):
                st.session_state.answers['Q5'] = 'Haan, di hai'
                st.session_state.result = "SP ne 15 din mein action lena hai. Agar 15 din baad bhi action na ho to Session Court mein Section 22A/22B CrPC ke tehat petition daal sakte ho.\n\n📞 SP office address: District Police Office, [apne shehar ka naam]"
                st.session_state.complete = True
                st.rerun()
        with col2:
            if st.button("❌ Nahi di", use_container_width=True):
                st.session_state.answers['Q5'] = 'Nahi di'
                st.session_state.result = "📝 ABHI KARO: SP ko likhit application do. SP ke paas 15 din hain action lene ke liye.\n\n📍 Address: District Police Office, [apne shehar ka naam]\n\n💡 Tip: Application ki copy apne paas rakho aur receipt lo."
                st.session_state.complete = True
                st.rerun()

# ============================================
# DOMAIN 2: SALARY DISPUTE
# ============================================
elif st.session_state.domain == "salary" and not st.session_state.complete:
    
    # Step 1
    if st.session_state.step == 1:
        st.subheader("📌 Sawaal 1/6")
        st.write("**Kis type ka masla hai?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💰 Tankhwah pending hai", use_container_width=True):
                st.session_state.answers['Q1'] = 'Tankhwah pending'
                st.session_state.step = 2
                st.rerun()
        with col2:
            if st.button("📄 Termination ka settlement chahiye", use_container_width=True):
                st.session_state.answers['Q1'] = 'Termination settlement'
                st.session_state.step = 3
                st.rerun()
    
    # Step 2 (Salary pending)
    elif st.session_state.step == 2:
        st.subheader("📌 Sawaal 2/6")
        st.write("**Kya aap abhi bhi company mein kaam kar rahe ho?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Haan, kar raha hoon", use_container_width=True):
                st.session_state.answers['Q2'] = 'Haan'
                st.session_state.step = 4
                st.rerun()
        with col2:
            if st.button("❌ Nahi, chod diya / nikal diya", use_container_width=True):
                st.session_state.answers['Q2'] = 'Nahi'
                st.session_state.result = "Company ko full and final settlement dena parega. Pehle HR ko written application do (email behtar hai). 15 din baad agar na milay to Labor Court jao."
                st.session_state.complete = True
                st.rerun()
    
    # Step 3 (Termination)
    elif st.session_state.step == 3:
        st.subheader("📌 Sawaal 3/6")
        st.write("**Company ne termination letter diya?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Haan, diya", use_container_width=True):
                st.session_state.answers['Q3'] = 'Haan'
                st.session_state.step = 4
                st.rerun()
        with col2:
            if st.button("❌ Nahi diya", use_container_width=True):
                st.session_state.answers['Q3'] = 'Nahi'
                st.session_state.result = "Ye unlawful termination hai. Pehle termination letter mango. Agar na dein to Labor Court mein reinstatement (waapas job) maang sakte ho."
                st.session_state.complete = True
                st.rerun()
    
    # Step 4 (HR complaint)
    elif st.session_state.step == 4:
        st.subheader("📌 Sawaal 4/6")
        st.write("**Kya aap ne HR ya manager ko LIKHIT complaint di hai?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Haan, di hai", use_container_width=True):
                st.session_state.answers['Q4'] = 'Haan'
                st.session_state.step = 5
                st.rerun()
        with col2:
            if st.button("❌ Nahi di", use_container_width=True):
                st.session_state.answers['Q4'] = 'Nahi'
                st.session_state.result = "PEHLA STEP: HR ko email karo. CC mein apna personal email rakho (record ke liye). 15 din ka time do. Agar 15 din mein na milay to wapas aao."
                st.session_state.complete = True
                st.rerun()
    
    # Step 5 (15 din)
    elif st.session_state.step == 5:
        st.subheader("📌 Sawaal 5/6")
        st.write("**Complaint diye 15 din ho gaye?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Haan, 15 din ho gaye", use_container_width=True):
                st.session_state.answers['Q5'] = 'Haan'
                st.session_state.step = 6
                st.rerun()
        with col2:
            if st.button("❌ Nahi, 15 din se kam", use_container_width=True):
                st.session_state.answers['Q5'] = 'Nahi'
                st.session_state.result = "Company ko 15 din ka time do law ke mutabiq. Agar 15 din baad bhi na milay to wapas aao."
                st.session_state.complete = True
                st.rerun()
    
    # Step 6 (Amount)
    elif st.session_state.step == 6:
        st.subheader("📌 Sawaal 6/6")
        st.write("**Pending kitni salary hai?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💰 5 lakh se kam", use_container_width=True):
                st.session_state.answers['Q6'] = '5 lakh se kam'
                st.session_state.result = "LABOR COURT JAO:\n\n✅ Fee nahi hai\n✅ Lawyer zaroori nahi (khud bhi kar sakte ho)\n✅ Time: 3-6 months\n\n📍 Labor Court address: [apne shehar ka Labor Court]\n\n📝 Kya aapko application template chahiye?"
                st.session_state.complete = True
                st.rerun()
        with col2:
            if st.button("💰 5 lakh se zyada", use_container_width=True):
                st.session_state.answers['Q6'] = '5 lakh se zyada'
                st.session_state.result = "CIVIL COURT JAO:\n\n⚠️ Advocate zaroori hai (procedure complicated hai)\n✅ Pehle legal notice bhejo\n⏰ Time: 6-12 months\n\n📝 Kya aapko legal notice template chahiye?"
                st.session_state.complete = True
                st.rerun()

# ============================================
# DOMAIN 3: DIVORCE / KHULA
# ============================================
elif st.session_state.domain == "divorce" and not st.session_state.complete:
    
    # Step 1
    if st.session_state.step == 1:
        st.subheader("📌 Sawaal 1/8")
        st.write("**Aap kaun ho?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("👨 Husband (Mard)", use_container_width=True):
                st.session_state.answers['Q1'] = 'Husband'
                st.session_state.step = 2
                st.rerun()
        with col2:
            if st.button("👩 Wife (Aurat)", use_container_width=True):
                st.session_state.answers['Q1'] = 'Wife'
                st.session_state.step = 6
                st.rerun()
    
    # Step 2 (Husband - talaq di?)
    elif st.session_state.step == 2:
        st.subheader("📌 Sawaal 2/8")
        st.write("**Kya aap ne talaq di hai?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Haan, di hai", use_container_width=True):
                st.session_state.answers['Q2'] = 'Haan'
                st.session_state.step = 3
                st.rerun()
        with col2:
            if st.button("❌ Nahi di, soch raha hoon", use_container_width=True):
                st.session_state.answers['Q2'] = 'Nahi'
                st.session_state.result = "Talaq dene se pehle soch lo:\n\n1️⃣ Pehle mediation try karo (family members)\n2️⃣ Agar talaq di to 15 din andar Union Council mein notify karna parega\n3️⃣ Iddat 90 din mein biwi ka kharcha dena parega\n4️⃣ Haq Mehr baqi hai to dena parega"
                st.session_state.complete = True
                st.rerun()
    
    # Step 3 (Union Council notification)
    elif st.session_state.step == 3:
        st.subheader("📌 Sawaal 3/8")
        st.write("**Kya aap ne Union Council mein talaq notify kar di?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Haan, kar di", use_container_width=True):
                st.session_state.answers['Q3'] = 'Haan'
                st.session_state.step = 4
                st.rerun()
        with col2:
            if st.button("❌ Nahi ki", use_container_width=True):
                st.session_state.answers['Q3'] = 'Nahi'
                st.session_state.step = 5
                st.rerun()
    
    # Step 4 (After notification)
    elif st.session_state.step == 4:
        st.subheader("📌 Sawaal 4/8")
        st.write("**Talaq register ho gayi. Ab kya?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⏳ Iddat mein hoon", use_container_width=True):
                st.session_state.answers['Q4'] = 'Iddat mein'
                st.session_state.result = "Iddat 90 din complete karo. Is doran biwi ka kharcha dena parega (khana, rehna, kapra). Agar biwi pregnant hai to delivery tak kharcha dena parega."
                st.session_state.complete = True
                st.rerun()
        with col2:
            if st.button("✅ Iddat complete ho gayi", use_container_width=True):
                st.session_state.answers['Q4'] = 'Iddat complete'
                st.session_state.result = "Talaq final ho gayi. Ab aap dono ka nikah khatam. Haq Mehr agar baqi hai to do. Biwi apni marzi se kahin ja sakti hai."
                st.session_state.complete = True
                st.rerun()
    
    # Step 5 (Notification deadline)
    elif st.session_state.step == 5:
        st.subheader("📌 Sawaal 5/8")
        st.write("**Talaq diye kitne din ho gaye?**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📅 15 din se kam", use_container_width=True):
                st.session_state.answers['Q5'] = '15 din se kam'
                st.session_state.result = "ABHI KARO: Union Council jao. Talaq nama (written) ke saath jao. Chairman Union Council talaq register kare ga. Biwi ko notice bhejega.\n\n📍 Apni Union Council ka address: [area name] Union Council"
                st.session_state.complete = True
                st.rerun()
        with col2:
            if st.button("📅 15-90 din", use_container_width=True):
                st.session_state.answers['Q5'] = '15-90 din'
                st.session_state.result = "DER HO GAYI: Phir bhi Union Council jao. Fine lag sakta hai (1000-5000 Rs). Biwi ko iddat period complete karni paregi."
                st.session_state.complete = True
                st.rerun()
        with col3:
            if st.button("📅 90 din se zyada", use_container_width=True):
                st.session_state.answers['Q5'] = '90 din se zyada'
                st.session_state.result = "Talaq ho chuki hai (iddat complete). Ab aap dono ajnabi ho sakte ho. Dobara shaadi ke liye naya nikah chahiye."
                st.session_state.complete = True
                st.rerun()
    
    # Step 6 (Wife - khula)
    elif st.session_state.step == 6:
        st.subheader("📌 Sawaal 6/8")
        st.write("**Kya husband talaq dene ko tayyar hai?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Haan, tayyar hai", use_container_width=True):
                st.session_state.answers['Q6'] = 'Haan'
                st.session_state.result = "BEST OPTION: Husband khud talaq de de ga. Aap ko kuch nahi karna.\n\n⚠️ Note: Is case mein aap ko Haq Mehr nahi mile ga (khula mein aap ko dena padta)"
                st.session_state.complete = True
                st.rerun()
        with col2:
            if st.button("❌ Nahi, tayyar nahi", use_container_width=True):
                st.session_state.answers['Q6'] = 'Nahi'
                st.session_state.step = 7
                st.rerun()
    
    # Step 7 (Khula)
    elif st.session_state.step == 7:
        st.subheader("📌 Sawaal 7/8")
        st.write("**Kya aap khula (court se talaq) lena chahti ho?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Haan, chahti hoon", use_container_width=True):
                st.session_state.answers['Q7'] = 'Haan'
                st.session_state.step = 8
                st.rerun()
        with col2:
            if st.button("❌ Nahi, mediation try karungi", use_container_width=True):
                st.session_state.answers['Q7'] = 'Nahi'
                st.session_state.result = "Acha hai. Koi family member ya arbitrator dono ko baithaye. Agar husband maan jaye to talaq de de ga. Warna court ka rasta hai."
                st.session_state.complete = True
                st.rerun()
    
    # Step 8 (Khula process)
    elif st.session_state.step == 8:
        st.subheader("📌 Sawaal 8/8")
        st.write("**Kya aap ne Family Court mein khula petition diya hai?**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Haan, diya hai", use_container_width=True):
                st.session_state.answers['Q8'] = 'Haan'
                st.session_state.result = "Court case pending hai. Court ki dates follow karo. Time lag sakta hai (6-9 months). Advocate rakha hai to unsey rabta rakho."
                st.session_state.complete = True
                st.rerun()
        with col2:
            if st.button("❌ Nahi diya", use_container_width=True):
                st.session_state.answers['Q8'] = 'Nahi'
                st.session_state.result = "KHULA KA PROCESS:\n\n1️⃣ Family Court mein petition daalo\n2️⃣ Court pehle mediation karegi\n3️⃣ Agar mediation fail to court khula de gi\n4️⃣ Aap ko husband ko Haq Mehr vapas dena parega\n\n⏰ Time: 3-9 months\n\n📍 Family Court address: [apne shehar ka Family Court]\n\n📝 Kya aapko khula petition template chahiye?"
                st.session_state.complete = True
                st.rerun()

# ============================================
# RESULT SCREEN (Common for all domains)
# ============================================
if st.session_state.complete:
    st.balloons()
    st.success("✅ Aapka masla identify ho gaya!")
    
    st.markdown("---")
    st.markdown("### 📋 Aapke liye hal / solution:")
    st.info(st.session_state.result)
    
    st.markdown("---")
    st.markdown("### 📝 Aapke diye gaye jawab:")
    for q, a in st.session_state.answers.items():
        st.markdown(f"- **{q}:** {a}")
    
    st.markdown("---")
    st.markdown("### 📞 Madad ke liye:")
    st.markdown("""
    - **Legal Aid Helpline:** 1099
    - **Police Complaint:** 15
    - **Women Helpline:** 1099
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Naya masla solve karein", use_container_width=True):
            reset_app()
            st.rerun()
    
    with col2:
        if st.button("ℹ️ Disclaimer", use_container_width=True):
            st.info("Ye tool sirf information ke liye hai. Kisi bhi legal action se pehle licensed lawyer se zaroor rabta karein.")

# Sidebar
with st.sidebar:
    st.markdown("### ⚖️ About This Tool")
    st.markdown("""
    Ye tool aapko batata hai:
    - Kya aapka haq hai?
    - Kahan jana hai?
    - Kya karna hai?
    
    **3 Domains covered:**
    1. Police FIR refusal
    2. Salary disputes
    3. Talaq / Khula
    
    **Note:** Ye kisi lawyer ki jagah nahi le sakta.
    """)
    
    if st.session_state.domain and not st.session_state.complete:
        st.markdown("---")
        st.markdown("### 📍 Progress:")
        st.markdown(f"Domain: **{st.session_state.domain.upper()}**")
        st.markdown(f"Step: **{st.session_state.step}**")
        st.markdown(f"Answers given: **{len(st.session_state.answers)}**")