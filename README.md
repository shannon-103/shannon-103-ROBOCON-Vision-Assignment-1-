# ROBOCON-Vision-Assignment-1




##1.System Information

代码：
```bash
(base) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-Assignment
-1/cpp$ cat /etc/os-release
uname -r
lscpu
lspci | grep -Ei 'vga|3d|display'
lspci -k | grep -EA3 'VGA|3D|Display'
echo "$XDG_SESSION_TYPE"
echo "$DISPLAY"
echo "$WAYLAND_DISPLAY"
nvidia-smi
PRETTY_NAME="Ubuntu 24.04.4 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.4 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=noble
LOGO=ubuntu-logo
7.0.0-34-generic
架构：                       x86_64
  CPU 运行模式：             32-bit, 64-bit
  Address sizes:             42 bits physical, 48 bits virtual
  字节序：                   Little Endian
CPU:                         18
  在线 CPU 列表：            0-17
厂商 ID：                    GenuineIntel
  型号名称：                 Intel(R) Core(TM) Ultra 7 251HX
    CPU 系列：               6
    型号：                   198
    每个核的线程数：         1
    每个座的核数：           18
    座：                     1
    步进：                   2
    CPU(s) scaling MHz:      36%
    CPU 最大 MHz：           5100.0000
    CPU 最小 MHz：           800.0000
    BogoMIPS：               6528.00
    标记：                   fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pg
                             e mca cmov pat pse36 clflush dts acpi mmx fxsr sse 
                             sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm cons
                             tant_tsc art arch_perfmon pebs bts rep_good nopl xt
                             opology nonstop_tsc cpuid aperfmperf tsc_known_freq
                              pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm
                             2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 
                             x2apic movbe popcnt tsc_deadline_timer aes xsave av
                             x f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault
                              ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flex
                             priority ept vpid ept_ad fsgsbase tsc_adjust bmi1 a
                             vx2 smep bmi2 erms invpcid rdt_a rdseed adx smap cl
                             flushopt clwb intel_pt sha_ni xsaveopt xsavec xgetb
                             v1 xsaves split_lock_detect user_shstk avx_vnni lam
                              wbnoinvd dtherm ida arat pln pts hwp hwp_notify hw
                             p_act_window hwp_epp hwp_pkg_req hfi vnmi umip pku 
                             ospke waitpkg gfni vaes vpclmulqdq rdpid bus_lock_d
                             etect movdiri movdir64b fsrm md_clear serialize arc
                             h_lbr ibt flush_l1d arch_capabilities
Virtualization features:     
  虚拟化：                   VT-x
Caches (sum of all):         
  L1d:                       672 KiB (18 instances)
  L1i:                       1.1 MiB (18 instances)
  L2:                        30 MiB (9 instances)
  L3:                        30 MiB (1 instance)
NUMA:                        
  NUMA 节点：                1
  NUMA 节点0 CPU：           0-17
Vulnerabilities:             
  Gather data sampling:      Not affected
  Ghostwrite:                Not affected
  Indirect target selection: Not affected
  Itlb multihit:             Not affected
  L1tf:                      Not affected
  Mds:                       Not affected
  Meltdown:                  Not affected
  Mmio stale data:           Not affected
  Old microcode:             Not affected
  Reg file data sampling:    Not affected
  Retbleed:                  Not affected
  Spec rstack overflow:      Not affected
  Spec store bypass:         Mitigation; Speculative Store Bypass disabled via p
                             rctl
  Spectre v1:                Mitigation; usercopy/swapgs barriers and __user poi
                             nter sanitization
  Spectre v2:                Mitigation; Enhanced / Automatic IBRS; IBPB conditi
                             onal; PBRSB-eIBRS Not affected; BHI BHI_DIS_S
  Srbds:                     Not affected
  Tsa:                       Not affected
  Tsx async abort:           Not affected
  Vmscape:                   Mitigation; IBPB before exit to userspace
00:02.0 VGA compatible controller: Intel Corporation Arrow Lake-U [Intel Graphics] (rev 06)
02:00.0 VGA compatible controller: NVIDIA Corporation Device 2d59 (rev a1)
80:14.5 Non-VGA unclassified device: Intel Corporation Device 7f2f (rev 10)
00:02.0 VGA compatible controller: Intel Corporation Arrow Lake-U [Intel Graphics] (rev 06)
	Subsystem: Lenovo Device 8015
	Kernel driver in use: i915
	Kernel modules: i915, xe
--
02:00.0 VGA compatible controller: NVIDIA Corporation Device 2d59 (rev a1)
	Subsystem: Lenovo Device 8015
	Kernel driver in use: nvidia
	Kernel modules: nvidiafb, nouveau, nvidia_drm, nvidia
--
80:14.5 Non-VGA unclassified device: Intel Corporation Device 7f2f (rev 10)
	Subsystem: Lenovo Device 3d73
80:15.0 Serial bus controller: Intel Corporation Device 7f4c (rev 10)
	Subsystem: Lenovo Device 3d73
x11
:1

Sun Sep 27 20:33:03 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 595.84                 Driver Version: 595.84         CUDA Version: 13.2     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 5060 ...    Off |   00000000:02:00.0 Off |                  N/A |
| N/A   39C    P4             10W /   50W |      15MiB /   8151MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            2500      G   /usr/lib/xorg/Xorg                        4MiB |
+-----------------------------------------------------------------------------------------+
```


##2.Python Project A

本项目基于 OpenCV，实现摄像头实时读取、图像灰度化、轮廓检测，同时实时保存原始彩色摄像头视频。
运行后同时弹出三个窗口：原始图像、灰度图像、轮廓处理图像。


所有操作均使用独立 Conda 虚拟环境，严格遵循项目 Python 版本约束。

```bash
conda activate proj_a
pip install opencv‑python
python --version
which python
python camera.py
```

代玛：
```bash
(base) shr@shr-Legion-Y7000P-IAX10:~$ conda activate proja
(proja) shr@shr-Legion-Y7000P-IAX10:~$ pip install opencv-python
Collecting opencv-python
  Downloading opencv_python-5.0.0.93-cp37-abi3-manylinux_2_28_x86_64.whl.metadata (19 kB)
Collecting numpy>=2 (from opencv-python)
  Downloading numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Downloading opencv_python-5.0.0.93-cp37-abi3-manylinux_2_28_x86_64.whl (73.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 73.8/73.8 MB 1.6 MB/s  0:00:46
Downloading numpy-2.4.6-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.9/16.9 MB 1.1 MB/s  0:00:15
Installing collected packages: numpy, opencv-python
Successfully installed numpy-2.4.6 opencv-python-5.0.0.93
(proja) shr@shr-Legion-Y7000P-IAX10:~$ python --version
Python 3.11.16
(proja) shr@shr-Legion-Y7000P-IAX10:~$ which python
/home/shr/miniconda3/envs/proja/bin/python
(proja) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-Assignmen
t-1/python-a$ python camera.py
QFontDatabase: Cannot find font directory /home/shr/miniconda3/envs/proja/lib/python3.11/site-packages/cv2/qt/fonts.
Note that Qt no longer ships fonts. Deploy some (from https://dejavu-fonts.github.io/ for example) or switch to fontconfig.
QFontDatabase: Cannot find font directory /home/shr/miniconda3/envs/proja/lib/python3.11/site-packages/cv2/qt/fonts.
Note that Qt no longer ships fonts. Deploy some (from https://dejavu-fonts.github.io/ for example) or switch to fontconfig.
QFontDatabase: Cannot find font directory /home/shr/miniconda3/envs/proja/lib/python3.11/site-packages/cv2/qt/fonts.
Note that Qt no longer ships fonts. Deploy some (from https://dejavu-fonts.github.io/ for example) or switch to fontconfig.
QFontDatabase: Cannot find font directory /home/shr/miniconda3/envs/proja/lib/python3.11/site-packages/cv2/qt/fonts.
Note that Qt no longer ships fonts. Deploy some (from https://dejavu-fonts.github.io/ for example) or switch to fontconfig.
QFontDatabase: Cannot find font directory /home/shr/miniconda3/envs/proja/lib/python3.11/site-packages/cv2/qt/fonts.
Note that Qt no longer ships fonts. Deploy some (from https://dejavu-fonts.github.io/ for example) or switch to fontconfig.
```





## 3、Process Observation
运行`python camera.py`，程序会调用`os.getpid()`打印自身PID，运行期间保持程序持续运行。使用`Ctrl + Alt + T`打开第二个独立终端，在新终端执行进程查询。

**使用pgrep管道**
```bash
sudo apt update
sudo apt install htop
htop
ps -o pid,ppid,cmd,%cpu,%mem,etime -p $(pgrep -f camera.py) 
```





## 4、Python Project B

本实验为 project_b离线视频分析任务，不使用 OpenCV，全程基于 imageio、numpy、scikit-image 完成图像处理。程序读取 project_a生成的原始视频文件 `raw_capture.mp4`，逐帧完成灰度转换、Canny边缘检测、帧间运动区域计算，并将 **原始画面、边缘特征、运动变化区域** 三帧横向拼接，最终输出合成视频 `advanced_analysis.mp4` 保存至本地磁盘。

代码：
```bash
(base) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-As
signment-1/python_b$ conda create -n projb python=3.13
2 channel Terms of Service accepted
WARNING: A conda environment already exists at '/home/shr/miniconda3/envs/projb'

Remove existing environment?
This will remove ALL directories contained within this specified prefix directory, including any other conda environments.

 (y/[n])? y

Channels:
 - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
 - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
 - defaults
Platform: linux-64
Collecting package metadata (repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
    current version: 26.7.1
    latest version: 26.7.2

Please update conda by running

    $ conda self update



## Package Plan ##

  environment location: /home/shr/miniconda3/envs/projb

  added / updated specs:
    - python=3.13


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    libmpdec-4.0.1             |       h47b2149_0          88 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    packaging-26.3             |  py313h06a4308_0         380 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    python-3.13.15             |h9631c4f_102_cp313        31.9 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    python_abi-3.13            |          4_cp313           5 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    setuptools-83.0.0          |  py313h06a4308_0         1.6 MB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    wheel-0.47.0               |  py313h06a4308_0          73 KB  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ------------------------------------------------------------
                                           Total:        34.0 MB

The following NEW packages will be INSTALLED:

  _libgcc_mutex      anaconda/pkgs/main/linux-64::_libgcc_mutex-0.1-main 
  _openmp_mutex      anaconda/pkgs/main/linux-64::_openmp_mutex-5.1-52_gnu 
  bzip2              anaconda/pkgs/main/linux-64::bzip2-1.0.8-h5eee18b_6 
  ca-certificates    anaconda/pkgs/main/linux-64::ca-certificates-2026.8.13-h06a4308_0 
  ld_impl_linux-64   anaconda/pkgs/main/linux-64::ld_impl_linux-64-2.44-h9e0c5a2_3 
  libexpat           anaconda/pkgs/main/linux-64::libexpat-2.8.5-h7354ed3_1 
  libffi             anaconda/pkgs/main/linux-64::libffi-3.4.8-h06d3fd0_3 
  libgcc             anaconda/pkgs/main/linux-64::libgcc-15.2.0-h69a1729_8 
  libgcc-ng          anaconda/pkgs/main/linux-64::libgcc-ng-15.2.0-h166f726_8 
  libmpdec           anaconda/pkgs/main/linux-64::libmpdec-4.0.1-h47b2149_0 
  libstdcxx          anaconda/pkgs/main/linux-64::libstdcxx-15.2.0-h39759b7_8 
  libuuid            anaconda/pkgs/main/linux-64::libuuid-1.41.5-h5eee18b_0 
  libxcb             anaconda/pkgs/main/linux-64::libxcb-1.17.0-h9b100fa_0 
  libzlib            anaconda/pkgs/main/linux-64::libzlib-1.3.2-h47b2149_0 
  ncurses            anaconda/pkgs/main/linux-64::ncurses-6.6-hfaaeb4e_0 
  openssl            anaconda/pkgs/main/linux-64::openssl-3.5.8-h1b28b03_0 
  packaging          anaconda/pkgs/main/linux-64::packaging-26.3-py313h06a4308_0 
  pip                anaconda/pkgs/main/noarch::pip-26.2.1-pyhc872135_0 
  pthread-stubs      anaconda/pkgs/main/linux-64::pthread-stubs-0.3-h47b2149_2 
  python             anaconda/pkgs/main/linux-64::python-3.13.15-h9631c4f_102_cp313 
  python_abi         anaconda/pkgs/main/linux-64::python_abi-3.13-4_cp313 
  readline           anaconda/pkgs/main/linux-64::readline-8.3-hc2a1206_0 
  setuptools         anaconda/pkgs/main/linux-64::setuptools-83.0.0-py313h06a4308_0 
  sqlite             anaconda/pkgs/main/linux-64::sqlite-3.53.4-h795bf6d_0 
  tk                 anaconda/pkgs/main/linux-64::tk-8.6.15-h54e0aa7_0 
  tzdata             anaconda/pkgs/main/noarch::tzdata-2026c-he532380_0 
  wheel              anaconda/pkgs/main/linux-64::wheel-0.47.0-py313h06a4308_0 
  xorg-libx11        anaconda/pkgs/main/linux-64::xorg-libx11-1.8.13-h65de747_0 
  xorg-libxau        anaconda/pkgs/main/linux-64::xorg-libxau-1.0.12-h9b100fa_0 
  xorg-libxdmcp      anaconda/pkgs/main/linux-64::xorg-libxdmcp-1.1.5-h9b100fa_0 
  xorg-xorgproto     anaconda/pkgs/main/linux-64::xorg-xorgproto-2025.1-h47b2149_0 
  xz                 anaconda/pkgs/main/linux-64::xz-5.8.4-h140a991_0 
  zlib               anaconda/pkgs/main/linux-64::zlib-1.3.2-h47b2149_0 


Proceed ([y]/n)? y


Downloading and Extracting Packages:
                                                                       
Preparing transaction: done                                            
Verifying transaction: done                                            
Executing transaction: done                                            
#                                                                      
# To activate this environment, use                                    
#
#     $ conda activate projb
#
# To deactivate an active environment, use
#
#     $ conda deactivate

WARNING conda.conda_pypi.main:notify_externally_managed_future(156): 
  Did you know? You can install many PyPI packages with conda
  using the conda-pypi beta. Get started:
    https://docs.conda.io/projects/conda/en/stable/new-features.html

(base) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-As
signment-1/python_b$ conda env list

# conda environments:
#
# * -> active
# + -> frozen
base                 *   /home/shr/miniconda3
proja                    /home/shr/miniconda3/envs/proja
projb                    /home/shr/miniconda3/envs/projb
rcvi                     /home/shr/miniconda3/envs/rcvi

(base) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-As
signment-1/python_b$ conda projb list
usage: conda [-h] [-v] [--no-plugins] [-V] COMMAND ...
conda: error: argument COMMAND: invalid choice: 'projb' (choose from 'activate', 'check', 'clean', 'commands', 'compare', 'config', 'content-trust', 'create', 'deactivate', 'doctor', 'env', 'export', 'index', 'info', 'init', 'install', 'list', 'menuinst', 'notices', 'package', 'pypi', 'remove', 'rename', 'repoquery', 'run', 'search', 'self', 'token', 'tos', 'uninstall', 'update', 'upgrade')
(base) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-As
signment-1/python_b$ conda list -n projb
# packages in environment at /home/shr/miniconda3/envs/projb:
#
# Name                     Version          Build               Channel
_libgcc_mutex              0.1              main                https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
_openmp_mutex              5.1              52_gnu              https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
bzip2                      1.0.8            h5eee18b_6          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
ca-certificates            2026.8.13        h06a4308_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
ld_impl_linux-64           2.44             h9e0c5a2_3          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
libexpat                   2.8.5            h7354ed3_1          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
libffi                     3.4.8            h06d3fd0_3          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
libgcc                     15.2.0           h69a1729_8          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
libgcc-ng                  15.2.0           h166f726_8          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
libmpdec                   4.0.1            h47b2149_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
libstdcxx                  15.2.0           h39759b7_8          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
libuuid                    1.41.5           h5eee18b_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
libxcb                     1.17.0           h9b100fa_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
libzlib                    1.3.2            h47b2149_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
ncurses                    6.6              hfaaeb4e_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
openssl                    3.5.8            h1b28b03_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
packaging                  26.3             py313h06a4308_0     https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
pip                        26.2.1           pyhc872135_0        https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
pthread-stubs              0.3              h47b2149_2          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
python                     3.13.15          h9631c4f_102_cp313  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
python_abi                 3.13             4_cp313             https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
readline                   8.3              hc2a1206_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
setuptools                 83.0.0           py313h06a4308_0     https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
sqlite                     3.53.4           h795bf6d_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
tk                         8.6.15           h54e0aa7_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
tzdata                     2026c            he532380_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
wheel                      0.47.0           py313h06a4308_0     https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
xorg-libx11                1.8.13           h65de747_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
xorg-libxau                1.0.12           h9b100fa_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
xorg-libxdmcp              1.1.5            h9b100fa_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
xorg-xorgproto             2025.1           h47b2149_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
xz                         5.8.4            h140a991_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
zlib                       1.3.2            h47b2149_0          https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
(base) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-As
signment-1/python_b$ conda activate projb
(projb) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-A
ssignment-1/python_b$ python --version
Python 3.13.15
(projb) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-A
ssignment-1/python_b$ pip install "numpy>=2.0,<3.0" "imageio>=2.36,<3.0" "imageio-ffmpeg>=0.5,<1.0" "scikit-image>=0.24,<0.27"
Collecting numpy<3.0,>=2.0
  Downloading numpy-2.5.3-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Collecting imageio<3.0,>=2.36
  Downloading imageio-2.37.4-py3-none-any.whl.metadata (9.6 kB)
Collecting imageio-ffmpeg<1.0,>=0.5
  Downloading imageio_ffmpeg-0.6.0-py3-none-manylinux2014_x86_64.whl.metadata (1.5 kB)
Collecting scikit-image<0.27,>=0.24
  Downloading scikit_image-0.26.0-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (15 kB)
Collecting pillow>=8.3.2 (from imageio<3.0,>=2.36)
  Downloading pillow-12.3.0-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (9.1 kB)
Collecting scipy>=1.11.4 (from scikit-image<0.27,>=0.24)
  Downloading scipy-1.18.1-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (62 kB)
Collecting networkx>=3.0 (from scikit-image<0.27,>=0.24)
  Downloading networkx-3.7-py3-none-any.whl.metadata (6.7 kB)
Collecting tifffile>=2022.8.12 (from scikit-image<0.27,>=0.24)
  Downloading tifffile-2026.9.20-py3-none-any.whl.metadata (34 kB)
Requirement already satisfied: packaging>=21 in /home/shr/miniconda3/envs/projb/lib/python3.13/site-packages (from scikit-image<0.27,>=0.24) (26.3)
Collecting lazy-loader>=0.4 (from scikit-image<0.27,>=0.24)
  Downloading lazy_loader-0.6-py3-none-any.whl.metadata (6.0 kB)
Downloading numpy-2.5.3-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.7/16.7 MB 898.0 kB/s  0:00:18
Downloading imageio-2.37.4-py3-none-any.whl (318 kB)
Downloading imageio_ffmpeg-0.6.0-py3-none-manylinux2014_x86_64.whl (29.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 29.5/29.5 MB 2.5 MB/s  0:00:11
Downloading scikit_image-0.26.0-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (13.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 13.7/13.7 MB 2.5 MB/s  0:00:05
Downloading lazy_loader-0.6-py3-none-any.whl (8.8 kB)
Downloading networkx-3.7-py3-none-any.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 2.5 MB/s  0:00:00
Downloading pillow-12.3.0-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (6.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.9/6.9 MB 2.5 MB/s  0:00:02
Downloading scipy-1.18.1-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (35.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 35.3/35.3 MB 2.4 MB/s  0:00:14
Downloading tifffile-2026.9.20-py3-none-any.whl (275 kB)
Installing collected packages: pillow, numpy, networkx, lazy-loader, imageio-ffmpeg, tifffile, scipy, imageio, scikit-image
Successfully installed imageio-2.37.4 imageio-ffmpeg-0.6.0 lazy-loader-0.6 networkx-3.7 numpy-2.5.3 pillow-12.3.0 scikit-image-0.26.0 scipy-1.18.1 tifffile-2026.9.20
(projb) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-A
ssignment-1/python_b$ python analyze_video.py \
  --input /home/shr/桌面/RCassignment/ROBOCON-Vision-Assignment-1/assets/python_a/raw_capture.mp4 \--output /home/shr/桌面/RCassignment/ROBOCON-Vision-Assignment-1/assets/python_b/advanced_analysis.mp4
```

project_b成功:
✅处理完成！输出文件保存在：/home/shr/桌面/RCassignment/ROBOCON-Vision-Assignment-1/assets/python_b/advanced_analysis.mp4



[project_a ]
env:proja
py:3.11
[project_b ]
env:projb
py:3.13


为什么Project A与Project B建议使用两套独立Conda虚拟环境:

从程序运行层面来说，若两个项目的全部第三方库版本要求完全兼容，将二者置于同一个虚拟环境中运行，代码也可以正常执行。但在工程开发场景下，依然推荐为两个项目分配相互独立的虚拟环境，主要原因分为三点：

第一，用来规避软件包的版本冲突。同一个Conda环境内部，同一个软件仅能够保存一个版本。在实际开发中，不同项目对库的版本往往会提出不一样的要求，例如新项目需要使用新版本OpenCV调用全新接口，而历史遗留代码只能在旧版本库下正常工作。共用一套环境时，升级或者降级软件包，就会直接造成另一套程序无法运行。使用隔离环境，不同项目可以保留自身所需的软件版本，互不干扰。

第二，可以防止环境被意外污染。当我们在其中一个项目中安装调试各类算法工具、扩展库的时候，新增软件的依赖关系有可能连锁改动numpy、OpenCV这类基础组件。会出现程序本身一行代码都没有修改，仅仅因为安装了别的工具，就发生程序异常崩溃的现象。将环境分开之后，在一个环境内的所有安装操作，都不会对另一个项目的依赖库产生任何改动，保障程序运行状态稳定。

第三，便于项目交付与团队复现。如果多个项目混杂在同一套环境，环境中会积攒大量临时安装的冗余工具，很难区分哪些是项目运行必不可少的依赖，哪些是调试使用的无关包。拆分环境之后，我们可以整理出每个项目专属的依赖清单，队友拿到清单就可以快速搭建出完全一致的运行环境，复现项目运行效果。

conclusion:本次作业要求划分两套独立环境，并不是程序运行的硬性需要，核心目的是训练基础工程思维，熟悉虚拟环境的隔离机制，提前建立起符合机器人团队开发习惯的工程意识，为之后RoboCon项目开发做好铺垫。





##5.C++ Manual Build

命令：
```bash
(base) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-Assignment
-1/cpp$ g++ src/main.cpp src/transform.cpp -o video_proc -std=c++17 -I./include -I/usr/include/eigen3 `pkg-config --cflags --libs opencv4`
(base) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-Assignment
-1/cpp$ ./video_proc '/home/shr/桌面/RCassignment/ROBOCON-Vision-Assignment-1/assets/python_a/raw_capture.mp4' '/home/shr/桌面/RCassignment/ROBOCON-Vision-Assignment-1/assets/cpp/out_video.mp4'
Input: /home/shr/桌面/RCassignment/ROBOCON-Vision-Assignment-1/assets/python_a/raw_capture.mp4
Output: /home/shr/桌面/RCassignment/ROBOCON-Vision-Assignment-1/assets/cpp/out_video.mp4
Frames: 10219
Mean scene luma: 121.54
Panels: original | Otsu binary | Canny edges
```

1. -I的作用：-I用来指定编译器搜索头文件的文件夹路径。程序中通过#include引入头文件时，编译器会到‑I指定的目录中进行查找。本项目通过该参数定位项目内的transform.hpp以及Eigen库的头文件，缺少该参数就会出现找不到头文件的编译错误。

2. 为什么transform.hpp不单独作为一个cpp文件编译：transform.hpp属于头文件，主要承担函数、数据结构的声明工作，用来定义程序的接口，函数的具体实现写在transform.cpp源文件当中。头文件会被源代码通过#include引入参与预处理，不需要直接交给编译器编译，单独编译头文件会引发重复定义等问题。

3. 为什么只写main.cpp往往无法得到完整程序：main.cpp只包含程序主流程的代码，项目里图像处理相关函数的实现全部写在transform.cpp文件中。如果只编译main.cpp，编译器能够看到函数声明，但是找不到函数的实际实现，链接阶段会报函数未定义错误，无法组装成完整程序，因此需要将所有cpp源文件一同参与编译。

4. 编译成功后产生的文件是什么：编译完成后会生成名为video_proc的二进制可执行文件。该文件脱离源代码，可以直接在终端运行，读取视频文件，执行我们编写的图像处理逻辑，并输出处理完成的视频结果。





##6.CMake Build


CMakeLists.txt完整内容
```cmake
cmake_minimum_required(VERSION 3.22)

project(video_proc LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)
include_directories("/usr/include/eigen3")

add_executable(video_process main.cpp)
target_link_libraries(video_process PRIVATE ${OpenCV_LIBS})
```


命令：
```bash
(base) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-Assignment
-1/cpp$ cmake -S . -B build
-- The C compiler identification is GNU 13.3.0
-- The CXX compiler identification is GNU 13.3.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found OpenCV: /usr (found version "4.6.0") 
-- Configuring done (0.4s)
-- Generating done (0.0s)
-- Build files have been written to: /home/shr/桌面/RCassignment/ROBOCON-Vision-Assignment-1/cpp/build
(base) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-Assignment
-1/cpp$ cmake --build build
[ 33%] Building CXX object CMakeFiles/video_process.dir/src/main.cpp.o
[ 66%] Building CXX object CMakeFiles/video_process.dir/src/transform.cpp.o
[100%] Linking CXX executable video_process
[100%] Built target video_process
(base) shr@shr-Legion-Y7000P-IAX10:~/桌面/RCassignment/ROBOCON-Vision-Assignment
-1/cpp$ /home/shr/桌面/RCassignment/ROBOCON-Vision-Assignment-1/cpp/video_proc1 '/home/shr/桌面/RCassignment/ROBOCON-Vision-Assignment-1/assets/python_a/raw_capture.mp4' /home/shr/桌面/RCassignment/ROBOCON-Vision-Assignment-1/assets/cpp/out.mp4
Input: /home/shr/桌面/RCassignment/ROBOCON-Vision-Assignment-1/assets/python_a/raw_capture.mp4
Output: /home/shr/桌面/RCassignment/ROBOCON-Vision-Assignment-1/assets/cpp/out.mp4
Frames: 10219
Mean scene luma: 121.54
Panels: original | Otsu binary | Canny edges
```


手工g++和CMAKE的关系:
g++ 是编译器，真正干活翻译C++代码；CMake根本不编译代码，它是一个生成编译脚本的工具。

This modification was written inside dev-develop branch
