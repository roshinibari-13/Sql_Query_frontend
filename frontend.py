import gradio as gr
import requests
import os

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "https://YOUR_BACKEND_URL.onrender.com"
)

def generate_sql(question):
    try:
        response = requests.post(
            f"{BACKEND_URL}/generate-sql",
            json={"question": question},
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()
            return data.get("sql", "No SQL generated.")
        else:
            return f"Error: {response.text}"

    except Exception as e:
        return f"Connection Error: {e}"


with gr.Blocks(title="AI SQL Query Generator") as demo:
    gr.Markdown("# AI SQL Query Generator")
    gr.Markdown("Enter your question in English and generate a MySQL query.")

    question = gr.Textbox(
        label="Enter your question",
        placeholder="Example: Show all students with marks greater than 80"
    )

    output = gr.Code(label="Generated SQL", language="sql")

    generate_btn = gr.Button("Generate SQL")

    generate_btn.click(
        fn=generate_sql,
        inputs=question,
        outputs=output
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
