import torch

import torch.nn as nn

import torch.optim as optim

from torchvision import datasets, transforms

from torch.utils.data import DataLoader

import matplotlib.pyplot as plt

import numpy as np

import os

from PIL import Image



# Simple CNN for MNIST

class SimpleCNN(nn.Module):

    def __init__(self):

        super(SimpleCNN, self).__init__()

        self.conv = nn.Sequential(

            nn.Conv2d(1, 10, kernel_size=5),

            nn.ReLU(),

            nn.MaxPool2d(2)

        )

        self.fc = nn.Sequential(

            nn.Linear(10 * 12 * 12, 10)

        )



    def forward(self, x):

        x = self.conv(x)

        x = x.view(-1, 10 * 12 * 12)

        x = self.fc(x)

        return x



def fgsm_attack(image, epsilon, data_grad):

    # Sign of gradient * epsilon

    sign_data_grad = data_grad.sign()

    perturbed_image = image + epsilon * sign_data_grad

    return torch.clamp(perturbed_image, 0, 1)



def main():

    transform = transforms.ToTensor()

    train_set = datasets.MNIST('./data', train=True, download=True, transform=transform)

    test_set = datasets.MNIST('./data', train=False, download=True, transform=transform)

    train_loader = DataLoader(train_set, batch_size=64, shuffle=True)

    test_loader = DataLoader(test_set, batch_size=1, shuffle=True)



    model = SimpleCNN()

    criterion = nn.CrossEntropyLoss()

    optimizer = optim.Adam(model.parameters(), lr=0.001)



    print("[INFO] Training a small model first...")

    model.train()

    for epoch in range(1):  # Keep it tiny for demo

        for data, target in train_loader:

            optimizer.zero_grad()

            output = model(data)

            loss = criterion(output, target)

            loss.backward()

            optimizer.step()

            break  # just a few samples



    torch.save(model.state_dict(), "model.pth")

    print("[INFO] Model trained and saved.")



    model.eval()

    example_data, example_target = next(iter(test_loader))

    example_data.requires_grad = True



    output = model(example_data)

    init_pred = output.max(1, keepdim=True)[1]

    print(f"[INFO] Original prediction: {init_pred.item()}")



    loss = criterion(output, example_target)

    model.zero_grad()

    loss.backward()



    data_grad = example_data.grad.data

    epsilon = 0.25

    perturbed_data = fgsm_attack(example_data, epsilon, data_grad)



    adv_output = model(perturbed_data)

    adv_pred = adv_output.max(1, keepdim=True)[1]

    print(f"[INFO] Adversarial prediction: {adv_pred.item()}")



    # Save original and adversarial images

    to_pil = transforms.ToPILImage()

    orig_img = to_pil(example_data.squeeze())

    adv_img = to_pil(perturbed_data.squeeze())



    orig_img.save("original_example.png")

    adv_img.save("fgsm_adversarial_example.png")

    print("[INFO] Images saved: original_example.png, fgsm_adversarial_example.png")



    # Side-by-side comparison

    side_by_side = Image.new('L', (56, 28))

    side_by_side.paste(orig_img, (0, 0))

    side_by_side.paste(adv_img, (28, 0))

    side_by_side.save("comparison.png")

    print("[INFO] Comparison image saved: comparison.png")



if __name__ == "__main__":

    main()


