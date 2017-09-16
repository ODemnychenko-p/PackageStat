import os
import json


path = r"E:\Demnichenko\Tasks\LiS\Content from UE3\Particles"

#MaterialExpressionDynamicTexture
dynamic_mat_list = []
for d,s,f in os.walk(path):
    if f:
        for file in f:
            with open(os.path.join(d, file), 'r') as my_list:
                for string in my_list:
                    if 'EPET_Kismet' in string:
                        dynamic_mat_list.append(file)
                        break

for item in dynamic_mat_list:
    print(item)
