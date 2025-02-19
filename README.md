# Qwen-VL 街道图像评估工具

## 项目概述

Qwen-VL 街道图像评估工具是一个 Python 脚本，用于批量处理街道图像并使用阿里云的 Qwen-VL 视觉语言模型生成评分。该脚本读取指定文件夹中的所有图像，将它们发送到 Qwen-VL API，并根据不同的评估维度和方法生成评分，最后将结果保存在 CSV 文件中。

## 功能特点

- 批量处理本地街道图像文件
- 使用 Qwen-VL API 生成图像评分
- 支持多种图像格式（PNG, JPG, JPEG, BMP, GIF）
- 支持多个评估维度：安全性、舒适度、美观度、社交性
- 每个维度支持三种评估方法：直接、引导、结构化
- 进度条显示处理进度
- 结果保存为 CSV 文件

## 安装说明

1. 确保您的系统已安装 Python 3.6 或更高版本。

2. 克隆此仓库或下载源代码。

3. 在项目目录中，安装所需的依赖项：

   ```bash
   pip install openai tqdm
   ```

## 使用方法

1. 在 `main.py` 文件中设置以下参数：
   - `API_KEY`: 您的阿里云 API 密钥
   - `input_folder`: 包含街道图像的文件夹路径
   - `output_folder`: 输出 CSV 文件的文件夹路径

2. 运行脚本：
   - 处理所有评估维度和方法：
     ```
     python main.py
     ```
   - 处理特定的评估维度和方法：
     ```
     python main.py [function] [type]
     ```
     例如：`python main.py safety direct`

3. 脚本将处理指定文件夹中的所有图像，并在控制台显示进度条。

4. 处理完成后，结果将保存在指定的 CSV 文件中。

## 评估维度和方法

- 评估维度（functions）：
  - safety: 安全性
  - comfort: 舒适度
  - aesthetics: 美观度
  - sociability: 社交性

- 评估方法（types）：
  - direct: 直接评估
  - guided: 引导式评估
  - structured: 结构化评估

## CSV 输出格式

输出的 CSV 文件包含两列：
- `image`: 图像文件名
- `response`: Qwen-VL 生成的评分（1-5分）

## 注意事项

- 确保您有足够的阿里云 API 配额来处理所有图像。
- 大型图像文件可能需要较长的处理时间。
- 请确保您的网络连接稳定，以便与 API 进行通信。
