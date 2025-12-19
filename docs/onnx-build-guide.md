# ONNX 生态系统编译指导手册

> Version: 1.0
> Last Updated: 2025-12-18
> 适用平台: macOS (Intel/Apple Silicon), Linux, Windows

---

## 概述

本手册涵盖 ONNX 生态系统主要组件的编译安装问题及解决方案：

- **onnx**: ONNX 模型格式核心库
- **onnxoptimizer**: ONNX 模型优化器
- **onnxruntime**: ONNX 模型推理引擎
- **onnx-mlir**: ONNX 到 MLIR 编译器

---

## 快速诊断流程

```
遇到 ONNX 相关编译错误
         │
         ▼
    检查 CMake 版本
    cmake --version
         │
    ┌────┴────┐
    │         │
 >= 4.0    < 4.0
    │         │
    ▼         ▼
 设置环境变量   检查其他问题
 CMAKE_POLICY_VERSION_MINIMUM=3.5
```

---

## 环境要求

### macOS

| 组件 | 最低版本 | 推荐版本 | 检查命令 |
|------|----------|----------|----------|
| macOS | 11.0 (Big Sur) | 14.0+ | `sw_vers` |
| Xcode CLT | 12.0 | 15.0+ | `xcode-select -p` |
| CMake | 3.13 | 3.28+ | `cmake --version` |
| Python | 3.8 | 3.10-3.12 | `python3 --version` |
| protobuf | 3.20 | 4.x | `protoc --version` |

### 编译工具链

```bash
# 安装 Xcode Command Line Tools
xcode-select --install

# 安装 CMake (通过 Homebrew)
brew install cmake

# 安装 protobuf
brew install protobuf
```

---

## 常见错误及解决方案

### 错误 1: CMake 版本兼容性问题 (最常见)

**错误信息:**
```
CMake Error at third_party/onnx/CMakeLists.txt:2 (cmake_minimum_required):
  Compatibility with CMake < 3.5 has been removed from CMake.
```

**原因:** CMake 4.0+ 移除了对旧版本 cmake_minimum_required 声明的兼容性支持。

**解决方案:**

```bash
# 方案 A: 设置环境变量 (推荐，适用于 CMake 4.0+)
CMAKE_POLICY_VERSION_MINIMUM=3.5 pip install onnxoptimizer
CMAKE_POLICY_VERSION_MINIMUM=3.5 pip install onnx

# 方案 B: 使用 uv
CMAKE_POLICY_VERSION_MINIMUM=3.5 uv pip install onnxoptimizer

# 方案 C: 从源码编译时传递 CMake 参数
cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 ..
```

**永久配置 (可选):**
```bash
# 添加到 ~/.zshrc 或 ~/.bashrc
export CMAKE_POLICY_VERSION_MINIMUM=3.5
```

---

### 错误 2: PythonLibs 找不到

**错误信息:**
```
Could NOT find PythonLibs (missing: PYTHON_LIBRARIES)
```

**原因:** CMake 无法定位 Python 开发库。

**解决方案:**

```bash
# macOS with Homebrew Python
cmake -DPython_INCLUDE_DIR=$(python3 -c "import sysconfig; print(sysconfig.get_path('include'))") \
      -DPython_EXECUTABLE=$(which python3) \
      ..

# 或者指定完整路径
cmake -DPython3_EXECUTABLE=/opt/homebrew/bin/python3 \
      -DPython3_INCLUDE_DIR=/opt/homebrew/opt/python@3.12/Frameworks/Python.framework/Versions/3.12/include/python3.12 \
      ..
```

---

### 错误 3: Protobuf 版本冲突

**错误信息:**
```
no arm64 symbol for InternalMetadata::~InternalMetadata
```
或
```
protobuf version mismatch
```

**原因:** 系统存在多个 protobuf 版本，或 protobuf 版本不兼容。

**解决方案:**

```bash
# 方案 A: 使用项目内置 protobuf
cmake -DONNX_OPT_USE_SYSTEM_PROTOBUF=OFF ..

# 方案 B: 重新安装匹配版本的 protobuf
brew uninstall protobuf
brew install protobuf@3

# 方案 C: 清理并重新编译
pip cache purge
pip install --no-cache-dir onnx
```

---

### 错误 4: Apple Silicon (M1/M2/M3) 架构问题

**错误信息:**
```
building for macOS-x86_64 but attempting to link with file built for macOS-arm64
```

**解决方案:**

```bash
# 强制指定架构
cmake -DCMAKE_OSX_ARCHITECTURES=arm64 ..

# 或者对于通用二进制
cmake -DCMAKE_OSX_ARCHITECTURES="arm64;x86_64" ..

# pip 安装时
ARCHFLAGS="-arch arm64" pip install onnx
```

---

### 错误 5: C++ 编译器问题

**错误信息:**
```
use of overloaded operator '<<' is ambiguous
```

**解决方案:**

```bash
# 指定 C++ 编译器
cmake -DCMAKE_CXX_COMPILER=/usr/bin/clang++ \
      -DCMAKE_C_COMPILER=/usr/bin/clang \
      ..

# 或者指定 C++ 标准
cmake -DCMAKE_CXX_STANDARD=17 ..
```

---

### 错误 6: Git Submodule 问题

**错误信息:**
```
fatal: 无效的 gitfile 格式
```
或
```
CMake Error: The source directory does not contain a CMakeLists.txt file
```

**解决方案:**

```bash
# 从源码编译时，确保初始化所有子模块
git clone --recursive https://github.com/onnx/optimizer onnxoptimizer
cd onnxoptimizer

# 如果已经 clone，更新子模块
git submodule update --init --recursive
```

---

## 各组件安装指南

### onnx

```bash
# 标准安装
CMAKE_POLICY_VERSION_MINIMUM=3.5 pip install onnx

# 从源码安装
git clone --recursive https://github.com/onnx/onnx.git
cd onnx
CMAKE_POLICY_VERSION_MINIMUM=3.5 pip install -e .
```

### onnxoptimizer

```bash
# 标准安装
CMAKE_POLICY_VERSION_MINIMUM=3.5 pip install onnxoptimizer

# 从源码安装
git clone --recursive https://github.com/onnx/optimizer onnxoptimizer
cd onnxoptimizer
CMAKE_POLICY_VERSION_MINIMUM=3.5 pip install -e .
```

### onnxruntime

```bash
# 标准安装 (预编译二进制，推荐)
pip install onnxruntime

# Apple Silicon 优化版本
pip install onnxruntime-silicon  # 如果可用

# 从源码编译 (高级)
git clone --recursive https://github.com/microsoft/onnxruntime
cd onnxruntime
./build.sh --config Release --build_shared_lib --parallel \
           --cmake_extra_defines CMAKE_OSX_ARCHITECTURES=arm64
```

### onnx-mlir

```bash
# 参考官方文档: https://onnx.ai/onnx-mlir/BuildOnLinuxOSX.html
git clone --recursive https://github.com/onnx/onnx-mlir.git
cd onnx-mlir
mkdir build && cd build

# macOS 特定配置
cmake -DCMAKE_BUILD_TYPE=Release \
      -DMLIR_DIR=/path/to/llvm-project/build/lib/cmake/mlir \
      -DCMAKE_OSX_ARCHITECTURES=arm64 \
      ..

make -j$(sysctl -n hw.ncpu)
```

---

## 环境变量参考

| 变量名 | 用途 | 示例值 |
|--------|------|--------|
| `CMAKE_POLICY_VERSION_MINIMUM` | 覆盖 CMake 最低版本策略 | `3.5` |
| `CMAKE_OSX_ARCHITECTURES` | 指定目标架构 | `arm64` |
| `ARCHFLAGS` | macOS 编译架构标志 | `-arch arm64` |
| `ONNX_ML` | 启用 ONNX-ML 扩展 | `1` |
| `ONNX_NAMESPACE` | ONNX 命名空间 | `onnx` |
| `PROTOBUF_DIR` | Protobuf 安装路径 | `/opt/homebrew/opt/protobuf` |

---

## 故障排除检查清单

在提交 issue 或寻求帮助前，请收集以下信息：

```bash
# 1. 系统信息
sw_vers                          # macOS 版本
uname -m                         # 架构 (arm64/x86_64)

# 2. 工具链版本
cmake --version
python3 --version
clang --version | head -1
protoc --version

# 3. Python 环境
which python3
pip list | grep -E "onnx|protobuf|numpy"

# 4. 完整错误日志
pip install onnxoptimizer -v 2>&1 | tee build.log
```

---

## 常见场景速查

### 场景: 全新 Mac 安装 ONNX 生态

```bash
# 1. 安装依赖
brew install cmake protobuf

# 2. 设置环境变量
export CMAKE_POLICY_VERSION_MINIMUM=3.5

# 3. 安装 ONNX 组件
pip install onnx onnxoptimizer onnxruntime
```

### 场景: M1/M2/M3 Mac 编译问题

```bash
# 完整环境配置
export CMAKE_POLICY_VERSION_MINIMUM=3.5
export CMAKE_OSX_ARCHITECTURES=arm64
export ARCHFLAGS="-arch arm64"

# 然后安装
pip install onnxoptimizer
```

### 场景: 企业环境/无网络编译

```bash
# 1. 在有网络的机器下载源码和依赖
pip download onnxoptimizer --no-binary :all: -d ./packages

# 2. 传输到目标机器后
CMAKE_POLICY_VERSION_MINIMUM=3.5 pip install --no-index --find-links=./packages onnxoptimizer
```

---

## 参考资源

- [ONNX GitHub](https://github.com/onnx/onnx)
- [ONNX Optimizer GitHub](https://github.com/onnx/optimizer)
- [ONNX Runtime GitHub](https://github.com/microsoft/onnxruntime)
- [ONNX Runtime Build Guide](https://onnxruntime.ai/docs/build/inferencing.html)
- [ONNX-MLIR Build Guide](https://onnx.ai/onnx-mlir/BuildOnLinuxOSX.html)
- [CMake Policy Documentation](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html)

---

## 更新日志

| 日期 | 版本 | 变更 |
|------|------|------|
| 2025-12-18 | 1.0 | 初始版本，包含 CMake 4.x 兼容性解决方案 |

---

**End of ONNX Build Guide**
