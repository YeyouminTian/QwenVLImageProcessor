# Qwen-VL Image Processor

## 项目概述

Qwen-VL Image Processor 是一个 Python 脚本，用于批量处理图像并使用阿里云的 Qwen-VL 视觉语言模型生成描述。该脚本读取指定文件夹中的所有图像，将它们发送到 Qwen-VL API，并将生成的描述保存在 CSV 文件中。

## 功能特点

- 批量处理本地图像文件
- 使用 Qwen-VL API 生成图像描述
- 支持多种图像格式（PNG, JPG, JPEG, BMP, GIF）
- 进度条显示处理进度
- 结果保存为 CSV 文件

## 安装说明

1. 确保您的系统已安装 Python 3.6 或更高版本。

2. 克隆此仓库或下载源代码。

3. 在项目目录中，安装所需的依赖项：
   ```
   pip install openai tqdm   ```

## 使用方法

1. 在 `main.py` 文件中设置以下参数：

   - `API_KEY`: 您的阿里云 API 密钥
   - `input_folder`: 包含图像的文件夹路径
   - `prompt`: 用于生成描述的提示文本
   - `output_file`: 输出 CSV 文件的名称
   - `model_name`: 要使用的 Qwen-VL 模型（"qwen-vl-max" 或 "qwen-vl-plus"）

2. 运行脚本：
   ```
   python main.py   ```

3. 脚本将处理指定文件夹中的所有图像，并在控制台显示进度条。

4. 处理完成后，结果将保存在指定的 CSV 文件中。

## CSV 输出格式

输出的 CSV 文件包含两列：

- `image`: 图像文件名
- `response`: Qwen-VL 生成的图像描述