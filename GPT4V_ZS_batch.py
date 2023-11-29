from openai import OpenAI
import base64
import glob
import os
import json
from datetime import datetime
import time
import hashlib
import random 
from config_path import find_path
import yaml

client = OpenAI()


# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


dataset_name = 'dtd'  # ["Your Dataset Name Here"]
config_path = find_path(dataset_name)
with open(config_path, 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

categories = config['categories']
data_path = config['data_path']
image_files = sorted(glob.glob(os.path.join(data_path, "*", "*.jpg")))
random.seed(666)
random.shuffle(image_files)
total_num = len(image_files)
print('Total images: {}'.format(total_num))
print('Total classes: {}'.format(len(categories)))

output_dir = f'./GPT4V_Pred_{dataset_name}'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# hash encoding image names
all_names = []
hash_dict = {}
for idx in range(len(image_files)):
    ori_name = os.path.basename(image_files[idx])
    hash_name = hashlib.sha256(ori_name.encode('utf-8')).hexdigest()[:10]
    all_names.append(hash_name)
    hash_dict[hash_name] = ori_name
hash_dict_path = os.path.join(output_dir, 'hash_dict.json')
with open(hash_dict_path, "w") as file:
    json.dump(hash_dict, file, indent=4)


log_error = []
log_path = 'log_error.txt'
processed_image_num = 10  # batch size
processed_step = total_num // processed_image_num if total_num % processed_image_num == 0 else total_num // processed_image_num + 1
i = 0

while True:
    if i == processed_step:
        break
    try:
        st = i * processed_image_num
        end = (i+1) * processed_image_num
        print(f'processing {st}-{end} images')
        subset = image_files[st:end]  # choose images
        image_names = all_names[st:end]

        text_prompt = "I want you to act as a Texture Image Classifier with a ranking system. I will provide you with a set of images and a list of optinal categoris. Your task is to choose the 5 most relevant categories for each image and rank them from most to least likely to accurately describe the image. Provide the output in a list format, starting with the most likely category. Do not provide explanations for your choices or any additional information—just the ranked list of categories in a json format. Here are few images({}) and their optional categories({}). You have to choose strictly among the given categories and do not give any predictions that are not in the given category.".format(image_names, categories)


        base64Images = [encode_image(p) for p in subset]

        PROMPT_MESSAGES = [
            {
                "role": "user",
                "content": [
                    text_prompt,
                    *map(lambda x: {"image": x, "resize": 512}, base64Images),
                ],
            }
          ]

        params = {
            "model": "gpt-4-vision-preview",
            "messages": PROMPT_MESSAGES,
            "max_tokens": 4096  # upperbound
        }

        # request
        result = client.chat.completions.create(**params)

        markdown_str = result.choices[0].message.content
        json_str = markdown_str.replace('```json\n', '').replace('\n```', '')

        text_filename = '{}_{}_{}.json'.format(dataset_name, st, end)
        output_path = os.path.join(output_dir, text_filename)
        # Write the string to a text file
        with open(output_path, 'w') as file:
            file.write(json_str)

        print(result.usage)
        # with open('token_usage.txt', 'a+') as file:
        #     file.write(str(result.usage)+'\n')

        i = i + 1
        time.sleep(10)

    except Exception as e:
        current_date_and_time = datetime.now()
        error_information = current_date_and_time.strftime("%D:%H:%M:%S") + str(e) + '\n'
        # log_error.append(error_information)
        with open(log_path, 'a') as f:
            f.writelines(error_information)
        time.sleep(60)