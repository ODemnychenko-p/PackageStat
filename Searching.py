import os
import json
import xlsxwriter

# path = r"E:\Demnichenko\Tasks\LiS\Content from UE4\MFS\Game"
#
# #MaterialExpressionDynamicTexture
# dynamic_mat_list = []
# for d,s,f in os.walk(path):
#     if f:
#         for file in f:
#             with open(os.path.join(d, file), 'r') as my_list:
#                 for string in my_list:
#                     if r"/Engine/Functions/Engine_MaterialFunctions02/WorldPositionOffset/Wind.Wind" in string:
#                         dynamic_mat_list.append(file)
#                         break
#
# for item in dynamic_mat_list:
#     print(item)
class Searching:
    def __init__(self):
        self.meshes_path = r'E:\Demnichenko\Tasks\LiS\Content from UE4\Meshes'
    def getMeshes(self):
        wb = xlsxwriter.Workbook("StaticMeshesList.xlsx")
        ws = wb.add_worksheet("Static Meshes")
        counter = 0
        form = wb.add_format()
        form.set_bg_color("#de8a8a")
        for d, s, f in os.walk(self.meshes_path):
            if f:
                path_name = d.replace(self.meshes_path, "")
                ws.write(counter, 0, path_name, form)
                counter += 1
                for file_name in f:
                    ws.write(counter, 0, file_name)
                    counter += 1
        wb.close()
a = Searching()
a.getMeshes()