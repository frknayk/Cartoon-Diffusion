import argparse
from diffusers import StableDiffusionPipeline
import torch
import numpy as np
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description="Run StableDiffusionPipeline with command-line arguments")
    parser.add_argument("--model_path", required=True, help="Path to the pre-trained model")
    parser.add_argument("--prompt", required=True, help="Prompt for the diffusion process")
    parser.add_argument("--num_inference_steps", type=int, default=50, help="Number of inference steps")
    parser.add_argument("--guidance_scale", type=float, default=7.5, help="Guidance scale for diffusion")
    args = parser.parse_args()

    pipe = StableDiffusionPipeline.from_pretrained(args.model_path, torch_dtype=torch.float16)
    pipe.to("cuda")

    prompt = args.prompt
    image = pipe(prompt, num_inference_steps=args.num_inference_steps, guidance_scale=args.guidance_scale).images[0]

    pil_image = Image.fromarray(np.asarray(image))
    pil_image.show()

if __name__ == "__main__":
    main()
