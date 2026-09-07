import chainlit as cl
import dotenv

dotenv.load_dotenv()

@cl.on Message
async def on_message(message: cl.Message):
    await cl.Message(content=f"Received: {message.content}").send()