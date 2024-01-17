from flasgger import swag_from

template = {
    "swagger": "2.0",
    "info": {
        "title": "Train/Val AOI & Labeling Service API Documentation",
        "description": "API documentation for the Aerotract LabelService tool",
        "version": "1.0.0"
    }
}

client_project_stand_params = [
    {
        'name': 'client_id',
        'description': 'Client ID of data to process',
        'example': '10007',
        'in': 'body',
        'required': True,
        'type': 'string'
    },{
        'name': 'project_id',
        'description': 'Project ID of data to process',
        'example': '101036',
        'in': 'body',
        'required': True,
        'type': 'string'
    },{
        'name': 'stand_id',
        'description': 'Stand ID of data to process',
        'example': '103',
        'in': 'body',
        'required': True,
        'type': 'string'
    },{
        'name': 'stand_persistent_id',
        'description': 'Stand Persistent ID of data to process',
        'example': '1015364',
        'in': 'body',
        'required': False,
        'type': 'string'
    }
]

swag_gen_aois = swag_from({
    'responses': {
        200: {
            'description': 'Succesfully submitted operation',
            'schema': {
                'type': 'string',
            }
        },
        500: {
            'description': 'Failed to submit operation',
            'schema': {
                'type': 'string',
            }
        }
    },
    'parameters': [
        *client_project_stand_params,
        {
            'name': 'gsd',
            'description': 'Ground Sampling Distance of image to process',
            'example': 0.24,
            'in': 'body',
            'required': False,
            'type': 'number',
            'format': 'float'
        },{
            'name': 'train_n',
            'description': 'Number of training AOIs to generate',
            'example': 5,
            'in': 'body',
            'required': False,
            'type': 'number'
        },{
            'name': 'train_height',
            'description': 'Height (ft) of training AOI',
            'example': 125,
            'in': 'body',
            'required': False,
            'type': 'number',
            'format': 'float'
        },{
            'name': 'train_width',
            'description': 'Width (ft) of training AOIs',
            'example': 125,
            'in': 'body',
            'required': False,
            'type': 'number',
            'format': 'float'
        },{
            'name': 'val_height',
            'description': 'Height (ft) of validation AOIs',
            'example': 24.1,
            'in': 'body',
            'required': False,
            'type': 'number',
            'format': 'float'
        },{
            'name': 'val_width',
            'description': 'Width (ft) of validation AOIs',
            'example': 24.1,
            'in': 'body',
            'required': False,
            'type': 'number'
        },{
            'name': 'val_spacing_ratio',
            'description': 'Create a (val_spacing_ratio)*(val_spacing_ratio) grid across the image',
            'example': 7,
            'in': 'body',
            'required': False,
            'type': 'number'
        }
    ]
})

swag_ref_aois_points = swag_from({
    'responses': {
        200: {
            'description': 'Succesfully submitted operation',
            'schema': {
                'type': 'string',
            }
        },
        500: {
            'description': 'Failed to submit operation',
            'schema': {
                'type': 'string',
            }
        }
    },
    'parameters': [
        *client_project_stand_params,
    ]
})