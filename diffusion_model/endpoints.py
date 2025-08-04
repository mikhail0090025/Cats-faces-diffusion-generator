from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
import torch
import numpy as np
from PIL import Image
import io
import diffusion_model as dm

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is a root of diffusion model microservice"}

@app.get("/generate")
async def image_endpoint():
    diffusion_steps = 50
    power = 0.3
    dm.model.plot_images(num_rows=3, num_cols=3, power=power, diffusion_steps=diffusion_steps)

    return FileResponse("generated.png", media_type="image/png")

@app.get("/gif_generate")
async def gif_image_endpoint():
    num_images = 1
    diffusion_steps = 100
    power = 0.3
    initial_noise = torch.randn((num_images, 3, dm.image_size, dm.image_size))
    generated_images = dm.model.generate_gif(initial_noise, diffusion_steps, filename="diffusion_process.gif", power=power)

    return FileResponse("diffusion_process.gif", media_type="image/gif")