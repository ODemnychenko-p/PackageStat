import os
pack_path = "D:/SVN/13.09.2017-15.24.24-LiS_TransferEP1_5-svn-martynyuk-r-8171/ChunkInstall/IOS/Episode"
unpacker_path = "D:/SVN/LiS_Production/Dev/UnrealEngine-4.15.1/Engine/Binaries/Win64"

for dir, subdir, files in os.walk(pack_path):
    for f in files:
        os.system("{0}/UnrealPak.exe {1} -Extract {2}".format(unpacker_path, os.path.join(dir, f), os.path.join(dir, f.replace(".pak", ""))))