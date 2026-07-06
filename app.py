import streamlit as st
import time

# --- CONFIGURATION & AESTHETIC ---
st.set_page_config(page_title="A.E.G.I.S. // Command Terminal", layout="wide")

st.markdown("""
<style>
    /* Cyberpunk Terminal Aesthetic */
    .stApp { background-color: #000000; color: #00FF41; font-family: 'JetBrains Mono', monospace; }
    h1, h2, h3 { color: #00FF41; text-shadow: 0 0 5px #00FF41; }
    div[data-testid="stMetricValue"] { color: #00FF41; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("PRIME AXIS")
st.subheader("Autonomous Energy & Governance Industrial System")

# --- TELEMETRY DASHBOARD ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Nexus-Flow Thermal", value="45.2°C", delta="-1.2°C")
with col2:
    st.metric(label="T.A.L.O.N. Arbitrage Index", value="0.94", delta="0.02")
with col3:
    st.metric(label="System Latency", value="0.42ms", delta="0.01ms")

# --- CONTROL LAYER ---
st.markdown("---")
st.write("### [ SOVEREIGN AGENT LOG ]")

if st.button("INITIATE AGENT SWARM"):
    with st.spinner('Orchestrating...'):
        time.sleep(1) # Simulate Latency
        st.success("Sovereign Loop Engaged: T.A.L.O.N. stabilizing grid.")
        st.code("""
        [0.00ms] Sentinel: Routing to Nexus-Flow.
        [0.15ms] Archivist: State validated.
        [0.32ms] Operator: Arbitrage threshold met.
        [0.42ms] STATUS: Sovereign Equilibrium Reached.
        """, language='text')

# --- SIDEBAR: SYSTEM STATUS ---
with st.sidebar:
    st.header("CORE MONITOR")
    st.info("System: OPERATIONAL")
    st.warning("Nexus-Flow: LIQUID COOLING NOMINAL")
    st.success("T.A.L.O.N.: GRID ARBITRAGE ACTIVE")
