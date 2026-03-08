#!/usr/bin/env python3
"""
LLM Tuning Studio - Interactive Control Panel
Explore how LLM parameters affect generation behavior.
"""

import os
import gradio as gr
from openai import OpenAI
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
import base64
import json
from config import get_api_key

# Initialize OpenAI client
client = OpenAI(
    api_key=get_api_key(),
)

MODEL_ID = "gpt-4.1-mini"

def generate_response(
    prompt: str,
    temperature: float,
    top_p: float,
    max_tokens: int,
    frequency_penalty: float,
    presence_penalty: float
) -> tuple:
    """Generate response with specified parameters and return both response and settings summary."""
    
    try:
        # Make API call with parameters
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )
        
        generated_text = response.choices[0].message.content
        finish_reason = response.choices[0].finish_reason
        
        # Create settings summary
        settings_summary = f"""Settings Used:
- Temperature: {temperature}
- Top P: {top_p}
- Max Tokens: {max_tokens}
- Frequency Penalty: {frequency_penalty}
- Presence Penalty: {presence_penalty}

Finish Reason: {finish_reason}
"""
        
        return generated_text, settings_summary
        
    except Exception as e:
        return f"Error: {str(e)}", "Error occurred during generation"


def create_token_visualization():
    """Create a simulated token probability visualization."""
    
    # Simulated token probabilities for educational purposes
    tokens = ["Paris", "the", "a", "known", "one", "often", "famous", "located", "beautiful", "called"]
    probabilities = [0.72, 0.12, 0.05, 0.03, 0.02, 0.02, 0.015, 0.01, 0.008, 0.007]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = ['#48bb78' if p > 0.1 else '#667eea' if p > 0.02 else '#a0aec0' for p in probabilities]
    
    bars = ax.barh(tokens[::-1], probabilities[::-1], color=colors[::-1])
    
    ax.set_xlabel('Probability', fontsize=12)
    ax.set_title('Next Token Probability Distribution\nPrompt: "The capital of France is ___"', fontsize=14)
    ax.set_xlim(0, 1)
    
    # Add probability labels
    for bar, prob in zip(bars, probabilities[::-1]):
        ax.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height()/2, 
                f'{prob:.2%}', va='center', fontsize=10)
    
    # Add Top P cutoff line
    ax.axvline(x=0.84, color='#f6ad55', linestyle='--', linewidth=2, label='Top P = 0.84 cutoff')
    ax.legend(loc='lower right')
    
    plt.tight_layout()
    
    # Convert to base64 for display
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    buf.seek(0)
    plt.close()
    
    return buf


def update_visualization(prompt: str, top_p: float, top_k: int):
    """Update the token visualization based on prompt, Top P and Top K settings."""
    
    # Define preset token distributions for different prompts
    preset_distributions = {
        "The capital of France is": {
            "tokens": ["Paris", "the", "a", "known", "one", "often", "famous", "located", "beautiful", "called"],
            "probabilities": [0.72, 0.12, 0.05, 0.03, 0.02, 0.02, 0.015, 0.01, 0.008, 0.007]
        },
        "The weather today is": {
            "tokens": ["sunny", "cloudy", "nice", "beautiful", "cold", "expected", "warm", "going", "looking", "quite"],
            "probabilities": [0.25, 0.20, 0.15, 0.12, 0.08, 0.06, 0.05, 0.04, 0.03, 0.02]
        },
        "The best programming language is": {
            "tokens": ["Python", "subjective", "Java", "JavaScript", "depends", "arguably", "C++", "one", "Go", "Rust"],
            "probabilities": [0.28, 0.18, 0.12, 0.10, 0.09, 0.07, 0.06, 0.04, 0.03, 0.03]
        },
        "Machine learning is": {
            "tokens": ["a", "the", "an", "one", "transforming", "changing", "revolutionizing", "becoming", "used", "being"],
            "probabilities": [0.35, 0.20, 0.12, 0.08, 0.07, 0.05, 0.04, 0.04, 0.03, 0.02]
        }
    }
    
    # Get the appropriate distribution (default to France if prompt not found)
    prompt_clean = prompt.strip()
    if prompt_clean in preset_distributions:
        tokens = preset_distributions[prompt_clean]["tokens"]
        probabilities = preset_distributions[prompt_clean]["probabilities"]
    else:
        # Default distribution
        tokens = preset_distributions["The capital of France is"]["tokens"]
        probabilities = preset_distributions["The capital of France is"]["probabilities"]
        prompt_clean = "The capital of France is"
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Calculate cumulative probability for Top P filtering
    cumulative = 0
    colors = []
    included_count = 0
    for i, p in enumerate(probabilities):
        cumulative += p
        if cumulative <= top_p and i < top_k:
            colors.append('#48bb78')  # Green - included
            included_count += 1
        else:
            colors.append('#e53e3e')  # Red - filtered out
    
    bars = ax.barh(tokens[::-1], probabilities[::-1], color=colors[::-1])
    
    ax.set_xlabel('Probability', fontsize=12)
    ax.set_title(f'Token Filtering: "{prompt_clean} ___"\nTop P = {top_p}, Top K = {top_k} ({included_count} tokens included)', fontsize=14)
    ax.set_xlim(0, 1)
    
    # Add probability labels
    for bar, prob in zip(bars, probabilities[::-1]):
        ax.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height()/2, 
                f'{prob:.2%}', va='center', fontsize=10)
    
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#48bb78', label='Included'),
        Patch(facecolor='#e53e3e', label='Filtered Out')
    ]
    ax.legend(handles=legend_elements, loc='lower right')
    
    plt.tight_layout()
    
    # Save to file for Gradio
    plt.savefig('/tmp/token_viz.png', format='png', dpi=100, bbox_inches='tight')
    plt.close()
    
    return '/tmp/token_viz.png'


def create_comparison(prompt: str, temp_low: float, temp_high: float):
    """Generate side-by-side comparison with different temperatures."""
    
    try:
        # Low temperature response
        response_low = client.chat.completions.create(
            model=MODEL_ID,
            messages=[{"role": "user", "content": prompt}],
            temperature=temp_low,
            max_tokens=100
        )
        text_low = response_low.choices[0].message.content
        
        # High temperature response
        response_high = client.chat.completions.create(
            model=MODEL_ID,
            messages=[{"role": "user", "content": prompt}],
            temperature=temp_high,
            max_tokens=100
        )
        text_high = response_high.choices[0].message.content
        
        return text_low, text_high
        
    except Exception as e:
        return f"Error: {str(e)}", f"Error: {str(e)}"


# Custom CSS - minimal padding, orange theme focus
custom_css = """
/* Full width container with balanced padding */
.gradio-container {
    max-width: 100% !important;
    padding: 40px 170px !important;
}

/* Tab navigation with KodeKloud dark fill */
.tab-nav {
    background: #161b22 !important;
    padding: 8px 16px !important;
    border-radius: 8px 8px 0 0 !important;
    margin-bottom: 0 !important;
    border-bottom: 1px solid #29ddff33 !important;
}

.tab-nav button {
    font-size: 14px !important;
    padding: 10px 20px !important;
    border-radius: 6px !important;
    margin-right: 4px !important;
    color: #94a3b8 !important;
}

.tab-nav button.selected {
    background: linear-gradient(135deg, #29ddff, #1fa2ff) !important;
    color: #0a0e14 !important;
    font-weight: 600 !important;
}

/* Fix label wrapping */
.wrap label span {
    white-space: nowrap !important;
}

/* Group styling */
.group {
    padding: 12px !important;
    margin-bottom: 12px !important;
    border: 1px solid #29ddff22 !important;
    border-radius: 8px !important;
}

/* Slider styling - KodeKloud Teal */
input[type="range"] {
    accent-color: #29ddff !important;
}

/* Headers - KodeKloud Cyan */
h1, h2, h3 {
    color: #29ddff !important;
}

/* Blockquote styling */
blockquote {
    border-left: 4px solid #29ddff !important;
    padding-left: 12px !important;
}

/* Table styling - fix bottom row cutoff */
table {
    border-collapse: collapse !important;
    width: 100% !important;
    margin-bottom: 16px !important;
}

th {
    background: #161b22 !important;
    color: #29ddff !important;
    padding: 10px 12px !important;
    text-align: left !important;
}

td {
    padding: 10px 12px !important;
    border-bottom: 1px solid #29ddff22 !important;
}

tr:last-child td {
    border-bottom: none !important;
}

/* Accordion styling - fix border and background */
.accordion {
    background: #161b22 !important;
    border: 1px solid #29ddff33 !important;
    border-radius: 8px !important;
    margin-bottom: 12px !important;
}

.accordion > .label-wrap {
    background: #1e293b !important;
    border-radius: 8px 8px 0 0 !important;
}

.accordion > .wrap {
    background: #161b22 !important;
    border-top: 1px solid #29ddff22 !important;
}

/* Primary button gradient */
button.primary {
    background: linear-gradient(135deg, #a5fecb, #12d8fa, #1fa2ff) !important;
    color: #0a0e14 !important;
    font-weight: 600 !important;
}

button.primary:hover {
    background: linear-gradient(135deg, #12d8fa, #1fa2ff, #7c3aed) !important;
}
"""

# KodeKloud Brand Theme
kk_theme = gr.themes.Base(
    primary_hue=gr.themes.colors.cyan,
    secondary_hue=gr.themes.colors.purple,
    neutral_hue=gr.themes.colors.slate,
).set(
    # KodeKloud dark backgrounds
    body_background_fill="#0a0e14",
    body_background_fill_dark="#0a0e14",
    background_fill_primary="#161b22",
    background_fill_primary_dark="#161b22",
    background_fill_secondary="#1e293b",
    background_fill_secondary_dark="#1e293b",
    
    # Text colors
    body_text_color="#ffffff",
    body_text_color_dark="#ffffff",
    body_text_color_subdued="#94a3b8",
    body_text_color_subdued_dark="#94a3b8",
    
    # Border colors
    border_color_primary="#29ddff33",
    border_color_primary_dark="#29ddff33",
    
    # Input styling
    input_background_fill="#161b22",
    input_background_fill_dark="#161b22",
    input_border_color="#29ddff33",
    input_border_color_dark="#29ddff33",
    
    # Button colors (KodeKloud Teal/Cyan)
    button_primary_background_fill="#29ddff",
    button_primary_background_fill_dark="#29ddff",
    button_primary_background_fill_hover="#12d8fa",
    button_primary_background_fill_hover_dark="#12d8fa",
    button_primary_text_color="#0a0e14",
    button_primary_text_color_dark="#0a0e14",
    
    # Block styling
    block_background_fill="#161b22",
    block_background_fill_dark="#161b22",
    block_border_color="#29ddff22",
    block_border_color_dark="#29ddff22",
    block_label_background_fill="#1e293b",
    block_label_background_fill_dark="#1e293b",
    block_label_text_color="#29ddff",
    block_label_text_color_dark="#29ddff",
    
    # Slider (KodeKloud Teal)
    slider_color="#29ddff",
    slider_color_dark="#29ddff",
)

# Create the Gradio interface
with gr.Blocks(
    title="LLM Tuning Studio", 
    theme=kk_theme,
    css=custom_css
) as app:
    
    # Header
    gr.Markdown("""
    # LLM Tuning Studio
    
    Explore how different parameters affect LLM generation behavior.
    """)
    
    with gr.Tabs():
        
        # Tab 1: Control Panel
        with gr.TabItem("Control Panel"):
            
            with gr.Row():
                # Left Column - Parameters
                with gr.Column(scale=2):
                    gr.Markdown("### Generation Parameters")
                    
                    with gr.Group():
                        temperature = gr.Slider(
                            minimum=0.0, maximum=2.0, value=0.7, step=0.1,
                            label="Temperature",
                            info="0 = deterministic, 2 = very random"
                        )
                        
                        top_p = gr.Slider(

                            minimum=0.0, maximum=1.0, value=1.0, step=0.05,
                            label="Top P",
                            info="Cumulative probability cutoff (nucleus sampling)"
                        )
                        
                        max_tokens = gr.Slider(
                            minimum=20, maximum=500, value=150, step=10,
                            label="Max Tokens",
                            info="Maximum response length"
                        )
                    
                    gr.Markdown("### Advanced Settings")
                    
                    with gr.Group():
                        frequency_penalty = gr.Slider(
                            minimum=0.0, maximum=2.0, value=0.0, step=0.1,
                            label="Frequency Penalty",
                            info="Penalize frequently used tokens"
                        )
                        
                        presence_penalty = gr.Slider(
                            minimum=0.0, maximum=2.0, value=0.0, step=0.1,
                            label="Presence Penalty",
                            info="Penalize any repeated token"
                        )
                
                # Right Column - Input/Output
                with gr.Column(scale=3):
                    gr.Markdown("### Prompt & Output")
                    
                    prompt_input = gr.Textbox(
                        label="Your Prompt",
                        placeholder="Enter your prompt here...",
                        lines=3,
                        value="Write a short product description for a coffee mug."
                    )
                    
                    generate_btn = gr.Button("Generate", variant="primary", size="lg")
                    
                    output_text = gr.Textbox(
                        label="Generated Output",
                        lines=6
                    )
                    
                    with gr.Accordion("Settings Summary", open=False):
                        settings_display = gr.Textbox(
                            label="",
                            lines=5,
                            show_label=False
                        )
            
            generate_btn.click(
                fn=generate_response,
                inputs=[prompt_input, temperature, top_p, max_tokens, 
                       frequency_penalty, presence_penalty],
                outputs=[output_text, settings_display]
            )

        
        # Tab 2: Temperature Comparison
        with gr.TabItem("Temperature Comparison"):
            gr.Markdown("")
            gr.Markdown("### Compare Temperature Effects")
            gr.Markdown("""
            See how the same prompt produces different outputs at different temperatures.
            
            - **Low temperature** = Consistent, predictable
            - **High temperature** = Creative, varied
            """)
            gr.Markdown("")
            
            compare_prompt = gr.Textbox(
                label="Prompt",
                value="Describe a sunset in one sentence.",
                lines=2
            )
            
            gr.Markdown("")
            
            with gr.Row():
                with gr.Column():
                    temp_low_slider = gr.Slider(
                        0.0, 1.0, value=0.0, step=0.1, 
                        label="Low Temperature Value"
                    )
                with gr.Column():
                    temp_high_slider = gr.Slider(
                        0.0, 2.0, value=1.0, step=0.1, 
                        label="High Temperature Value"
                    )
            
            gr.Markdown("")
            
            compare_btn = gr.Button("Compare Outputs", variant="primary", size="lg")
            
            gr.Markdown("")
            
            with gr.Row():
                with gr.Column():
                    gr.Markdown("#### Low Temperature Output")
                    output_low = gr.Textbox(label="", lines=6, show_label=False)
                    
                with gr.Column():
                    gr.Markdown("#### High Temperature Output")
                    output_high = gr.Textbox(label="", lines=6, show_label=False)
            
            compare_btn.click(
                fn=create_comparison,
                inputs=[compare_prompt, temp_low_slider, temp_high_slider],
                outputs=[output_low, output_high]
            )
        
        # Tab 3: Token Probability Visualization
        with gr.TabItem("Token Visualization"):
            gr.Markdown("")
            gr.Markdown("### Token Filtering Visualization")
            gr.Markdown("""
            This visualization shows how **Top P** and **Top K** filter the token pool.
            
            - **Green bars** = Tokens included in sampling
            - **Red bars** = Tokens filtered out
            
            Select a prompt, adjust the sliders, and click Update to see how different settings affect token selection.
            """)
            gr.Markdown("")
            
            # Prompt selector
            viz_prompt = gr.Dropdown(
                choices=[
                    "The capital of France is",
                    "The weather today is",
                    "The best programming language is",
                    "Machine learning is"
                ],
                value="The capital of France is",
                label="Select Example Prompt",
                info="Choose a prompt to see its token probability distribution"
            )
            
            gr.Markdown("")
            
            with gr.Row():
                with gr.Column():
                    viz_top_p = gr.Slider(
                        0.0, 1.0, value=0.9, step=0.05, 
                        label="Top P Value",
                        info="Cumulative probability cutoff"
                    )
                with gr.Column():
                    viz_top_k = gr.Slider(
                        1, 10, value=10, step=1, 
                        label="Top K Value",
                        info="Maximum number of tokens to consider"
                    )
            
            gr.Markdown("")
            
            update_viz_btn = gr.Button("Update Visualization", variant="primary", size="lg")
            
            gr.Markdown("")
            
            viz_image = gr.Image(label="", type="filepath", show_label=False)
            
            gr.Markdown("""
            > **Note:** This is a simulated visualization for educational purposes.
            > Token probabilities are representative examples to demonstrate filtering concepts.
            
            **Try This:**
            - Select "The weather today is" and set Top P = 0.5 to see how varied weather words get filtered
            - Select "The best programming language is" and compare Top P = 0.3 vs 0.9
            """)
            
            update_viz_btn.click(
                fn=update_visualization,
                inputs=[viz_prompt, viz_top_p, viz_top_k],
                outputs=[viz_image]
            )
        
        # Tab 4: Production Scenarios
        with gr.TabItem("Production Scenarios"):
            gr.Markdown("")
            gr.Markdown("### Production Configuration Examples")
            gr.Markdown("Different use cases require different parameter configurations.")
            gr.Markdown("")
            
            with gr.Accordion("Drive-Thru Ordering Agent", open=True):
                gr.Markdown("""
                **Goal:** Consistent, menu-focused responses
                
                | Parameter | Value | Reason |
                |-----------|-------|--------|
                | Temperature | 0 | Deterministic responses |
                | Top P | 0.3 | Narrow vocabulary |
                | Frequency Penalty | 0 | Repetition is OK |
                | Presence Penalty | 0 | Consistency over variety |
                
                **Try this prompt:** `You are a Taco Bell drive-thru agent. A customer asks: What comes in a Crunchy Taco?`
                """)
            
            gr.Markdown("")
            
            with gr.Accordion("Creative Story Writer", open=True):
                gr.Markdown("""
                **Goal:** Varied, imaginative outputs
                
                | Parameter | Value | Reason |
                |-----------|-------|--------|
                | Temperature | 0.9 | High creativity |
                | Top P | 0.95 | Wide vocabulary |
                | Frequency Penalty | 0.8 | Avoid word repetition |
                | Presence Penalty | 0.6 | Encourage new topics |
                
                **Try this prompt:** `Write a short story about a robot who discovers music for the first time.`
                """)
            
            gr.Markdown("")
            
            with gr.Accordion("Code Documentation Generator", open=False):
                gr.Markdown("""
                **Goal:** Accurate, consistent, technical
                
                | Parameter | Value | Reason |
                |-----------|-------|--------|
                | Temperature | 0.2 | Mostly deterministic |
                | Top P | 0.8 | Standard vocabulary |
                | Frequency Penalty | 0.3 | Some variety OK |
                | Presence Penalty | 0.1 | Technical consistency |
                
                **Try this prompt:** `Write a docstring for a Python function called calculate_average that takes a list of numbers and returns the mean.`
                """)
            
            gr.Markdown("")
            gr.Markdown("""
            > **Key Insight:** There is no universal "best" setting. 
            > Configuration depends entirely on your specific use case.
            """)
    
    gr.Markdown("")
    gr.Markdown("---")
    gr.Markdown("**LLM Tuning Studio** - Learn how LLM parameters affect generation behavior")


if __name__ == "__main__":
    # Create marker when app launches
    os.makedirs("markers", exist_ok=True)
    with open("markers/app_launched.txt", "w") as f:
        f.write("APP_LAUNCHED")
    
    print("Starting LLM Tuning Studio...")
    print("Access the UI via the 'Gradio UI' button (top-right of lab)")
    
    app.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )

