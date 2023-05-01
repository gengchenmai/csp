def get_paths(variable_name):
    paths = {
    'mask_dir': '../data/',
    'inat_2018_data_dir': '../geo_prior_data_csp/data/inat_2018/',
    'fmow_data_dir': '../geo_prior_data_csp/data/fmow/',
    }
    return paths[variable_name]
