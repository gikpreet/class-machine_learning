import numpy as np
import matplotlib.pyplot as plt

def draw_thumbnail(arr, ratio=1, cmap='gray'):
    n = len(arr)
    rows = int(np.ceil(n / 10))
    cols = n if rows < 2 else 10

    fig, axs = plt.subplots(rows, cols, figsize=(cols * ratio, rows * ratio), squeeze=False)

    for i in range(rows):
        for j in range(cols):
            if i * 10 + j < n:
                axs[i, j].imshow(arr[i * 10 + j], cmap=cmap)
            axs[i, j].axis('off')
    plt.show()

if __name__ == '__main__':
    pass