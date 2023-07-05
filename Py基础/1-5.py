'''
为 Windows 创建虚拟环境
    py -3 -m venv .venv
    .venv\scripts\activate

适用于 macOS/Linux 的虚拟环境创建
    python3 -m venv .venv
    source .venv/bin/activate

终端窗口中键入以停用虚拟环境。deactivate


安装软件包

# Don't use with Anaconda distributions because they include matplotlib already.

# macOS
    python3 -m pip install matplotlib

# Windows (may require elevation)
    python -m pip install matplotlib

# Linux (Debian)
    apt-get install python3-tk
    python3 -m pip install matplotlib



    sudo apt-get update
    sudo apt install libgl1-mesa-glx
    sudo apt-get install libxcb-xinerama0
'''



#print("Hi,Python!")
#name=input("请输入姓名：")
#print(name)

# print(input("请输入你的名字："))

# print（5+3）
for i in range(5):
    print(i)
