def find_path(dataset_name):
    if dataset_name == 'raf_db':
        return 'config/raf_db.yaml'
    elif dataset_name == 'eurosat':
        return 'config/eurosat.yaml'
    elif dataset_name == 'stanford_car':
        return 'config/stanford_car.yaml'
    elif dataset_name == 'flower102':
        return 'config/flower102.yaml'
    elif dataset_name == 'dtd':
        return 'config/dtd.yaml'
    elif dataset_name == 'caltech101':
        return 'config/caltech101.yaml'
    elif dataset_name == 'pets':
        return 'config/pets.yaml'
    elif dataset_name == 'food101':
        return 'config/food101.yaml'
    elif dataset_name == 'aircraft':
        return 'config/aircraft.yaml'
    elif dataset_name == 'sun397':
        return 'config/sun397.yaml'
    elif dataset_name == 'imagenet':
        return 'config/imagenet.yaml'
    elif dataset_name == 'k400':
        return 'config/k400.yaml'
    elif dataset_name == 'ssv1':
        return 'config/ssv1.yaml'
    elif dataset_name == 'ucf':
        return 'config/ucf.yaml' 
    elif dataset_name == 'hmdb':
        return 'config/hmdb.yaml'   
    else:
        raise NotImplementedError
