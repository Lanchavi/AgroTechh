import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with Krishi Sathi AI powered chatbot")
outputs = gr.outputs.Textbox(label="Here is your desired result")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Krishi Sathi",
             description="Farmer Assistance Ask anything you want",
             theme="compact").launch(share=True)