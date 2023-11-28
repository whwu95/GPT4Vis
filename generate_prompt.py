from openai import OpenAI
import os
import json
import time
from datetime import datetime
from config_path import find_path
import yaml

client = OpenAI()

dataset_name = 'dtd'  # ["Your Dataset Name Here"]

config_path = find_path(dataset_name)
with open(config_path, 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

categories = config['categories']

sentence_num = config['sentence_num']

log_error = []
log_path = 'log_error.txt'
error_count = 0
i = 0
end = 0

output_prompt = {}
output_dir = f'./{dataset_name}'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
output_path = os.path.join(output_dir, f'{dataset_name}_{sentence_num}_prompts_{i}_{end if end != 0 else len(categories)}_api.json')

PROMPT_MESSAGES = [
            {
                "role": "system",
                "content": "You are ChatGPT, a large language model trained by OpenAI."
            }]

while True:
    if i == (end if end != 0 else len(categories)):
        break
    try:
        print(f'processing {i}')
        text_prompt = config['prompt'].format(sentence_num, categories[i])
        PROMPT_MESSAGES = [{
            "role": "system",
            "content": "You are ChatGPT, a large language model trained by OpenAI."
        }, {"role": "user", "content": text_prompt}]

        params = {
            "model": "gpt-4-1106-preview",
            "messages": PROMPT_MESSAGES,
            "max_tokens": 4096  # upperbound
        }

        result = client.chat.completions.create(**params)

        markdown_str = result.choices[0].message.content
        print(markdown_str)
        # PROMPT_MESSAGES.append({"role": "assistant", "content": markdown_str})
        json_str = markdown_str.replace('```json\n', '').replace('\n```', '')
        output_prompt[categories[i]] = json.loads(json_str)[categories[i]]

        with open(output_path, 'w') as f:
            json.dump(output_prompt, f, indent=4)

        print(f'processed {i}/{len(categories)}, {result.usage}, {len(PROMPT_MESSAGES)}')

        i = i + 1
        error_count = 0
        # time.sleep(20)
    except Exception as e:
        error_count += 1
        current_date_and_time = datetime.now()
        error_information = current_date_and_time.strftime("%D:%H:%M:%S") + str(e) + '\n'
        # log_error.append(error_information)
        with open(log_path, 'a') as f:
            f.writelines(error_information)
        time.sleep(2)
        if error_count == 2:
            with open(log_path, 'a') as f:
                f.writelines(f'skip {i}!!!!!!!!!!!\n')
            i += 1
            error_count = 0