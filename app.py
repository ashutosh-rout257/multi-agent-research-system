import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="ResearchHub · AI Research",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling with Dark Theme, Orange Run Button, and Uniform Blue Preset Buttons
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');

    /* Global Dark Theme Settings */
    .stApp {
        background-color: #0E0F12;
        color: #E2E8F0;
        font-family: 'Inter', sans-serif;
    }

    #MainMenu, footer, header {visibility: hidden;}

    /* Centered Hero Section */
    .hero-container {
        text-align: center;
        padding-top: 1rem;
        padding-bottom: 2rem;
    }

    .sub-tag {
        color: #FF6B35;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.25em;
        text-transform: uppercase;
        margin-bottom: 0.6rem;
    }

    .main-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 3.8rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 0.8rem;
        letter-spacing: -0.02em;
    }

    .hero-description {
        color: #94A3B8;
        font-size: 1.05rem;
        max-width: 680px;
        margin: 0 auto;
        line-height: 1.6;
    }

    /* Input Field Label */
    .input-label {
        color: #FF6B35;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    /* Custom Streamlit Input */
    .stTextInput > div > div > input {
        background-color: #16181E !important;
        color: #FFFFFF !important;
        border: 1px solid #262932 !important;
        border-radius: 12px !important;
        padding: 14px 18px !important;
        font-size: 1rem !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 2px rgba(59, 130, 246, 0.2) !important;
    }

    /* Primary Action Button (Orange Gradient) */
    .stButton > button {
        background: linear-gradient(90deg, #FF9F29 0%, #FF6B35 100%) !important;
        color: #0E0F12 !important;
        font-weight: 700 !important;
        font-family: 'Space Grotesk', sans-serif !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 24px !important;
        font-size: 1.05rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 107, 53, 0.4) !important;
    }

    /* Uniform Single-Color Suggested Topic Buttons (Electric Blue) */
    div.row-widget.stHorizontal div.stButton > button {
        background-color: #1E293B !important;
        color: #38BDF8 !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
        font-size: 0.85rem !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        padding: 8px 12px !important;
        box-shadow: none !important;
        transition: all 0.2s ease !important;
    }

    div.row-widget.stHorizontal div.stButton > button:hover {
        background-color: #0284C7 !important;
        color: #FFFFFF !important;
        border-color: #38BDF8 !important;
        transform: translateY(-1px);
    }

    /* Try Preset Tags Label */
    .try-tag {
        color: #64748B;
        font-size: 0.75rem;
        font-weight: 600;
        margin-top: 1.2rem;
        margin-bottom: 0.4rem;
        letter-spacing: 0.05em;
    }

    /* Pipeline Status Header */
    .pipeline-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 1.6rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 1.2rem;
    }

    /* Footer */
    .footer-text {
        text-align: center;
        color: #475569;
        font-size: 0.8rem;
        margin-top: 4rem;
        padding-bottom: 2rem;
        letter-spacing: 0.05em;
    }
</style>
""", unsafe_allow_html=True)

# Try importing backend agents (falls back safely if running standalone UI)
try:
    from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain
    HAS_BACKEND = True
except ImportError:
    HAS_BACKEND = False

# Hero Banner
st.markdown("""
<div class="hero-container">
    <div class="sub-tag">MULTI-AGENT AI SYSTEM</div>
    <div class="main-title">ResearchHub</div>
    <div class="hero-description">
        Four specialized AI agents collaborate — searching, scraping, writing, and critiquing — to deliver a polished research report on any topic.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Main Two-Column Layout
col1, col2 = st.columns([1.1, 0.9], gap="large")

with col1:
    st.markdown('<div class="input-label">RESEARCH TOPIC</div>', unsafe_allow_html=True)
    
    # Session state for topic input (empty by default)
    if "topic_input" not in st.session_state:
        st.session_state["topic_input"] = ""

    user_topic = st.text_input(
        label="topic_label", 
        value=st.session_state["topic_input"], 
        label_visibility="collapsed",
        placeholder="e.g. Quantum computing breakthroughs in 2025"
    )

    run_btn = st.button("⚡ Run Research Pipeline", use_container_width=True)

    st.markdown('<div class="try-tag">TRY →</div>', unsafe_allow_html=True)
    
    btn_col1, btn_col2, btn_col3 = st.columns(3)
    with btn_col1:
        if st.button("LLM agents 2025", key="p1", use_container_width=True):
            st.session_state["topic_input"] = "LLM agents 2025"
            st.rerun()
    with btn_col2:
        if st.button("CRISPR gene editing", key="p2", use_container_width=True):
            st.session_state["topic_input"] = "CRISPR gene editing"
            st.rerun()
    with btn_col3:
        if st.button("Fusion energy progress", key="p3", use_container_width=True):
            st.session_state["topic_input"] = "Fusion energy progress"
            st.rerun()

# Dynamic Pipeline Status Setup
if "agent_status" not in st.session_state:
    st.session_state["agent_status"] = {
        "01": "WAITING",
        "02": "WAITING",
        "03": "WAITING",
        "04": "WAITING"
    }

if "results" not in st.session_state:
    st.session_state["results"] = None

def render_pipeline():
    statuses = st.session_state["agent_status"]
    
    def get_badge(status):
        if status == "RUNNING":
            return '<span style="color: #FF9F29; font-weight:700; font-size:0.75rem; letter-spacing:0.1em;">RUNNING...</span>'
        elif status == "COMPLETED":
            return '<span style="color: #10B981; font-weight:700; font-size:0.75rem; letter-spacing:0.1em;">✓ DONE</span>'
        return '<span style="color: #64748B; font-weight:700; font-size:0.75rem; letter-spacing:0.1em;">WAITING</span>'

    def get_border(status):
        if status == "RUNNING":
            return "1px solid #FF6B35"
        elif status == "COMPLETED":
            return "1px solid #10B981"
        return "1px solid #262932"

    st.markdown(f"""
    <div style="background-color: #16181E; border: {get_border(statuses['01'])}; border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div style="color: #FFFFFF; font-weight: 600; font-size: 1rem;"><span style="color: #FF6B35; font-weight: 700; margin-right: 8px;">01</span> Search Agent</div>
            <div style="color: #64748B; font-size: 0.85rem; margin-top: 4px;">Gathers recent web information</div>
        </div>
        <div>{get_badge(statuses['01'])}</div>
    </div>

    <div style="background-color: #16181E; border: {get_border(statuses['02'])}; border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div style="color: #FFFFFF; font-weight: 600; font-size: 1rem;"><span style="color: #FF6B35; font-weight: 700; margin-right: 8px;">02</span> Reader Agent</div>
            <div style="color: #64748B; font-size: 0.85rem; margin-top: 4px;">Scrapes & extracts deep content</div>
        </div>
        <div>{get_badge(statuses['02'])}</div>
    </div>

    <div style="background-color: #16181E; border: {get_border(statuses['03'])}; border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div style="color: #FFFFFF; font-weight: 600; font-size: 1rem;"><span style="color: #FF6B35; font-weight: 700; margin-right: 8px;">03</span> Writer Chain</div>
            <div style="color: #64748B; font-size: 0.85rem; margin-top: 4px;">Drafts the full research report</div>
        </div>
        <div>{get_badge(statuses['03'])}</div>
    </div>

    <div style="background-color: #16181E; border: {get_border(statuses['04'])}; border-radius: 12px; padding: 16px 20px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div style="color: #FFFFFF; font-weight: 600; font-size: 1rem;"><span style="color: #FF6B35; font-weight: 700; margin-right: 8px;">04</span> Critic Chain</div>
            <div style="color: #64748B; font-size: 0.85rem; margin-top: 4px;">Reviews & scores the report</div>
        </div>
        <div>{get_badge(statuses['04'])}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="pipeline-title">Pipeline</div>', unsafe_allow_html=True)
    pipeline_placeholder = st.empty()
    with pipeline_placeholder.container():
        render_pipeline()

# Pipeline Execution Logic
if run_btn:
    topic_to_run = user_topic if user_topic.strip() else st.session_state["topic_input"]
    if not topic_to_run.strip():
        st.warning("Please enter or select a research topic.")
    else:
        state = {}
        
        # Step 1: Search Agent
        st.session_state["agent_status"]["01"] = "RUNNING"
        with pipeline_placeholder.container():
            render_pipeline()
        
        if HAS_BACKEND:
            search_agent = build_search_agent()
            search_result = search_agent.invoke({
                "messages": [("user", f"Find 3 to 5 recent, reliable, and detailed web sources about: {topic_to_run}")]
            })
            state["search_results"] = search_result['messages'][-1].content
        else:
            state["search_results"] = f"Sample search results for {topic_to_run}."

        st.session_state["agent_status"]["01"] = "COMPLETED"
        st.session_state["agent_status"]["02"] = "RUNNING"
        with pipeline_placeholder.container():
            render_pipeline()

        # Step 2: Reader Agent
        if HAS_BACKEND:
            reader_agent = build_reader_agent()
            reader_result = reader_agent.invoke({
                "messages": [("user",
                    f"Based on the following search results about '{topic_to_run}', "
                    f"pick the most relevant URL and scrape it for deeper content.\n\n"
                    f"Search Results:\n{state['search_results']}"
                )]
            })
            state['scraped_content'] = reader_result['messages'][-1].content
        else:
            state['scraped_content'] = f"Sample scraped content for {topic_to_run}."

        st.session_state["agent_status"]["02"] = "COMPLETED"
        st.session_state["agent_status"]["03"] = "RUNNING"
        with pipeline_placeholder.container():
            render_pipeline()

        # Step 3: Writer Chain
        if HAS_BACKEND:
            research_combined = (
                f"SEARCH RESULTS AND URLS:\n{state['search_results']}\n\n"
                f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
            )
            state["report"] = writer_chain.invoke({
                "topic": topic_to_run,
                "research": research_combined
            })
        else:
            state["report"] = f"# Research Report: {topic_to_run}\n\nSample research report."

        st.session_state["agent_status"]["03"] = "COMPLETED"
        st.session_state["agent_status"]["04"] = "RUNNING"
        with pipeline_placeholder.container():
            render_pipeline()

        # Step 4: Critic Chain
        if HAS_BACKEND:
            state["feedback"] = critic_chain.invoke({
                "report": state['report']
            })
        else:
            state["feedback"] = "Score: 8/10\n\nStrengths:\n- Detailed breakdown\n- Clear insights\n\nAreas to Improve:\n- Add more metrics\n\nOne line verdict:\nSolid report."

        st.session_state["agent_status"]["04"] = "COMPLETED"
        with pipeline_placeholder.container():
            render_pipeline()

        st.session_state["results"] = state

# Display Output Results Section
if st.session_state.get("results"):
    res = st.session_state["results"]
    st.markdown("<br><hr style='border-color:#262932;'><br>", unsafe_allow_html=True)
    
    st.markdown('<div class="pipeline-title">Results</div>', unsafe_allow_html=True)

    # Search Results in plain text container (no JSON)
    with st.expander("🔍 Search Results (raw)", expanded=False):
        st.text_area(
            "Search Results Output",
            value=str(res["search_results"]),
            height=200,
            disabled=True,
            label_visibility="collapsed"
        )

    # Scraped Content in plain text container (no JSON)
    with st.expander("🌐 Scraped Content (raw)", expanded=False):
        st.text_area(
            "Scraped Content Output",
            value=str(res["scraped_content"]),
            height=200,
            disabled=True,
            label_visibility="collapsed"
        )

    # Final Report Output (includes 3-5 clickable markdown links under Sources)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="font-family: \'Space Grotesk\', sans-serif; font-size: 1.4rem; font-weight: 700; color: #FFFFFF; margin-bottom: 1rem;">📄 FINAL RESEARCH REPORT</div>', unsafe_allow_html=True)
    
    st.markdown(res["report"])
    
    # Critic Feedback Section (Dark card with yellow lightning icon)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="display: flex; align-items: center; margin-bottom: 1rem;"><span style="color: #FFB020; font-size: 1.2rem; margin-right: 8px;">⚡</span><span style="font-family: \'Space Grotesk\', sans-serif; font-size: 1.4rem; font-weight: 700; color: #FFFFFF; letter-spacing: 0.05em;">CRITIC FEEDBACK</span></div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background-color: #16181E; border: 1px solid #262932; border-radius: 12px; padding: 20px; color: #E2E8F0; font-family: 'Inter', sans-serif; line-height: 1.6;">
        {str(res["feedback"]).replace('\n', '<br>')}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.download_button(
        label="📥 Download Report (.md)",
        data=str(res["report"]),
        file_name="research_report.md",
        mime="text/markdown"
    )

# Footer
st.markdown("""
<div class="footer-text">
    ResearchHub · Powered by LangChain multi-agent pipeline · Built with Streamlit
</div>
""", unsafe_allow_html=True)