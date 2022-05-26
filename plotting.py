import matplotlib.pyplot as plt


def plot_images(images: list , titles: list = None , grid: tuple = None) :
    # Checking titles
    if titles :
        assert len(images) == len(titles) , 'The number of titles must match the number of images.'
    else :
        titles = ['' for i in images]
    
    # Checking grid
    if grid :
        assert len(images) <= grid[0] * grid[1] , \
            f'Grid parameter must match the number of images. {len(images)} != {grid[0] * grid[1]}'
        assert len(grid) == 2 , 'Grid parameter must be a 2-length tuple.'
    
    else :
        # Infering grid from images list
        grid = list(i + 1 for i , _ in enumerate(images) if len(images) / (i + 1) <= (i + 1))
        grid = (grid[0] , grid[0]) if grid[0] ** 2 == len(images) else (grid[0] , grid[0] - 1)
    
    fig , axis = plt.subplots(nrows=grid[0] , ncols=grid[1])
    
    count = 0
    for i in range(grid[0]) :
        for j in range(grid[1]) :
            axis[i , j].imshow(images[count])
            axis[i , j].set_title(titles[count])
            count += 1
    
    plt.show(block=True)
