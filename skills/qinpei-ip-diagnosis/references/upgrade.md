# 版本自检与升级 · 执行手册

> **什么时候读这个文件**：学员说「升级到最新版本」「升级技能包」「技能包自检升级」「检查更新」「有没有新版本」「更新一下技能包」任意一句时。**五步一次做完，别来回问。**

---

**第 1 步 · 看本机装了什么**
```bash
ls -d ~/.workbuddy/skills/qinpei* 2>/dev/null
```

**第 2 步 · 取线上版本表**（这是唯一的版本真源，别用记忆里的版本号）
```bash
curl -fsSL --max-time 10 "https://qinpei-skill-all.app.workbuddy.host/skills-catalog.md?t=$(date +%s)"
```
在返回内容里找 **VERSION-MANIFEST** 那一段，每一行长这样：`包名=版本`。
取不到就换域名 `https://qinpei-skill-all.app.workbuddy.link/skills-catalog.md?t=时间戳` 再取一次；两次都失败 → **如实告诉学员「现在连不上更新服务器，过会儿再试」**。🔴 禁止瞎猜版本、禁止拿记忆里的旧版本糊弄。

**第 3 步 · 逐包比对**
比「线上版本」和「本机 `~/.workbuddy/skills/<包名>/SKILL.md` 里的 `version:`」：
- 线上更新 → 进第 4 步
- 一样 → 记作「已是最新」
- 本机有、版本表里没有 → 跳过，并在汇报里如实说明

**第 4 步 · 升级（一个包一次）**
```bash
S=<包名>
U="https://qinpei-skill-all.app.workbuddy.host/skillhub-zips/$S.zip?t=$(date +%s)"
curl -fsSL --max-time 15 "$U" -o "/tmp/$S.zip"
head -c 2 "/tmp/$S.zip"          # 应为 PK，确认它真是个 zip
python3 -c "import zipfile,os;zipfile.ZipFile('/tmp/$S.zip').extractall(os.path.expanduser('~/.workbuddy/skills/$S'))" \
  || unzip -o "/tmp/$S.zip" -d ~/.workbuddy/skills/$S/
grep -m1 '^version:' ~/.workbuddy/skills/$S/SKILL.md    # 复查：应等于线上版本
```

**🔴 升级四条铁律**
1. **绝不用 `rm -rf` 删技能目录**——学员的资料卡和档案就在里面
2. **不用手工备份**：zip 里本来就不含 `我的画像.md` 和 `学员档案/`，覆盖解压**只覆盖同名文件**，学员数据天然不受影响
3. **解压必须复查版本**——`grep` 出来的等于线上版本，才算升级成功
4. **🔴 取任何本站文件都要带时间戳参数**——边缘节点会缓存旧内容。**上面所有 `qinpei-skill-all.app.workbuddy.host` 地址，抓取时一律在末尾拼 `?t=$(date +%s)`**（只能读网页、跑不了 shell 时，就换成当前时间戳的随机数字）。漏了它就可能读到旧版本表，升级会**静默不执行**（最难发现）。

**第 5 步 · 汇报（一句话，别写小作文）**
> 已升级：朋友圈 2.3.4、展业诊断 3.0.2 ✅ 不用重装，你的资料卡和记录都还在。
> （全都已是最新时：）查过了，你现在都是最新版，不用动。

本机一个 qinpei 技能包都没有 → 说明还没装过，引导他用原来的安装方式装一次即可。

**手机端 / 没有命令行工具怎么办**
用你能用的取文件方式（读网页 / 下载）做同样三件事：**取版本表 → 比版本 → 覆盖写入新文件**。落盘位置和上面一样，**同样不许删除任何已有文件**。
