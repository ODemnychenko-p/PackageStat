import os
import json

class Ue4NameConvantion:
    def __init__(self):
        self.prefixes_by_type = {
                            'Blueprint' : 'BP_',
                            'Skeletal Mesh' : 'SK_',
                            'Static Mesh' : 'SM_',
                            'Apex Destructible Asset' : 'AD_',
                            'Apex Cloth Asset' : ' AC_',
                            'Morph Target' : 'MT_',
                            'Speed Tree' : 'St_',
                            'Particle System' : 'PS_',
                            'Lens Flare' : 'LF_',
                            'Vector Field' : 'VF_',
                            'Sound' : 'S_',
                            'Sound Cue' : 'SC_',
                            'Material' : 'MT_', #original M_
                            'Material Instance' : 'MI_',
                            'Material Instance Time Varying' : 'MITV_',
                            'Material Function' : 'MF_',
                            'Material Parameter Collection' : 'MPC_',
                            'Texture' : 'T_',
                            'Sprite' : 'SP_',
                            'Sprite Sheet' : 'SS_',
                            'Texture Cube' : 'TC_',
                            'Render Target' : 'RT_',
                            'Physical Material' : 'PM_',
                            'All Assets' : ''
                        }

    def getPrefix(self, prefixName):
        return self.prefixes_by_type.get(prefixName, False)
class Filter:
    def __init__(self, asset_type = 'All Assets', size_range = 0):
        self.asset_type = asset_type
        self.size_range = size_range
        self.filtered_by_size = []
        self.filtered_by_type = []

    def filtering(self, assetName, assetPath, assetSize):
        if '\\Characters\\' in assetPath:
        # if assetName.startswith(Ue4NameConvantion().getPrefix(self.asset_type)):
            self.filtered_by_type.append({'name' : assetName, 'path' : assetPath, 'size' : assetSize})
            if assetSize > self.size_range:
                self.filtered_by_size.append({'name' : assetName, 'path' : assetPath, 'size' : assetSize})
    def getFilteredAssetsSize(self):
        return sum([item[key] for item in self.filtered_by_type for key in item if key == 'size'])
    def getFilteredAssetsBySizeCount(self):
        return len(self.filtered_by_size)

class sizes:
    def __init__(self):
        self.path = r"D:\SVN\NBAPlaygrounds2\Builds\IOS\17.12.2018\IOS\pak\nbaplaygrounds2-ios\NBAPlaygrounds2\Content"

        self.directory_size = 0
        self.file_size = 0

        self.filter = Filter('Material')

    def path_to_dict(self, path):
        d = {'name': os.path.basename(path)}
        if os.path.isdir(path):
            d['type'] = "directory"
            d['size'] = 0
            d['children'] = []
            for p, sd, f in os.walk(path):
                if ".DS_Store" in f:
                    f.remove('.DS_Store')
                if p != path:
                    break
                if sd:
                    for x in sd:
                        d['children'].append(self.path_to_dict(os.path.join(p, x)))
                if f:
                    for k in f:
                        d['children'].append(self.path_to_dict(os.path.join(p, k)))
                        d['size'] += self.file_size
                        self.directory_size += self.file_size
                        self.file_size = 0
                else:
                    d['size'] += self.directory_size
                break
        else:
            d['size'] = self.file_size = os.path.getsize(path) / 1000000
            d['type'] = "file"
            self.filter.filtering(d['name'], os.path.dirname(path), d['size'])
        return d

a = sizes()
a.path_to_dict(a.path)
print("Totals {0}s size: {1}\nCount filtered {0}s by size: {2}\nFiltered {0}s by size: {3}".format(a.filter.asset_type,
                                                                                                  a.filter.getFilteredAssetsSize(),
                                                                                                  a.filter.getFilteredAssetsBySizeCount(),
                                                                                                  json.dumps(a.filter.filtered_by_size, indent=2)
                                                                                                  ))
