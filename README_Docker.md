# Genie TTS

A simple guide to set up the Genie TTS Docker container with models on your NAS server.

## Steps to Deploy

1. **Download the Models**
   Download the required models from [Hugging Face](https://huggingface.co/High-Logic/Genie).

2. **Build the Docker Image**
   Build the Docker image locally:

   ```bash
   docker build -t genie_tts .
   ```

3. **Save the Docker Image**
   Save the Docker image to a file for transfer:

   ```bash
   docker save -o genie_tts.tar genie_tts
   ```

4. **Upload the Docker Image to NAS**
   Transfer `genie_tts.tar` to your NAS server.

5. **Upload the Docker-Compose File**
   Upload your `docker-compose.yml` to the NAS server.

6. **Prepare Model Directory**
   On the NAS, under the path where `docker-compose.yml` is located, create a directory named `models`:

   ```bash
   mkdir models
   ```

7. **Upload the Model Folder**
   Upload the folder `misono_mika` into the `models` directory.

8. **Run Docker-Compose**
   Start the container in detached mode:

   ```bash
   sudo docker-compose up -d
   ```

9. **Deployment Complete**
   The Genie TTS service should now be running successfully.
