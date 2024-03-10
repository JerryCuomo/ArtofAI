# Source: "Think Artificial Intelligence" by Jerry Cuomo, 2024
# Purpose: Educational code examples from the book.
# Copyright © 2024 Jerry Cuomo. All rights reserved.
#
# This code was autogenerated by GPT-4, from the following prompt:
# Prompt: Visualize the hierarchical structure of the Anatomy of an AI Solution, showcasing the relationship between AI and Cloud Services. 
# Use layers {L1: "Cloud"}, {L2: "AI Services | Model Data, Model Train, Model Serve, Model Govern"}, {L3: "Automation Services | Workflow, Decisions, Integration, Mobile/IoT"}, {L4: "Digital Labor | Talent, Carebots, Codebots, Salesbots, Cloud ITBots"}, and {L5: "AI Solutions"} to detail the stack from foundational cloud infrastructure to advanced AI solutions.
#
# About: This script generates a visual representation of the market-ecture of the Anatomy of an AI Solution, unpacking the intricate AI-Cloud Services Relationship. It leverages Python's NetworkX and Matplotlib libraries to create a multilayer stack diagram that outlines the core components and services that underpin AI technologies, providing a clear and educational insight into how these elements interact to form comprehensive AI solutions.
#
# Setup: Python installed with NetworkX and Matplotlib. Install using 'pip install networkx matplotlib'.

import matplotlib.pyplot as plt

# Define layer labels and their colors
layer_labels = ["Cloud", "AI Services", "Automation Services", "Digital Labor", "AI Solutions"]
colors = {
    "Cloud": ("lightgray", "black"),
    "AI Services": ("darkblue", "white"),
    "Automation Services": ("darkgreen", "white"),
    "Digital Labor": ("darkred", "white"),
    "AI Solutions": ("black", "white")
}

# Define subcategories for each layer
sub_categories = {
    "Cloud": [],
    "AI Services": ["Model Data", "Model Train", "Model Serve", "Model Govern"],
    "Automation Services": ["Workflow", "Decisions", "Integration", "Mobile/IoT"],
    "Digital Labor": ["Talent", "Carebots", "Codebots", "Salesbots", "Cloud ITBots"],
    "AI Solutions": []
}

# Function to create sub-categories text
def create_sub_cat_text(sub_categories):
    return " | ".join(sub_categories) if sub_categories else ""

# Define spacing between layers for layout adjustment
layer_spacing = 0.5

# Create the plot
fig, ax = plt.subplots(figsize=(14, 10))

# Drawing layers with centered labels and larger font
for i, label in enumerate(layer_labels):
    # Draw the main layer
    ax.barh(i * layer_spacing, 1, height=0.5, color=colors[label][0], edgecolor='black')
    # Prepare the text: main category in bold, followed by sub-categories if any
    # Fix for displaying category labels with spaces
    text_label = f"$\\bf{{\\text{{{label}}}}}$: " if sub_categories[label] else f"$\\bf{{\\text{{{label}}}}}$"
    text_sub_cats = create_sub_cat_text(sub_categories[label])
    full_text = text_label + text_sub_cats
    # Label for the main category and its sub-categories with larger font and centered
    ax.text(0.5, i * layer_spacing, full_text, ha='center', va='center', fontsize=16, color=colors[label][1], wrap=True)

# Adjusting the overall graph limits based on new layer spacing
ax.set_xlim(0, 1)
ax.set_ylim(-0.25, len(layer_labels) * layer_spacing)
plt.yticks([])  # Hide y-axis ticks
ax.set_xticks([])  # Hide x-axis ticks
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()
plt.show()