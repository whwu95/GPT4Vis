from openai import OpenAI
import base64
import glob
import os
import json
from datetime import datetime
import time
import hashlib
import random 

client = OpenAI()

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


data_path = 'dataset/dtd'
image_files = sorted(glob.glob(os.path.join(data_path, "*", "*.jpg")))
random.seed(666)
random.shuffle(image_files)
total_num = len(image_files)
print('Total images: {}'.format(total_num))


categories = ['banded', 'blotchy', 'braided', 'bubbly', 'bumpy', 'chequered', 'cobwebbed', 'cracked', 'crosshatched', 'crystalline', 'dotted', 'fibrous', 'flecked', 'freckled', 'frilly', 'gauzy', 'grid', 'grooved', 'honeycombed', 'interlaced', 'knitted', 'lacelike', 'lined', 'marbled', 'matted', 'meshed', 'paisley', 'perforated', 'pitted', 'pleated','polka-dotted', 'porous', 'potholed', 'scaly', 'smeared', 'spiralled', 'sprinkled', 'stained', 'stratified', 'striped', 'studded', 'swirly', 'veined', 'waffled', 'woven', 'wrinkled', 'zigzagged']
print('Total classes: {}'.format(len(categories)))



# generate gt dict
gt_dict = {}
all_names = []
for idx in range(len(image_files)):
    ori_name = os.path.basename(image_files[idx])
    # new_name = hashlib.sha256(ori_name.encode('utf-8')).hexdigest()[:4]
    new_name = hashlib.sha256(ori_name.encode('utf-8')).hexdigest()[:7] # + ori_name[-9:-4]
    all_names.append(new_name)
    gt_dict[new_name] = ori_name.split('_')[0]
with open('dtd_gt_hash.json', "w") as file:
    json.dump(gt_dict, file, indent=4)

log_error = []
log_path = 'log_error.txt'
processed_image_num = 10
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

        text_prompt = "I want you to act as an Image Texture Classifier with a ranking system. I will provide you with a set of images and a list of potential categoris. Your task is to choose the 5 most relevant categories for each image and rank them from most to least likely to accurately describe the image. Provide the output in a list format, starting with the most likely category. Do not provide explanations for your choices or any additional information—just the ranked list of categories in a json format. Here are the first few images({}) and their possible categories({}). Evaluate each image only once and don't generate categories that are not in the given categoryies.".format(image_names, categories)


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

        text_filename = 'dtd_{}_{}.json'.format(st, end)
        # Write the string to a text file
        with open(text_filename, 'w') as file:
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