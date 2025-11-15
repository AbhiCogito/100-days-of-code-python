import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import textwrap
from visuals import WorkoutCharts, ProgressCharts
from llm_summary import llm_response

wc = WorkoutCharts()
pc = ProgressCharts()

# Fetching charts individually from all the functions
vol_per_exercise_fig = wc.vol_per_exercise_chart()
# vol_per_title_fig = wc.vol_per_title_chart()
avg_wt_per_rep_per_ex_fig = wc.avg_wt_per_rep_per_ex_chart()
total_wt_per_day_fig = wc.total_wt_per_day_chart()
total_wt_per_week_fig = wc.total_wt_per_week_chart()
total_wt_per_month_fig = wc.total_wt_per_month_chart()
avg_workout_duration_fig = wc.avg_workout_duration_chart()
top_day_week_fig = wc.top_day_in_week_chart()
top_day_month_fig = wc.top_day_in_month_chart()
top_day_year_fig = wc.top_day_in_year_chart()
top_week_month_fig = wc.top_week_in_month_chart()
top_month_year_fig = wc.top_month_in_year_chart()
ex_monthly_variety_fig = pc.exercise_monthly_variety_chart()

# Function to clean LLM response
def clean_llm_response(text):
    """Remove <think> tags and clean up the response"""
    # Remove <think> and </think> tags and content between them
    import re
    cleaned = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    # Remove any extra whitespace
    cleaned = cleaned.strip()
    return cleaned

# Function to parse and format markdown-style text
def parse_formatted_text(text):
    """Parse text with markdown-style formatting and return structured data"""
    import re
    
    lines = text.split('\n')
    formatted_blocks = []
    
    for line in lines:
        line = line.strip()
        if not line:
            formatted_blocks.append({'type': 'blank', 'text': ''})
        elif line.startswith('###'):
            # Main heading (H3)
            clean_text = line.replace('###', '').strip().strip('*').strip()
            formatted_blocks.append({'type': 'h3', 'text': clean_text})
        elif line.startswith('####'):
            # Subheading (H4)
            clean_text = line.replace('####', '').strip().strip('*').strip()
            formatted_blocks.append({'type': 'h4', 'text': clean_text})
        elif line.startswith('#'):
            # Alternative heading format
            clean_text = line.replace('#', '').strip().strip('*').strip()
            formatted_blocks.append({'type': 'h3', 'text': clean_text})
        elif line.startswith('-') or line.startswith('•'):
            # Bullet point - remove asterisks from content
            bullet_text = line[1:].strip()
            bullet_text = re.sub(r'\*\*([^*]+)\*\*', r'\1', bullet_text)  # Remove ** bold markers
            formatted_blocks.append({'type': 'bullet', 'text': bullet_text, 'has_bold': '**' in line})
        elif line.startswith('```'):
            # Code block marker (skip)
            continue
        elif line.startswith('--'):
            # Horizontal line (skip)
            formatted_blocks.append({'type': 'separator', 'text': ''})
        else:
            # Regular text - check if it has bold markers
            has_bold = '**' in line
            # Extract bold and regular text
            clean_text = re.sub(r'\*\*([^*]+)\*\*', r'\1', line)  # Remove ** markers but keep text
            formatted_blocks.append({'type': 'text', 'text': clean_text, 'has_bold': has_bold, 'original': line})
    
    return formatted_blocks

# Function to create LLM summary pages (can span multiple pages)
def create_summary_pages():
    """Create figure(s) with the LLM summary text with proper formatting"""
    
    # Clean the LLM response
    cleaned_response = clean_llm_response(llm_response)
    
    # Parse formatted text
    formatted_blocks = parse_formatted_text(cleaned_response)
    
    figures = []
    current_y = 0.90  # Starting Y position
    page_num = 1
    
    # Create first page
    fig, ax = plt.subplots(figsize=(8.5, 11))
    ax.axis('off')
    
    # Add title on first page
    title_text = "🏋️‍♂️ AI-Powered Workout Insights"
    ax.text(0.5, 0.97, title_text, 
            ha='center', va='top', 
            fontsize=20, fontweight='bold',
            color='#2E86AB',
            transform=ax.transAxes)
    
    # Add date
    date_text = f"Generated on: {datetime.now().strftime('%B %d, %Y')}"
    ax.text(0.5, 0.94, date_text,
            ha='center', va='top',
            fontsize=9, style='italic', color='gray',
            transform=ax.transAxes)
    
    # Add horizontal line
    ax.plot([0.08, 0.92], [0.925, 0.925], 'k-', linewidth=2, transform=ax.transAxes)
    
    line_height = 0.022  # Increased height per line to prevent overlap
    margin_left = 0.08
    
    for block in formatted_blocks:
        block_type = block['type']
        text = block['text']
        
        # Check if we need a new page (with more conservative margin)
        if current_y < 0.10:
            figures.append(fig)
            page_num += 1
            
            # Create new page
            fig, ax = plt.subplots(figsize=(8.5, 11))
            ax.axis('off')
            current_y = 0.95
        
        if block_type == 'blank':
            current_y -= line_height * 0.5
            
        elif block_type == 'separator':
            current_y -= line_height * 0.3
            
        elif block_type == 'h3':
            # Main heading - large, bold, colored with extra spacing
            current_y -= line_height * 0.8
            ax.text(margin_left, current_y, text,
                    ha='left', va='top',
                    fontsize=12, fontweight='bold',
                    color='#A23B72',
                    transform=ax.transAxes)
            current_y -= line_height * 1.8  # Extra space after heading
            
        elif block_type == 'h4':
            # Subheading - medium, bold, different color with spacing
            current_y -= line_height * 0.6
            ax.text(margin_left, current_y, text,
                    ha='left', va='top',
                    fontsize=10.5, fontweight='bold',
                    color='#F18F01',
                    transform=ax.transAxes)
            current_y -= line_height * 1.3  # Space after subheading
            
        elif block_type == 'bold':
            # Bold text block
            wrapped_lines = textwrap.fill(text, width=90).split('\n')
            for line in wrapped_lines:
                ax.text(margin_left, current_y, line,
                        ha='left', va='top',
                        fontsize=9.5, fontweight='bold',
                        color='#333333',
                        transform=ax.transAxes)
                current_y -= line_height
            current_y -= line_height * 0.3
            
        elif block_type == 'bullet':
            # Bullet point with bold text handling
            import re
            original_text = block.get('original', text)
            wrapped_lines = textwrap.fill(text, width=85).split('\n')
            
            for idx, line in enumerate(wrapped_lines):
                prefix = '  • ' if idx == 0 else '    '
                
                # Check if this line has bold segments in original
                if '**' in original_text:
                    # Mixed bold - handle carefully
                    ax.text(margin_left + 0.02, current_y, prefix + line,
                            ha='left', va='top',
                            fontsize=9,
                            color='#333333',
                            transform=ax.transAxes)
                else:
                    ax.text(margin_left + 0.02, current_y, prefix + line,
                            ha='left', va='top',
                            fontsize=9,
                            color='#333333',
                            transform=ax.transAxes)
                current_y -= line_height
            
        elif block_type == 'text':
            # Regular text with potential bold segments
            if text:
                import re
                original = block.get('original', text)
                
                # Check if has bold markers
                if '**' in original:
                    # Split by bold markers and render appropriately
                    # For simplicity in PDF, just render cleaned text
                    wrapped_lines = textwrap.fill(text, width=90).split('\n')
                    for line in wrapped_lines:
                        ax.text(margin_left, current_y, line,
                                ha='left', va='top',
                                fontsize=9,
                                color='#333333',
                                transform=ax.transAxes)
                        current_y -= line_height
                else:
                    wrapped_lines = textwrap.fill(text, width=90).split('\n')
                    for line in wrapped_lines:
                        ax.text(margin_left, current_y, line,
                                ha='left', va='top',
                                fontsize=9,
                                color='#333333',
                                transform=ax.transAxes)
                        current_y -= line_height
        
        # Add page number to each page
        ax.text(0.5, 0.02, f"Page {page_num}",
                ha='center', va='bottom',
                fontsize=8, color='gray',
                transform=ax.transAxes)
    
    # Add the last page
    figures.append(fig)
    plt.tight_layout()
    
    return figures

# Create the summary page figures
summary_figs = create_summary_pages()

# Create a list of all generated figure objects (summary first)
all_figures = summary_figs + [
    vol_per_exercise_fig,
    avg_wt_per_rep_per_ex_fig,
    total_wt_per_day_fig,
    total_wt_per_week_fig,
    total_wt_per_month_fig,
    avg_workout_duration_fig,
    top_day_week_fig,
    top_day_month_fig,
    top_day_year_fig,
    top_week_month_fig,
    top_month_year_fig,
    ex_monthly_variety_fig
]

today_date = datetime.now().strftime('%Y-%m-%d')
# Define the base directory and the specific sub-directory
base_dir = '/Users/Money/Dropbox/Python/100-days-of-code-python'
target_sub_dir = 'Capstone_Projects/GymTracker/visuals'

# Construct the full file path using os.path.join
pdf_filename = os.path.join(
    base_dir,
    target_sub_dir,
    f'{today_date}_Workout_Report.pdf'
)

# Ensure the target directory exists before saving
os.makedirs(os.path.dirname(pdf_filename), exist_ok=True)

print(f"\nSaving charts to: {pdf_filename}")
print(f"Summary will span {len(summary_figs)} page(s)")

# Use PdfPages to save all figures
with PdfPages(pdf_filename) as pdf:
    for fig in all_figures:
        # Save the figure to the open PDF file
        pdf.savefig(fig)
        # Close the figure to free up memory (optional but recommended)
        plt.close(fig)

print("PDF successfully generated with LLM summary!")