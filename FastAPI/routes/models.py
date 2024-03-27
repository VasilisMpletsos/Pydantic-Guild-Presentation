import torch

from models import ModelInference, UserInput
from fastapi import APIRouter, Depends

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

router = APIRouter(prefix="/model", tags=["Models"])

# # Load the model and the tokenizer
# tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
# model = AutoModelForCausalLM.from_pretrained(
#     "mistralai/Mistral-7B-Instruct-v0.2", torch_dtype=torch.bfloat16
# )
# model = model.to("cuda")


# @router.post("/llm_query")
# async def llm_query(inference_input: ModelInference):

#     FORMAT = """<s> [INST] System:{input.system_prompt}
#     User Message: {input.user_prompt} [/INST]"""

#     text = FORMAT.format(input=inference_input)
#     inputs = tokenizer(text, return_tensors="pt").to("cuda")

#     outputs = model.generate(
#         **inputs,
#         max_length=200,
#         do_sample=True,
#         temperature=0.9,
#         top_k=50,
#         top_p=0.95,
#         num_return_sequences=1,
#     )
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)

#     # split the response into the system and user message
#     response = response.split("[/INST]")[1].strip()

#     return {"response": response}
