import os
import csv
import base64
from openai import OpenAI
from tqdm import tqdm

def process_images(api_key, input_folder, prompt, output_file, model_name):
    client = OpenAI(
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )

    results = []

    # 获取图片文件列表
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    # 使用tqdm创建进度条
    for filename in tqdm(image_files, desc="Processing images"):
        image_path = os.path.join(input_folder, filename)
        
        # 读取并编码图片
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        try:
            # 调用Qwen-VL API
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{encoded_image}"
                                }
                            },
                            {"type": "text", "text": prompt},
                        ],
                    }
                ],
            )
            
            # 获取API响应
            api_response = response.choices[0].message.content
            
            # 将结果添加到列表
            results.append([filename, api_response])
            
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

    # 将结果写入CSV文件
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['image', 'response'])  # 写入表头
        writer.writerows(results)  # 写入数据行
