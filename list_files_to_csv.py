import os
import csv
from natsort import natsorted



def list_files_to_csv(directory_path, output_csv_path):

    """

    读取指定目录下的所有文件名,按自然名称升序排序,然后输出到CSV文件。



    参数:

    directory_path (str): 要读取的目录路径

    output_csv_path (str): 输出CSV文件的路径



    返回:

    None

    """

    try:

        # 获取目录下所有文件名并进行自然排序

        file_names = natsorted(os.listdir(directory_path))

        

        # 写入CSV文件

        with open(output_csv_path, 'w', newline='', encoding='utf-8-sig') as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow(['File Name'])  # 写入表头

            for file_name in file_names:

                writer.writerow([file_name])

        

        print(f"文件列表已成功写入 {output_csv_path}")

    except Exception as e:

        print(f"发生错误: {str(e)}")



# 示例使用

if __name__ == "__main__":

    directory_to_scan = r"D:\LifeOS\1. 项目\学校课程-研一上\城市研究方法\svi收集"  # 当前目录,可以根据需要修改

    output_file = "file_list.csv"

    list_files_to_csv(directory_to_scan, output_file)


