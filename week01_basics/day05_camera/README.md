# Day 05: 摄像机与场景 (Camera and Scene)

> **核心目标**：理解 Manim 的“镜头”概念，掌握如何通过操作摄像机帧 (Camera Frame) 实现动态视角切换、缩放和追踪。

---

## 📸 核心原理解析

在普通的 `Scene` 中，摄像机捕捉的是一个固定的 14x8 个单位区域。要让摄像机动起来，我们需要使用 `MovingCameraScene`。

### 1. 摄像机帧 (Camera Frame)
`MovingCameraScene` 提供了一个名为 `self.camera.frame` 的特殊对象。它在本质上是一个 **`Rectangle` Mobject**。
- **平移 (Shift)**: `self.camera.frame.animate.shift(RIGHT)` 使镜头向右移。
- **缩放 (Scale)**: `self.camera.frame.animate.set_width(5)` 使视野宽度变为 5（原值为 14）。由于视野变窄，屏幕上的物体看起来变大了，这就是“推镜头”。
- **旋转 (Rotate)**: `self.camera.frame.animate.rotate(PI/4)` 会旋转视角。

### 2. 状态保存与恢复 (Save & Restore)
当你需要频繁在局部特写和全局视图之间切换时，手动设置位置非常繁琐。
- `self.camera.frame.save_state()`: 记录当前的位置、缩放和旋转。
- `Restore(self.camera.frame)`: 动画式地回到保存的状态。

---

## 🚀 深度技巧：动态追踪

利用 `add_updater`，我们可以让摄像机帧跟随某个物体移动。

```python
# 让相机中心始终对准 dot
self.camera.frame.add_updater(lambda f: f.move_to(dot.get_center()))
```

**❗ 常见坑点 (Common Pitfalls):**
- **物体消失了？**: 如果你移动了相机但没有配套调整背景（如 `NumberPlane`），建议使用足够大的背景。
- **相机追踪中的“平移”与“旋转”**: 仅用 `move_to` 追踪时，目标保持在中心，但背景不会旋转。
- **❗ 深度避坑：相机帧的 Updater 激活**:
  - **现象**: 给 `self.camera.frame` 添加了 `add_updater` 但发现完全没反应。
  - **原因**: Manim 仅对已添加到场景中的 Mobjects 执行 updater。必须调用 `self.add(self.camera.frame)` 显式将其加入。
- **旋转缩放陷阱 (The Rotation-Scale Trap)**:
  - 在 `add_updater` 中同时调用 `rotate` 和 `set_width` 会导致视角“呼吸式抖动”。
  - **解决方案**: 在开启旋转前固定好缩放，或使用绝对高度。
- **渲染性能**: 向量图形即使无限缩放也非常清晰，位图则容易失真。

---

## 🛠 常用 API 速查

| 函数 | 功能 | 示例 |
|------|------|------|
| `self.camera.frame.animate.move_to()` | 镜头对准指定点或物体 | `move_to(dot)` |
| `self.camera.frame.animate.set_width()` | 改变镜头宽度（控制缩放） | `set_width(5)` |
| `self.camera.frame.animate.rotate()` | 旋转镜头视角 | `rotate(PI/2)` |
| `self.camera.frame.save_state()` | 保存摄像机当前状态 | - |
| `Restore(self.camera.frame)` | 恢复摄像机保存的状态 | - |

---

## 📝 本日练习

1. **基础**: 创建三个分散分布的矩形，让相机按顺序依次“路过”它们。
2. **挑战**: 编写一个场景，让一个粒子在屏幕上随机弹跳，摄像机实时平滑地追踪该粒子，并配合背景网格的变化。

---

> [!TIP]
> 深入理解 `camera.frame` 作为一个 `Mobject` 的本质，意味着你可以像操作圆、方块一样对其使用 `animate` 属性！
