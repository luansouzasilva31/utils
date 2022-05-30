import matplotlib.pyplot as plt


def plot_images(images: list , titles: list = None , grid: tuple = None) :
    '''
    Function for plotting N images organized in grid format.
    :param images: list of np.ndarray images
    :param titles: list of str titles
    :param grid: tuple containing the grid shape
    :return:
    '''
    # Checking titles
    if titles :
        assert len(images) == len(titles) > 0 , 'The number of titles must match the number of images.'
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
    
    # Creating plotting section
    fig , axis = plt.subplots(nrows=grid[0] , ncols=grid[1])
    
    count = 0
    if grid[0] == 1 and grid[1] == 1 :
        axis.imshow(images[count])
        axis.set_title(titles[count])
    
    elif grid[0] == 1 or grid[1] == 1 :
        for i in range(max(grid[0] , grid[1])) :
            axis[i].imshow(images[count])
            axis[i].set_title(titles[count])
            count += 1
    
    else :
        for i in range(grid[0]) :
            for j in range(grid[1]) :
                axis[i , j].imshow(images[count])
                axis[i , j].set_title(titles[count])
                count += 1
    
    plt.show(block=True)
