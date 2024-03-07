import json
import os
import copy

pred_json_path = 'GPT4V_ZS_Results/imagenet.json'
gt_json_path = 'annotations/imagenet_gt.json'

with open(pred_json_path, 'r') as f:
    pred_data = json.load(f)

print('pred', len(pred_data))


with open(gt_json_path, 'r') as f:
    gt_data = json.load(f)

print('gt', len(gt_data))

new_gt_data = {}
for k, v in gt_data.items():
    new_gt_data[k] = v.replace('_', ' ')
gt_data = new_gt_data
del new_gt_data

total_img = 0
correct_img = 0
top_5_img = 0

# error_category = {}
category = set(gt_data.values())
new_category = set()
for c in category:
    new_category.add(c.replace('_', ' '))
category = new_category

additional_category = set()

for idx, (img, pred) in enumerate(pred_data.items()):
    # if '.JPEG' not in img:
    #     img += '.JPEG'
    if img in gt_data:
        total_img += 1
        for p in pred[:]:
            if p not in category:
                additional_category.add(p)
                pred.remove(p)
        if len(pred) == 0:
            continue
        if pred[0] == gt_data[img]:
            correct_img += 1
        else:
            pass
            # print(f'img: {img}, pred: {pred[0]}, gt: {gt_data[img]}')
        if gt_data[img] in pred:
            top_5_img += 1
    else:
        pass
        print(f'{idx},{img} not in gt')

# print(len(additional_category), additional_category)
print(f'Total images num: {total_img}, Top1 acc: {correct_img/total_img}, error num:{total_img - correct_img}, Top5 acc: {top_5_img/total_img}')

# for label, error_num in error_category.items():
#     print(f'error category: {label}, error num: {error_num}')