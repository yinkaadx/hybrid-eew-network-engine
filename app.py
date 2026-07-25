import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time

st.set_page_config(page_title="Hybrid EEW Network Engine", layout="wide")

st.title("Serverless Hybrid Earthquake Early Warning Pipeline")
st.caption("Real-Time Edge-Cloud Orchestration: MEMS Decentralized Array & Observatory-Grade Data Fusion")

st.sidebar.header("Geohazard Configuration")
selected_fault = st.sidebar.selectbox("Simulated Tectonic Origin", ["Hikurangi Subduction Zone", "Alpine Fault Transpressional", "Wellington Fault Line"])
seismic_magnitude = st.sidebar.slider("Simulate Earthquake Magnitude (Mw)", 4.0, 8.5, 7.2)
run_simulation = st.sidebar.button("Initialize Hybrid EEW System")

st.sidebar.markdown("---")
st.sidebar.caption("Architecture: MEMS Edge Processing -> Observatory Data Fusion -> Alert API")

if run_simulation:
    st.subheader(f"Active Seismic Monitoring: {selected_fault}")
    
    col1, col2, col3, col4 = st.columns(4)
    metric_mems = col1.empty()
    metric_obs = col2.empty()
    metric_latency = col3.empty()
    metric_status = col4.empty()

    chart_placeholder = st.empty()
    log_placeholder = st.empty()

    np.random.seed(1122)
    time_steps = pd.date_range(start=pd.Timestamp.now(), periods=100, freq="s")
    
    mems_amplitude = []
    obs_amplitude = []
    
    base_noise = 0.5 
    
    for i in range(100):
        if i < 35:
            current_mems = base_noise + np.random.uniform(-0.3, 0.3)
            current_obs = base_noise + np.random.uniform(-0.1, 0.1)
            latency = np.random.uniform(50.0, 100.0)
            status = "BACKGROUND NOISE"
        elif i >= 35 and i < 45:
            current_mems = base_noise + (i - 35) * (seismic_magnitude * 1.5) + np.random.uniform(-2.0, 2.0)
            current_obs = base_noise + (i - 35) * (seismic_magnitude * 1.2) + np.random.uniform(-0.5, 0.5)
            latency = np.random.uniform(10.0, 25.0) 
            status = "P-WAVE DETECTED AT EDGE"
        else:
            current_mems = max(base_noise, current_mems - np.random.uniform(1.0, 5.0))
            current_obs = max(base_noise, current_obs - np.random.uniform(0.5, 3.0))
            latency = np.random.uniform(15.0, 30.0)
            status = "S-WAVE PROPAGATING"
            
        mems_amplitude.append(current_mems)
        obs_amplitude.append(current_obs)
        
        metric_mems.metric("MEMS Edge Array (Amplitude)", f"{current_mems:.2f} m/s²", "High Density")
        metric_obs.metric("Observatory Sensor (Amplitude)", f"{current_obs:.2f} m/s²", "High Fidelity")
        metric_latency.metric("System Alert Latency", f"{latency:.1f} ms", "- Edge Optimized")
        
        if status == "P-WAVE DETECTED AT EDGE":
            metric_status.metric("EEW Network Status", status, "Triggering Alert")
        elif status == "S-WAVE PROPAGATING":
            metric_status.metric("EEW Network Status", status, "Alert Issued")
        else:
            metric_status.metric("EEW Network Status", status, "Stable")
            
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=mems_amplitude, mode='lines', name='MEMS Sensor Array (Decentralized)', line=dict(color='orange')))
        fig.add_trace(go.Scatter(x=time_steps[:i+1], y=obs_amplitude, mode='lines', name='Observatory Grade Sensor (National)', yaxis='y2', line=dict(color='blue', dash='dot')))
        
        fig.update_layout(
            title=f"Hybrid Instrument Network: Mw {seismic_magnitude} Earthquake Detection & Data Fusion",
            xaxis=dict(title="High-Frequency Signal Timeline"),
            yaxis=dict(title="MEMS Acceleration (m/s²)", range=[0, max(20, max(mems_amplitude)+5)]),
            yaxis2=dict(title="Observatory Acceleration", overlaying='y', side='right', range=[0, max(20, max(obs_amplitude)+5)]),
            height=400,
            margin=dict(l=0, r=0, t=40, b=0)
        )
        
        chart_placeholder.plotly_chart(fig, use_container_width=True)
        
        if status == "P-WAVE DETECTED AT EDGE" and i == 35:
            log_placeholder.error(f"SEISMIC ALERT: P-Wave arrival detected by MEMS Edge Computing node at {time_steps[i].strftime('%H:%M:%S')}. Initiating immediate asynchronous data fusion with Observatory network to verify magnitude.")
        elif status == "S-WAVE PROPAGATING" and i == 45:
            log_placeholder.warning(f"EEW SUCCESS: Serverless API gateway issued regional protective alerts {latency:.1f}ms after P-wave validation. S-wave damage mitigated.")
        elif status == "BACKGROUND NOISE" and i % 5 == 0:
            log_placeholder.success(f"Log: Telemetry tick {i} processed. Edge nodes actively filtering anthropogenic noise from decentralized MEMS array.")
            
        time.sleep(0.15)
        
    st.info("Simulation Complete. The hybrid edge-cloud architecture successfully integrated MEMS and observatory-grade data, minimizing alert latency for next-generation Earthquake Early Warning.")
else:
    st.info("Click 'Initialize Hybrid EEW System' in the sidebar to simulate high-velocity seismic data fusion.")