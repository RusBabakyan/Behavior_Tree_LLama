import torch
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer
model_path = "model/checkpoint-50"

def get_promt(input_text):
    prompt = f"""
    Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

    ### Instruction:
    Generate anwer in XML format using tags: task, action, direction, object, location

    ### Input:
    {input_text}

    ### Response:
    """
    return prompt

def save_XML(text):
    with open("output.xml", "w", encoding="utf-8") as file:
        file.write(text)

def main():
    try:
        model = AutoPeftModelForCausalLM.from_pretrained(
            model_path,
            low_cpu_mem_usage=True,
            torch_dtype=torch.float16,
            load_in_4bit=True,
        )
    except:
        raise FileNotFoundError("Model not found, extract model from model.zip here")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    print("Model ready")
    while True:
        input_text = input("Write a input task: ")
        if not input_text:
            continue
        prompt = get_promt(input_text)
        input_ids = tokenizer(prompt, return_tensors="pt", truncation=True).input_ids.cuda()
        outputs = model.generate(input_ids=input_ids, max_new_tokens=512, do_sample=True, top_p=0.6,temperature=0.9)
        output_text = tokenizer.batch_decode(outputs.detach().cpu().numpy(), skip_special_tokens=True)[0][len(prompt):]
        
        print(f"Input:\n{input_text}\n")
        print(f"Generated Response:\n{output_text}\n")

        save_XML(output_text)

if __name__ == '__main__':
    main()
