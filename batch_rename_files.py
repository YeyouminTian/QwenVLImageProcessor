import os
import csv

def batch_rename_files(directory_path, csv_file_path):
    """
    批量重命名指定目录下的文件。

    参数:
    directory_path (str): 要重命名文件的目录路径
    csv_file_path (str): 包含原文件名和新文件名的CSV文件路径

    返回:
    None
    """
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) != 2:
                    print(f"跳过无效行: {row}")
                    continue

                original_name, new_name = row
                original_path = os.path.join(directory_path, original_name)
                new_path = os.path.join(directory_path, new_name)

                if os.path.exists(original_path):
                    os.rename(original_path, new_path)
                    print(f"已将 {original_name} 重命名为 {new_name}")
                else:
                    print(f"文件 {original_name} 不存在，跳过重命名")
    except Exception as e:
        print(f"发生错误: {str(e)}")

# 示例使用
if __name__ == "__main__":
    directory_to_rename = "images"  # 当前目录,可以根据需要修改
    csv_file = "file_list.csv"  # CSV文件名,可以根据需要修改
    batch_rename_files(directory_to_rename, csv_file)
