import os
from qwen_vl_processor import process_images

# 设置API密钥
API_KEY = "********"#请输入您的API密钥

# 设置输入参数
input_folder = "images"#请输入您的图片文件夹路径
prompt = "Describe this image in detail in Chinese."#请输入您的描述提示
output_file = "output.csv"#请输入您的输出文件路径
model_name = "qwen-vl-plus"  # 可选: "qwen-vl-max", "qwen-vl-plus"

# 调用功能函数
process_images(API_KEY, input_folder, prompt, output_file, model_name)

print(f"Processing complete. Results saved to {output_file}")
