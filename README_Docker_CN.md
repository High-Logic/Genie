# Genie TTS

这是在 NAS 服务器上部署 Genie TTS Docker 容器的简单指南。

## 部署步骤

1. **下载模型**
   从 [Hugging Face](https://huggingface.co/High-Logic/Genie) 下载所需模型。

2. **构建 Docker 镜像**
   在本地构建 Docker 镜像：

   ```bash
   docker build -t genie_tts .
   ```

3. **保存 Docker 镜像**
   将 Docker 镜像保存为文件以便传输：

   ```bash
   docker save -o genie_tts.tar genie_tts
   ```

4. **上传 Docker 镜像到 NAS**
   将 `genie_tts.tar` 文件传到 NAS 服务器。

5. **上传 Docker-Compose 文件**
   将 `docker-compose.yml` 上传到 NAS 服务器。

6. **准备模型目录**
   在 `docker-compose.yml` 所在路径下创建一个名为 `models` 的目录：

   ```bash
   mkdir models
   ```

7. **上传模型文件夹**
   将 `misono_mika` 文件夹上传到 `models` 目录下。

8. **启动 Docker-Compose**
   在后台启动容器：

   ```bash
   sudo docker-compose up -d
   ```

9. **部署完成**
   Genie TTS 服务现在已成功运行。