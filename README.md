<div align="center">



<h2 align="center"> <a href="https://arxiv.org/abs/2311.15732">GPT4Vis: What Can GPT-4 Do for Zero-shot Visual Recognition?</a></h2>
<h5 align="center"> If you like our project, please give us a star ⭐ on GitHub for latest update.  </h2>


[![arXiv](https://img.shields.io/badge/Arxiv-2311.15732-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/2311.15732) 
[![zhihu](https://img.shields.io/badge/-知乎-000000?logo=zhihu&logoColor=0084FF)](https://zhuanlan.zhihu.com/p/669758735)


[Wenhao Wu](https://whwu95.github.io/)<sup>1,2</sup>, [Huanjin Yao](https://openreview.net/profile?id=~Huanjin_Yao1)<sup>2,3</sup>, [Mengxi Zhang](https://scholar.google.com/citations?user=73tAoEAAAAAJ&hl=en)<sup>2,4</sup>, [Yuxin Song](https://openreview.net/profile?id=~YuXin_Song1)<sup>2</sup>, [Wanli Ouyang](https://wlouyang.github.io/)<sup>5</sup>, [Jingdong Wang](https://jingdongwang2017.github.io/)<sup>2</sup>

 
<sup>1</sup>[The University of Sydney](https://www.sydney.edu.au/), <sup>2</sup>[Baidu](https://vis.baidu.com/#/), <sup>3</sup>[Tsinghua University](https://www.tsinghua.edu.cn/en/), <sup>4</sup>[Tianjin University](https://www.tju.edu.cn/english/index.htm/), <sup>5</sup>[The Chinese University of Hong Kong](https://www.cuhk.edu.hk/english/#)


</div>

***
This work delves into an essential, yet must-know baseline in light of the latest advancements in Generative Artificial Intelligence (GenAI): the utilization of GPT-4 for visual understanding. We center on the evaluation of GPT-4's linguistic and visual capabilities in zero-shot visual recognition tasks. To ensure a comprehensive evaluation, we have conducted experiments across three modalities—images, videos, and point clouds—spanning a total of 16 popular academic benchmark. 

<div align="center">
<img src="docs/method.png" width="800" />
</div>

<details open><summary>📣 I also have other cross-modal projects that may interest you ✨. </summary><p>


> [**Revisiting Classifier: Transferring Vision-Language Models for Video Recognition**](https://arxiv.org/abs/2207.01297)<br>
> Wenhao Wu, Zhun Sun, Wanli Ouyang <br>
> [![Conference](http://img.shields.io/badge/AAAI-2023-f9f107.svg)](https://ojs.aaai.org/index.php/AAAI/article/view/25386/25158) [![Journal](http://img.shields.io/badge/IJCV-2023-Bf107.svg)](https://link.springer.com/article/10.1007/s11263-023-01876-w) [![github](https://img.shields.io/badge/-Github-black?logo=github)](https://github.com/whwu95/Text4Vis) 


> [**Bidirectional Cross-Modal Knowledge Exploration for Video Recognition with Pre-trained Vision-Language Models**](https://arxiv.org/abs/2301.00182)<br>
> Wenhao Wu, Xiaohan Wang, Haipeng Luo, Jingdong Wang, Yi Yang, Wanli Ouyang <br>
> [![Conference](http://img.shields.io/badge/CVPR-2023-f9f107.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Wu_Bidirectional_Cross-Modal_Knowledge_Exploration_for_Video_Recognition_With_Pre-Trained_Vision-Language_CVPR_2023_paper.html) [![github](https://img.shields.io/badge/-Github-black?logo=github)](https://github.com/whwu95/BIKE) 


> [**Cap4Video: What Can Auxiliary Captions Do for Text-Video Retrieval?**](https://arxiv.org/abs/2301.00184)<br>
> Wenhao Wu, Haipeng Luo, Bo Fang, Jingdong Wang, Wanli Ouyang <br>
> Accepted by CVPR 2023 as 🌟Highlight🌟 | [![Conference](http://img.shields.io/badge/CVPR-2023-f9f107.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Wu_Cap4Video_What_Can_Auxiliary_Captions_Do_for_Text-Video_Retrieval_CVPR_2023_paper.html) [![github](https://img.shields.io/badge/-Github-black?logo=github)](https://github.com/whwu95/Cap4Video)<br>


</p></details>




## News
- [x] **[Mar 8, 2024]** We have updated all results in our [report](https://arxiv.org/abs/2311.15732). For accurate predictions, we strongly recommend using single testing with GPT-4V and have accordingly eliminated scripts related to batch testing.
- [x] **[Mar 7, 2024]** 
Due to the recent removal of RPD (request per day) limits on the GPT-4V API, we've updated our predictions for all datasets using standard single testing (one sample per request) and shared all results in the [**GPT4V_ZS_Results**](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results) folder! **Additionally, we offer a reference data point: the total cost of invoking the GPT-4V API to test across all datasets once is estimated to be around $4000, intended to assist readers in their planning.**
- [x] **[Nov 28, 2023]** We release our [report](https://arxiv.org/abs/2311.15732) in Arxiv.
- [x] **[Nov 27, 2023]** Our prompts have been released. Thanks for your star 😝.


## Overview

<!-- <h3 style="text-align: center;">Zero-shot visual recognition leveraging GPT-4's linguistic and visual capabilities.</h3> -->




<div align="center">
An overview of 16 evaluated popular benchmark datasets, comprising images, videos, and point clouds.

<img src="docs/datasets.png" width="800">

Zero-shot visual recognition leveraging GPT-4's linguistic and visual capabilities.
<img src="docs/results.jpg" width="800">
</div>


## Generated Descriptions from GPT-4

<div align="center">
<img src="docs/generated_sentences.png" width="800" />
</div>

- We have pre-generated descriptive sentences for all the categories across the datasets, which you can find in the [**GPT_generated_prompts**](https://github.com/whwu95/GPT4Vis/tree/main/GPT4_generated_prompts) folder. Enjoy exploring!

- We've also provided the example script to help you generate descriptions using GPT-4. For guidance on this, please refer to the [generate_prompt.py](https://github.com/whwu95/GPT4Vis/blob/main/generate_prompt.py) file. Happy coding! Please refer to the [**config**](https://github.com/whwu95/GPT4Vis/tree/main/config) folder for detailed information on all datasets used in our project. 
- Execute the following command to generate descriptions with GPT-4.
  ```sh
  # To run the script for specific dataset, simply update the following line with the name of the dataset you're working with: 
  # dataset_name = ["Dataset Name Here"]   # e.g., dtd
  python generate_prompt.py
  ```

## GPT-4V(ision) for Visual Recognition
<div align="center">
<img src="docs/gpt4v_prompt.png" width="800" />
</div>

- We share an example script that demonstrates how to use the GPT-4V API for zero-shot predictions on the DTD dataset. Please refer to the [GPT4V_ZS.py](https://github.com/whwu95/GPT4Vis/blob/main/GPT4V_ZS.py) file for a step-by-step guide on implementing this. We hope it helps you get started with ease!

  ```sh
  # GPT4V zero-shot recognition script. 
  # dataset_name = ["Dataset Name Here"]   # e.g., dtd
  python GPT4V_ZS.py
  ```

- All results are available in the [**GPT4V_ZS_Results**](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results) folder! In addition, we've provided the [**Datasets link**](https://unisyd-my.sharepoint.com/:f:/g/personal/wenhao_wu_sydney_edu_au/EmoNoASH2b1JqQXb14fx0tMBkj4VU3nOUrKyt9ZT1aIw2Q?e=jNL0CL) along with their corresponding ground truths ([**annotations**](https://github.com/whwu95/GPT4Vis/tree/main/annotations) folder) to help readers in replicating the results.

| DTD |  EuroSAT |  SUN397 |  RAF-DB |  Caltech101  | ImageNet-1K | FGVC-Aircraft | Flower102 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| [57.7](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/dtd.json)  | [46.8](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/eurosat.json) |  [59.2](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/sun397.json) |  [68.7](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/rafdb.json) | [93.7](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/caltech101.json)  |  [xx](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/ImageNet-1K.json) | [56.6](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/aircraft.json) |  [69.1](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/flower102.json) | 
|  [Label](https://github.com/whwu95/GPT4Vis/tree/main/annotations/dtd_gt.json)  |  Label  | Label   | Label   |  Label  |  Label  |  Label  | Label   |
   


| Stanford Cars | Food101| Oxford Pets | UCF-101 | HMDB-51 | Kinetics-400 | ModelNet-10 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
[62.7](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/car.json)  |  [86.2](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/food101.json) | [90.8](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/pets.json) | [83.7](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/ucf_8frame.json) | [58.8](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/hmdb_8frame.json) | [58.8](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/k400.json) | [66.6](https://github.com/whwu95/GPT4Vis/tree/main/GPT4V_ZS_Results/modelnet10_front.json) |
|  Label  |  Label  | Label   | [Label](https://github.com/whwu95/GPT4Vis/tree/main/annotations/ucf_gt.json)   |  [Label](https://github.com/whwu95/GPT4Vis/tree/main/annotations/hmdb_gt.json)  |  [Label](https://github.com/whwu95/GPT4Vis/tree/main/annotations/k400_gt.json)  |  [Label](https://github.com/whwu95/GPT4Vis/tree/main/annotations/modelnet10_gt.json)   |


## Requirement
For guidance on setting up and running the GPT-4 API, we recommend checking out the official OpenAI Quickstart documentation available at: [OpenAI Quickstart Guide](https://platform.openai.com/docs/quickstart).





<a name="bibtex"></a>
## 📌 BibTeX & Citation

If you use our code in your research or wish to refer to the results, please star 🌟 this repo and use the following BibTeX 📑 entry.

```bibtex
@article{GPT4Vis,
  title={GPT4Vis: What Can GPT-4 Do for Zero-shot Visual Recognition?},
  author={Wu, Wenhao and Yao, Huanjin and Zhang, Mengxi and Song, Yuxin and Ouyang, Wanli and Wang, Jingdong},
  booktitle={arXiv preprint arXiv:2311.15732},
  year={2023}
}
```

<a name="acknowledgment"></a>
## 🎗️ Acknowledgement
This evaluation is built on the excellent works:
- [CLIP](https://github.com/openai/CLIP): Learning Transferable Visual Models From Natural Language Supervision
- [GPT-4](https://platform.openai.com/docs/guides/vision)
- [Text4Vis](https://github.com/whwu95/Text4Vis): Transferring Vision-Language Models for Visual Recognition: A Classifier Perspective
  
We extend our sincere gratitude to these contributors.



## 👫 Contact
For any questions, please feel free to file an issue.
