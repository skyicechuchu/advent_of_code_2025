import streamlit as st
import os
import importlib.util
import sys

st.set_page_config(
    page_title="AoC 2025 - AI Pair Programming",
    page_icon="🎄",
    layout="wide"
)

# Custom CSS for "fancy" look
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #262730;
    }
    h1 {
        background: -webkit-linear-gradient(45deg, #00FF00, #00FFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

def load_day_module(day_num):
    day_dir = f"day{day_num}"
    script_path = os.path.join(day_dir, f"day{day_num}.py")
    input_path = os.path.join(day_dir, f"day{day_num}_input.txt")
    
    if not os.path.exists(script_path):
        return None, None, None

    spec = importlib.util.spec_from_file_location(f"day{day_num}", script_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[f"day{day_num}"] = module
    spec.loader.exec_module(module)
    
    input_text = ""
    if os.path.exists(input_path):
        with open(input_path, 'r') as f:
            input_text = f.read()
            
    return module, input_text, script_path

# Sidebar
st.sidebar.title("🎄 Advent of Code 2025")
st.sidebar.markdown("### BroProgramming")

# Get available days
days = []
for item in os.listdir('.'):
    if item.startswith('day') and os.path.isdir(item):
        try:
            days.append(int(item[3:]))
        except ValueError:
            continue
days = sorted(days)

selected_day = st.sidebar.selectbox("Select Day", days, index=len(days)-1 if days else 0)

# Main Content
st.title(f"Day {selected_day} Solution")

module, input_text, script_path = load_day_module(selected_day)

if module:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📝 Input Data")
        with st.expander("View Input File", expanded=False):
            st.code(input_text[:1000] + ("..." if len(input_text) > 1000 else ""))
            st.caption(f"Total lines: {len(input_text.splitlines())}")

        st.subheader("🚀 Execution")
        if st.button("Run Solution"):
            with st.spinner("Processing..."):
                try:
                    p1 = module.solve_part1(input_text)
                    st.success(f"**Part 1 Result:** {p1}")
                except Exception as e:
                    st.error(f"Part 1 Error: {e}")
                
                try:
                    if hasattr(module, 'solve_part2'):
                        p2 = module.solve_part2(input_text)
                        st.info(f"**Part 2 Result:** {p2}")
                except Exception as e:
                    st.error(f"Part 2 Error: {e}")

    with col2:
        st.subheader("💻 Source Code")
        with open(script_path, 'r') as f:
            code = f.read()
        st.code(code, language='python')

    # AI Analysis Section (Static for now, but structures the app)
    st.markdown("---")
    st.subheader("🤖 AI Analysis & Visualization")
    
    # Check for visual assets
    asset_types = {
        'png': 'image',
        'jpg': 'image', 
        'gif': 'image',
        'mp4': 'video'
    }
    
    found_asset = False
    for ext, type_ in asset_types.items():
        asset_path = f"assets/day{selected_day}_visual.{ext}"
        if os.path.exists(asset_path):
            if type_ == 'image':
                st.image(asset_path, caption=f"Day {selected_day} Visualization")
            elif type_ == 'video':
                st.video(asset_path)
            found_asset = True
            break
            
    if not found_asset:
        st.info("No visualization available for this day yet. Add images to the 'assets' folder!")

    analyses = {
        1: "Uses basic arithmetic modulo operations to track circular movement.",
        2: "Implements string parsing for ranges and pattern matching for ID validation.",
        3: "Uses a Greedy Monotonic Stack approach to solve the optimization problem in O(n) time.",
        4: "Simulates grid neighbor states iteratively until convergence.",
        5: "Solves range intersection using Interval Merging (O(N log N)) instead of brute force.",
        6: "Utilizes NumPy for efficient matrix transposition to switch between reading directions."
    }
    
    st.info(analyses.get(selected_day, "Analysis not available for this day."))

else:
    st.error("Module not found!")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Developed with ❤️ by Human & AI")

