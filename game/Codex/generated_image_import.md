# AI 生图导入流程

用途：把生图结果稳定落到项目 `images/` 目录，不再依赖客户端是否自动保存到指定文件夹。

## 脚本

使用：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\import_generated_image.ps1 -ImageName c1_07_pq_run_v1
```

默认行为：

- 自动从 `C:\Users\fld16\.codex\generated_images` 里取最新的一张图
- 如果文件名形如 `c1_07_pq_run_v1`，会自动放进 `images/chapter1/`
- 导入后会打印可直接粘贴到 `bg_images.rpy` 的 `image bg ...` 和 `scene bg ...`

## 常用写法

指定章节：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\import_generated_image.ps1 -ImageName c2_02_cpa_pq_v1 -Chapter 2
```

指定源文件：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\import_generated_image.ps1 -ImageName c1_08_pq_pose_v1 -SourcePath "C:\path\to\image.png"
```

覆盖同名文件：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\import_generated_image.ps1 -ImageName c1_08_pq_pose_v1 -Overwrite
```

## 约束

- `ImageName` 只允许小写字母、数字、下划线
- 建议继续遵守 `c章节号_场次号_主体或动作_v版本号`
- 角色图、CG、背景图都可以走这套导入流程
