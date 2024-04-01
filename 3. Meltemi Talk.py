import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# Load model directly
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the model
tokenizer = AutoTokenizer.from_pretrained("ilsp/Meltemi-7B-Instruct-v1")
model = AutoModelForCausalLM.from_pretrained(
    "ilsp/Meltemi-7B-Instruct-v1", torch_dtype=torch.bfloat16
)
model = model.to("cuda")

# Initialize fast api
app = FastAPI()

FORMAT = """<|system|> {input.system_propmt} </s> 
<|user|> {input.user_propmt} </s>
<|assistant|> """


class MeltemiInput(BaseModel):
    system_propmt: str
    user_propmt: str
    generation_conf: dict


@app.get("/")
def read_root():
    return {"Hello Welcome to the meltemi chat application"}


@app.post("/ask_meltemi")
def chat(input: MeltemiInput):
    text = FORMAT.format(input=input)
    inputs = tokenizer(text, return_tensors="pt").to("cuda")

    outputs = model.generate(**inputs, **input.generation_conf)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # split the response into the system and user message
    response = response.split("<|assistant|>")[1].strip()
    return {"answer": response}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="info")
