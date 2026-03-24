# 常见问题排查 (Troubleshooting)

---

## 🔴 安装类问题

### 问题：`latex` 命令找不到
```
FileNotFoundError: [Errno 2] No such file or directory: 'latex'
```
**解决**：需要安装 LaTeX 发行版
```bash
# macOS（使用 MacTeX）
brew install --cask mactex

# 或安装更轻量的 BasicTeX
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install collection-fontsrecommended
```

### 问题：`ffmpeg` 找不到
```
FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'
```
**解决**：
```bash
# macOS
brew install ffmpeg

# 或通过 conda
conda install -c conda-forge ffmpeg
```

---

## 🟡 渲染类问题

### 问题：渲染后找不到文件
**说明**：输出文件默认保存在 `media/videos/<文件名>/<质量>/` 目录  
**解决**：使用 `-p` 参数自动用播放器打开，或手动查找 `media/` 下的文件

### 问题：动画运行很慢
**原因**：高质量模式（`-qh`）渲染耗时长  
**解决**：开发时使用 `-ql`（低质量）或 `-qm`（中质量）

### 问题：LaTeX 渲染出现乱码/方块
**原因**：字体不支持中文字符  
**解决**：改用 `Text()` 类显示中文（不依赖 LaTeX）
```python
# ❌ 中文 LaTeX 可能出问题
Tex("你好世界")

# ✅ 使用 Text 类
Text("你好世界")
```

---

## 🟢 代码类问题

### 问题：`AttributeError: 'NoneType' object has no attribute...`
**可能原因**：动画对象未正确初始化  
**解决**：确认 `construct()` 中所有对象都已通过 `self.add()` 或 `self.play()` 添加到场景

### 问题：`ValueError: z coordinate must be 0 for 2D scenes`
**原因**：在普通 `Scene` 中使用了 3D 坐标  
**解决**：将 3D 场景改继承 `ThreeDScene`
```python
class My3DScene(ThreeDScene):  # 而不是 Scene
    def construct(self):
        pass
```

---

*遇到新问题请在此处补充记录*
