
def rename_points_descriptions(category):
    updated_point_names = []
    if category['supercategory'] == 'animal_face':
        updated_point_names = ['top left side of the left eye', 'bottom right side of the left eye',
                               'bottom left side of the right eye', 'top right side of the right eye',
                               'nose tip', 'left side of the lip', 'right side of the lip', 'top side of the lip',
                               'bottom side of the lip']
    elif category['name'] == 'sofa':
        updated_point_names = ['left and back leg', 'left and front leg', 'left and back side of the seat',
                               'left and front side of the seat', 'back side of the left armrest',
                               'front side of the left armrest', 'top left side of the backrest',
                               'right and back leg', 'right and front leg', 'right and back side of the seat',
                               'right and front side of the seat', 'back side of the right armrest',
                               'front side of the right armrest', 'top right side of the backrest']
    elif category['name'] == 'chair':
        updated_point_names = ['left and front leg', 'right and front leg', 'right and back leg',
                               'left and back leg', 'left and front side of the seat',
                               'right and front side of the seat', 'right and back side of the seat',
                               'left and back side of the seat', 'top left side of the backseat',
                               'top right side of the backseat']
    elif category['name'] == 'bed':
        updated_point_names = ['left and back leg', 'left and front leg', 'left and back side of the mattress',
                               'left and front side of the mattress', 'top left side of the headboard',
                               'right and back leg', 'right and front leg', 'right and back side of the mattress',
                               'right and front side of the mattress', 'top right side of the headboard']
    elif category['name'] == 'swivelchair':
        updated_point_names = ['wheel', 'wheel', 'wheel', 'wheel', 'wheel', 'center of the wheels',
                               'center of the seat', 'left and front side of the seat',
                               'right and front side of the seat', 'right and back side of the seat',
                               'left and back side of the seat', 'top left side of the backrest',
                               'top right side of the backrest']
    elif category['name'] == 'table':
        updated_point_names = ['left and front side of the top', 'left and back side of the top',
                               'right and front side of the top', 'right and back side of the top',
                               'left and front leg', 'left and back leg', 'right and front leg',
                               'right and back leg']
    elif category['supercategory'] == 'vehicle':
        # windshield is not present in the skeleton and should be ignored.
        updated_point_names = ['front and right wheel', 'front and left wheel', 'rear and right wheel',
                               'rear and left wheel', 'right headlight', 'left headlight', 'right taillight',
                               'left taillight', 'windshield', 'front and right side of the top',
                               'front and left side of the top', 'rear and right side of the top',
                               'rear and left side of the top']
    elif category['name'] == 'skirt':
        updated_point_names = ['top left side of the skirt', 'top side of the skirt', 'top right side of the skirt',
                               'left side of the skirt', 'bottom left side of the skirt', 'bottom side of the skirt',
                               'bottom right side of the skirt', 'right side of the skirt']
    elif category['name'] == 'short_sleeved_outwear':
        updated_point_names = ['back side of the collar', 'top left side of the placket', 'front left side of the collar',
                               'left side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left side of the shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left and upper body of the shirt',
                               'left and lower body of the shirt', 'bottom left side of the shirt',
                               'bottom left side of the shirt placket', 'bottom right side of the shirt',
                               'right and lower body of the shirt', 'right and upper body of the shirt',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right side of the shoulder seam', 'top right side of the collar',
                               'upper right side of the shirt placket', 'lower right side of the shirt placket',
                               'bottom right side of the shirt placket', 'upper left side of the shirt placket',
                               'lower left side of the shirt placket']
    elif category['name'] == 'long_sleeved_outwear':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar', 'top left side of the placket',
                               'front right side of the collar', 'right side of the collar',
                               'left side of the shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left and upper body of the shirt',
                               'left and lower body of the shirt', 'bottom left side of the shirt',
                               'bottom left side of the shirt placket', 'bottom right side of the shirt',
                               'right and lower body of the shirt', 'right and upper body of the shirt',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right side of the shoulder seam', 'top right side of the placket',
                               'upper right side of the shirt placket', 'lower right side of the shirt placket',
                               'bottom right side of the shirt placket', 'upper left side of the shirt placket',
                               'lower left side of the shirt placket']
    elif category['name'] == 'sling':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                               'front side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left shoulder strap', 'upper left body of the shirt', 'lower left body of the shirt',
                               'bottom left side of the shirt', 'bottom side of the shirt',
                               'bottom right side of the shirt', 'lower right side of the shirt',
                               'upper right side of the shirt', 'right shoulder strap']

    elif category['name'] == 'sling_dress':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                               'front side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left strap', 'upper left body of the dress', 'upper left body of the dress',
                               'left body of the dress', 'lower left side of the dress',
                               'bottom left side of the dress', 'bottom side of the dress',
                               'bottom right side of the dress', 'lower right side of the dress',
                               'right body of the dress', 'upper right body of the dress',
                               'upper right body of the dress', 'right strap']
    elif category['name'] == 'long_sleeved_dress':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                               'front side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left side of the shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left and upper body of the dress',
                               'left and upper body of the dress', 'left body of the dress',
                               'left and lower body of the dress', 'bottom left side of the dress',
                               'bottom side of the dress', 'bottom right side of the dress',
                               'right and lower body of the dress', 'right body of the dress',
                               'right and upper body of the dress', 'right and upper body of the dress',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right side of the shoulder seam']
    elif category['name'] == 'short_sleeved_dress':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                               'front side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left side of the shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left and upper body of the dress',
                               'left and upper body of the dress', 'left body of the dress',
                               'left and lower body of the dress', 'bottom left side of the dress',
                               'bottom side of the dress', 'bottom right side of the dress',
                               'right and lower body of the dress', 'right body of the dress',
                               'right and upper body of the dress', 'right and upper body of the dress',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right side of the shoulder seam']
    elif category['name'] == 'vest':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                               'front side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left shoulder', 'upper left body of the shirt', 'lower left body of the shirt',
                               'bottom left side of the shirt', 'bottom side of the shirt',
                               'bottom right side of the shirt', 'lower right side of the shirt',
                               'upper right side of the shirt', 'right shoulder']
    elif category['name'] == 'vest_dress':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                               'front side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left shoulder', 'upper left body of the dress', 'upper left body of the dress',
                               'left body of the dress', 'lower left body of the dress',
                               'bottom left side of the dress', 'bottom side of the dress',
                               'bottom right side of the dress', 'lower right side of the dress',
                               'right side of the dress', 'upper right side of the dress',
                               'upper right side of the dress', 'right shoulder']

    elif category['name'] == 'long_sleeved_shirt':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                               'front side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left side of the shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left and upper body of the shirt',
                               'left and lower body of the shirt', 'bottom left side of the shirt',
                               'bottom side of the shirt', 'bottom right side of the shirt',
                               'right and lower body of the shirt', 'right and upper body of the shirt',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right side of the shoulder seam']

    elif category['name'] == 'shorts':
        updated_point_names = ['top left side of the pants', 'top side of the pants', 'top right side of the pants',
                               'left side of the pants', 'left side of the left leg opening',
                               'right side of the left leg opening', 'crutch', 'left side of the right leg opening',
                               'right side of the right leg opening', 'right side of the pants']
    elif category['name'] == 'trousers':
        updated_point_names = ['top left side of the pants', 'top side of the pants', 'top right side of the pants',
                               'upper left side of the pants', 'lower left side of the pants',
                               'left side of the left leg opening', 'right side of the left leg opening',
                               'lower left side of the pants', 'crutch', 'lower right side of the pants',
                               'left side of the right leg opening', 'right side of the right leg opening',
                               'lower right side of the pants', 'upper right side of the pants']
    elif category['name'] == 'short_sleeved_shirt':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                               'front side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left side of the shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left and upper body of the shirt',
                               'left and lower body of the shirt', 'bottom left side of the shirt',
                               'bottom side of the shirt', 'bottom right side of the shirt',
                               'right and lower body of the shirt', 'right and upper body of the shirt',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right side of the shoulder seam']
    elif category['id'] == 40:
        # human_face from 300W
        updated_point_names = ['top side of the upper left cheek', 'middle side of the upper left cheek',
                               'bottom side of the upper left cheek',
                               'top side of the lower left cheek', 'middle side of the lower left cheek',
                               'bottom side of the lower left cheek',
                               'top side of the left jaw', 'bottom side of the left jaw',
                               'chin',
                               'bottom side of the right jaw', 'top side of the right jaw',
                               'bottom side of the lower right cheek', 'middle side of the lower right cheek',
                               'top side of the lower right cheek',
                               'bottom side of the upper right cheek', 'middle side of the upper right cheek',
                               'top side of the upper right cheek',
                               'left side of the left eyebrow', 'middle side of the left eyebrow',
                               'middle side of the left eyebrow', 'middle side of the left eyebrow',
                               'right side of the left eyebrow',
                               'left side of the right eyebrow', 'middle side of the right eyebrow',
                               'middle side of the right eyebrow', 'middle side of the right eyebrow',
                               'right side of the right eyebrow',
                               'top side of the nose', 'middle side of the nose', 'middle side of the nose',
                               'bottom side of the nose',
                               'left side of the left nostril', 'right side of the left nostril',
                               'middle of the nostrils',
                               'left side of the right nostril', 'right side of the right nostril',
                               'left side of the left eye',
                               'top left side of the left eye', 'top right side of the left eye',
                               'right side of the left eye',
                               'bottom right side of the left eye', 'bottom left side of the left eye',
                               'left side of the right eye',
                               'top left side of the right eye', 'top right side of the right eye',
                               'right side of the right eye',
                               'bottom right side of the right eye', 'bottom left side of the right eye',
                               'left side of the lips', 'top left side of the upper lip',
                               'top side of the upper lip', 'top side of the upper lip', 'top side of the upper lip',
                               'top right side of the upper lip', 'right side of the lips',
                               'bottom right side of the bottom lip',
                               'bottom side of the lower lip', 'bottom side of the lower lip', 'bottom side of the lower lip',
                               'bottom left side of the lower lip',
                               'left side of the lips',
                               'bottom side of the upper lip', 'bottom side of the upper lip', 'bottom side of the upper lip',
                               'right side of the lips',
                               'top side of the lower lip', 'top side of the lower lip', 'top side of the lower lip'
                               ]
    elif category['id'] == 18:
        updated_point_names = ['left side of the left eyebrow', 'middle side of the left eyebrow',
                               'right side of the left eyebrow', 'left side of the right eyebrow',
                               'middle side of the right eyebrow', 'right side of the right eyebrow',
                               'left side of the left eye', 'middle side of the left eye', 'right side of the left eye',
                               'left side of the right eye', 'middle side of the right eye',
                               'right side of the right eye', 'left side of the nose', 'middle of the nostrils',
                               'right side of the nose', 'left side of the lips', 'mouth', 'right side of the lips',
                               'chin']
    elif category['name'] == 'hand':
        updated_point_names = ['wrist',
                               'base of the thumb', 'lower part of the thumb', 'middle part of the thumb',
                               'top part of the thumb', 'base of the index finger', 'lower part of the index finger',
                               'middle part of the index finger',  'top part of the index finger',
                               'base of the middle finger', 'lower part of the middle finger',
                               'middle part of the middle finger', 'top part of the middle finger',
                               'base of the ring finger', 'lower part of the ring finger',
                               'middle part of the ring finger', 'top part of the ring finger',
                               'base of the pinky finger', 'lower part of the pinky finger',
                               'middle part of the pinky finger', 'top part of the pinky finger'
                               ]
    elif category['name'] == 'locust':
        updated_point_names = ['head', 'neck', 'middle part', 'lower part', 'tail',
                               'tip of the left antenna', 'base of the left antenna', 'left eye',
                               'front left leg', 'front left leg', 'front left leg', 'front left leg',
                               'middle left leg', 'middle left leg', 'middle left leg', 'middle left leg',
                               'back left leg', 'back left leg', 'back left leg', 'back left leg',
                               'tip of the right antenna', 'base of the right antenna', 'right eye',
                               'front right leg', 'front right leg', 'front right leg', 'front right leg',
                               'middle right leg', 'middle right leg', 'middle right leg', 'middle right leg',
                               'back right leg', 'back right leg', 'back right leg', 'back right leg']
    else:
        updated_point_names = category['keypoints']
        updated_point_names = [k.replace("_", " ") for k in updated_point_names]

    return updated_point_names