import pandas as pd
import os

# 设置文件路径
data_dir = r'C:\Users\why\CODE\PYTHON\split\data'

# filename 为需要分解的表名

filename = "house_tiny.xlsx" 
input_file = os.path.join(data_dir, filename)


if filename.endswith(".xlsx"):
    # 读取 XLSX 文件
    # rows = []
    with pd.ExcelFile(input_file, engine='openpyxl') as xls:
        df = pd.read_excel(xls)

        # 获取所有列名
        columns = df.columns

        # 将列名转换为列表
        columns_list = columns.tolist()

        if df.empty:
            print("打开文件为空")

        else:
            for index, row in df.iterrows():
                # 创建 DataFrame
                # print(index)
                
                df_new = pd.DataFrame(columns=columns_list)
                df_new.loc[0] = row.tolist()
                
                # 将 DataFrame 写入新文件
                
                output_file = os.path.join(data_dir, '{}.xlsx'.format(index+1))
                try:
                    # 尝试保存 DataFrame
                    df_new = pd.DataFrame([row.tolist()], columns=columns_list)
                    df_new.to_excel(output_file, index=False)
                except Exception as e:
                    # 处理错误
                    print("An error occurred while saving the file:", e)

                

elif filename.endswith(".csv"):
    df = pd.read_csv(input_file)

        # 获取所有列名
    columns = df.columns

    # 将列名转换为列表
    columns_list = columns.tolist()

    
    if df.empty:
        print("打开文件为空")

    
    else:
        for index, row in df.iterrows():
            # print(len(row))
        # Create DataFrame
                
            df_new = pd.DataFrame(columns=columns_list)
            df_new.loc[0] = row.tolist()
        
        # Write DataFrame to new file

            output_file = os.path.join(data_dir, '{}.csv'.format(index+1))

            try:
                # 尝试保存 DataFrame
                df_new.to_csv(output_file, index=False)
            except Exception as e:
                print("An error occurred while saving the file:", e)                


    
