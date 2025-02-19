import os
import sys
from qwen_vl_processor import process_images

# 设置API密钥
API_KEY = "*********"  # 请输入您的API密钥

# 设置输入参数
input_folder = "image"  # 请输入您的图片文件夹路径
output_folder = "results"  # 输出文件夹路径

# 定义function和type列表
functions = ["safety", "comfort", "aesthetics", "sociability"]
types = ["direct", "guided", "structured"]

# 定义prompt字典
prompts = {
    "safety": {
        "direct": "分析这张街道图片的出行安全性。\n完整思考评估过程后，仅回复一个数字作为评分：\n5=很安全\n4=较安全\n3=适中\n2=有点不安全\n1=很不安全. 【请直接回复评分，不要输出其他内容，这十分重要】",
        "guided": "作为城市规划专家，请仔细分析这张街道图片的出行安全性。\n考虑：人行道状况、交通设施、照明条件、无障碍设施等要素。\n完成分析后，仅输出一个数字评分：\n5=很安全\n4=较安全\n3=适中\n2=有点不安全\n1=很不安全【请直接回复评分，不要输出其他内容，这十分重要】",
        "structured": "请按以下步骤评估街道出行安全性：\n1. 分析基础设施（人行道、交通设施、照明）\n2. 评估使用者安全（行人空间、非机动车条件、无障碍设施）\n3. 考虑环境安全（视线通透度、监控覆盖）\n严格按照以下标准给出评分：\n5=很安全（完善的安全设施和友好的步行环境）\n4=较安全（基本安全设施齐全，环境总体安全）\n3=适中（存在一些安全隐患，但不严重）\n2=有点不安全（多个安全问题待改善）\n1=很不安全（存在严重安全隐患）\n完成分析后，仅输出一个数字作为最终评分。【请直接回复评分，不要输出其他内容，这十分重要】"
    },
    "comfort": {
        "direct": "分析这张街道图片的环境舒适度。\n完整思考评估过程后，仅回复一个数字作为评分：\n5=很舒适\n4=较舒适\n3=适中\n2=有点不舒适\n1=很不舒适【请直接回复评分，不要输出其他内容，这十分重要】",
        "guided": "作为城市环境评估专家，请仔细分析这张街道图片的环境舒适度。\n考虑：绿化覆盖、遮阳设施、噪音环境、空间尺度、微气候条件等要素。\n完成分析后，仅输出一个数字评分：\n5=很��适\n4=较舒适\n3=适中\n2=有点不舒适\n1=很不舒适【请直接回复评分，不要输出其他内容，这十分重要】",
        "structured": "请按以下步骤评估街道环境舒适度：\n1. 分析自然环境要素\n   - 绿化覆盖情况（树木、植被）\n   - 遮阴效果\n   - 通风条件\n2. 评估人工环境要素\n   - 街道尺度与围合度\n   - 遮阳设施完善度\n   - 休憩设施布置\n3. 考虑环境干扰因素\n   - 噪音水平\n   - 空气质量表现\n   - 拥挤程度\n严格按照以下标准给出评分：\n5=很舒适（绿化充足，环境宜人，干扰极少）\n4=较舒适（环境要素较好，偶有干扰）\n3=适中（基本舒适，存在一些不足）\n2=有点不舒适（多个环境问题，影响体验）\n1=很不舒适（环境质量差，干扰严重）\n完成分析后，仅输出一个数字作为最终评分。【请直接回复评分，不要输出其他内容，这十分重要】"
    },
    "aesthetics": {
        "direct": "分析这张街道图片的视觉美观度。\n完整思考评估过程后，仅回复一个数字作为评分：\n5=很美观\n4=较美观\n3=适中\n2=有点不美观\n1=很不美观【请直接回复评分，不要输出其他内容，这十分重要】",
        "guided": "作为城市景观设���专家，请仔细分析这张街道图片的视觉美观度。\n考虑：建筑立面、色彩搭配、空间序列、街道家具、景观小品、整体协调性等要素。\n完成分析后，仅输出一个数字评分：\n5=很美观\n4=较美观\n3=适中\n2=有点不美观\n1=很不美观【请直接回复评分，不要输出其他内容，这十分重要】",
        "structured": "请按以下步骤评估街道视觉美观度：\n1. 分析空间构成要素\n   - 建筑立面的风格与质感\n   - 街道空间的尺度与比例\n   - 天际线的连续性与变化\n2. 评估景观设计要素\n   - 绿化景观的层次感\n   - 街道家具的设计品质\n   - 铺装材质的协调性\n   - 景观小品的艺术性\n3. 考虑视觉整合性\n   - 色彩方案的和谐度\n   - 材质搭配的统一性\n   - 细节处理的精致度\n   - 日间/夜间景观效果\n严格按照以下标准给出评分：\n5=很美观（设计优秀，细节精致，高度和谐）\n4=较美观（整体协调，有特色，轻微瑕疵）\n3=适中（基本美观，但缺乏特色）\n2=有点不美观（多处设计问题，视觉杂乱）\n1=很不美观（设计粗糙，严重不协调）\n完成分析后，仅输出一个数字作为最终评分。【请直接回复评分，不要输出其他内容，这十分重要】"
    },
    "sociability": {
        "direct": "分析这张街道图片的交往适宜性。\n完整思考评估过程后，仅回复一个数字作为评分：\n5=很适宜交往\n4=较适宜交往\n3=适中\n2=有点不适宜交往\n1=很不适宜交往【请直接回复评分，不要输出其他内容，这十分重要】",
        "guided": "作为公共空间行为研究专家，请仔细分析这张街道图片的交往适宜性。\n考虑：驻留空间、休憩设施、活动场地、界面开放性、步行友好性、社交距离等要素。\n完成分析后，仅输出一个数字评分：\n5=很适宜交往\n4=较适宜交往\n3=适中\n2=有点不适宜交往\n1=很不适宜交往【请直接回复评分，不要输出其他内容，这十分重要】",
        "structured": "请按以下步骤评估街道交往适宜性：\n1. 分析空间支持度\n   - 驻留空间的规模与分布\n   - 休憩设施的类型与数量\n   - 遮阳避雨设施的覆盖\n   - 街道边界的开放程度\n2. 评估行为便利性\n   - 步行环境的友好度\n   - 社交距离的适宜性\n   - 活动空间的灵活性\n   - 界面互动的可能性\n3. 考虑环境促进度\n   - 空间吸引力\n   - 微气候宜人度\n   - 噪音干扰程度\n   - 安全感营造\n严格按照以下标准给出评分：\n5=很适宜交往（空间友好，设施完善，高度促进社交）\n4=较适宜交往（基本具备条件，环境总体支持交往）\n3=适中（可以进行交往，但存在一些局限）\n2=有点不适宜交往（多个因素制约社交活动）\n1=很不适宜交往（环境抑制交往，不利于社交活动）\n完成分析后，仅输出一个数字作为最终评分。【请直接回复评分，不要输出其他内容，这十分重要】"
    }
}

model_name = "qwen-vl-max"  # 可选: "qwen-vl-max", "qwen-vl-plus"

def process_single_combination(function, type):
    if function in functions and type in types:
        prompt = prompts[function][type]
        output_file = os.path.join(output_folder, f"{function}-{type}.csv")
        process_images(API_KEY, input_folder, prompt, output_file, model_name)
        print(f"Processing complete for {function}-{type}. Results saved to {output_file}")
    else:
        print(f"Invalid function '{function}' or type '{type}'. Please check your input.")

def process_all_combinations():
    for func in functions:
        for t in types:
            process_single_combination(func, t)

def main():
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    if len(sys.argv) == 3:
        process_single_combination(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 1:
        process_all_combinations()
    else:
        print("Usage: python main.py [function] [type]")
        print("Available functions:", ", ".join(functions))
        print("Available types:", ", ".join(types))
        print("If no arguments are provided, all combinations will be processed.")

    print("All processing complete.")

if __name__ == "__main__":
    main()
