def rename_points_descriptions(category, test_type=None):
    if test_type is None:
        return regular_descriptions(category)
    elif test_type == "synonyms_test":
        return synonyms_test(category)
    elif test_type == "translate_test":
        return translate_test(category)
    elif test_type == "typo_test":
        return typo_test(category)

def regular_descriptions(category):
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

    elif category['name'] == 'fly':
        updated_point_names = ['head', 'left eye', 'right eye', 'neck', 'thorax', 'abdomen', 'front right leg',
                               'start point of the front right leg', 'middle point of the front right leg',
                               'almost the end point of the front right leg', 'end point of the front right leg',
                               'start point of the middle right leg', 'middle point of the middle right leg',
                               'almost the end point of the middle right leg', 'end point of the middle right leg',
                               'start point of the back right leg', 'middle point of the back right leg',
                               'almost the end point of the back right leg', 'end point of the back right leg',
                               'start point of the front left leg', 'middle point of the front left leg',
                               'almost the end point of the front left leg', 'end point of the front left leg',
                               'start point of the middle left leg', 'middle point of the middle left leg',
                               'almost the end point of the middle left leg', 'end point of the middle left leg',
                               'start point of the back left leg', 'middle point of the back left leg',
                               'almost the end point of the back left leg', 'end point of the back left leg',
                               'left wing', 'right wing']
    else:
        updated_point_names = category['keypoints']
        updated_point_names = [k.replace("_", " ") for k in updated_point_names]

    return updated_point_names

def synonyms_test(category):
    updated_point_names = []
    # total: 37

    # 34 categories
    if category['name'] in ['antelope_body', 'beaver_body', 'bison_body', 'bobcat_body', 'cat_body', 'cheetah_body',
                            'cow_body', 'deer_body', 'dog_body', 'elephant_body', 'fox_body', 'giraffe_body',
                            'gorilla_body', 'hamster_body', 'hippo_body', 'horse_body', 'leopard_body', 'lion_body',
                            'otter_body', 'panda_body', 'panther_body', 'pig_body', 'polar_bear_body', 'rabbit_body',
                            'raccoon_body', 'rat_body', 'rhino_body', 'sheep_body', 'skunk_body', 'spider_monkey_body',
                            'squirrel_body', 'weasel_body', 'wolf_body', 'zebra_body']:
        updated_point_names = ['left oculus', 'right oculus', 'beak', 'cervix', 'pelvis',
                               'left upper arm bone', 'left ancon', 'left front wrist', 'right upper arm bone',
                               'right ancon', 'right front wrist', 'left back thigh', 'left back patella',
                               'left back foot', 'right back thigh', 'right back patella', 'right back foot']
    elif category['name'] in ["human_body", "person", "macaque"]:
        updated_point_names = ['nostrils', 'left pupil', 'right pupil', 'left auricle', 'right auricle',
                               'left arm joint', 'right arm joint', 'middle of the left arm',
                               'middle of the right arm', 'left palm', 'right palm', 'left thigh', 'right thigh',
                               'middle of the left leg', 'middle of the right leg', 'left foot', 'right foot']
    elif category['supercategory'] == 'bird':
        updated_point_names = ['dorsal region', 'bill', 'abdomen', 'pectoral area', 'crown of the head', 'forehead',
                               'left eye', 'left limb', 'left wing', 'nape', 'right eye', 'right limb', 'right wing',
                               'caudal feathers', 'cervix']


    elif category['supercategory'] == 'animal_face':
        updated_point_names = ['upper left region of the left eye', 'lower right region of the left eye',
                               'lower left region of the right eye', 'upper right region of the right eye',
                               'nasal tip', 'left lip margin', 'right lip margin', 'superior lip margin',
                               'inferior lip margin']
    elif category['name'] == 'sofa':
        updated_point_names = ['rear left leg', 'front left leg', 'rear left seat base',
                               'front left seat base', 'rear left armrest',
                               'front left armrest', 'upper left backrest',
                               'rear right leg', 'front right leg', 'rear right seat base',
                               'front right seat base', 'rear right armrest',
                               'front right armrest', 'upper right backrest']
    elif category['name'] == 'chair':
        updated_point_names = ['front left leg', 'front right leg', 'rear right leg',
                               'rear left leg', 'front left seat base',
                               'front right seat base', 'rear right seat base',
                               'rear left seat base', 'upper left backrest',
                               'upper right backrest']
    elif category['name'] == 'bed':
        updated_point_names = ['rear left leg', 'front left leg', 'rear left mattress base',
                               'front left mattress base', 'upper left headboard',
                               'rear right leg', 'front right leg', 'rear right mattress base',
                               'front right mattress base', 'upper right headboard']
    elif category['name'] == 'swivelchair':
        updated_point_names = ['caster', 'caster', 'caster', 'caster', 'caster', 'wheel hub',
                               'seat center', 'front left seat base',
                               'front right seat base', 'rear right seat base',
                               'rear left seat base', 'upper left backrest',
                               'upper right backrest']
    elif category['name'] == 'table':
        updated_point_names = ['front left tabletop', 'rear left tabletop',
                               'front right tabletop', 'rear right tabletop',
                               'front left leg', 'rear left leg', 'front right leg',
                               'rear right leg']
    elif category['supercategory'] == 'vehicle':
        # windshield is not present in the skeleton and should be ignored.
        updated_point_names = ['front right wheel', 'front left wheel', 'rear right wheel',
                               'rear left wheel', 'right headlamp', 'left headlamp', 'right taillamp',
                               'left taillamp', 'windshield', 'front right roof edge',
                               'front left roof edge', 'rear right roof edge',
                               'rear left roof edge']
    elif category['name'] == 'skirt':
        updated_point_names = ['upper left skirt', 'upper skirt', 'upper right skirt',
                               'left skirt', 'lower left skirt', 'lower skirt',
                               'lower right skirt', 'right skirt']
    elif category['name'] == 'short_sleeved_outwear':
        updated_point_names = ['rear collar', 'upper left placket', 'front left collar',
                               'left collar', 'front right collar', 'right collar',
                               'left shoulder seam', 'the left sleeve', 'the left sleeve', 'the left sleeve',
                               'the left sleeve', 'the left sleeve', 'left upper torso',
                               'left lower torso', 'lower left shirt',
                               'lower left placket', 'lower right shirt',
                               'right lower torso', 'right upper torso',
                               'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve',
                               'right shoulder seam', 'upper right collar',
                               'upper right placket', 'lower right placket',
                               'lower right placket', 'upper left placket',
                               'lower left placket']
    elif category['name'] == 'long_sleeved_outwear':
        updated_point_names = ['rear collar', 'left collar', 'front left collar', 'upper left placket',
                               'front right collar', 'right collar',
                               'left shoulder seam', 'the left sleeve', 'the left sleeve', 'the left sleeve',
                               'the left sleeve', 'the left sleeve', 'the left sleeve', 'the left sleeve', 'the left sleeve', 'the left sleeve',
                               'left upper torso',
                               'left lower torso', 'lower left shirt',
                               'lower left placket', 'lower right shirt',
                               'right lower torso', 'right upper torso',
                               'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve',
                               'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve',
                               'right shoulder seam', 'upper right placket',
                               'upper right placket', 'lower right placket',
                               'lower right placket', 'upper left placket',
                               'lower left placket']
    elif category['name'] == 'sling':
        updated_point_names = ['rear collar', 'left collar', 'front left collar',
                               'front collar', 'front right collar', 'right collar',
                               'left strap', 'left upper torso', 'left lower torso',
                               'lower left shirt', 'lower shirt',
                               'lower right shirt', 'right lower torso',
                               'right upper torso', 'right strap']
    elif category['name'] == 'sling_dress':
        updated_point_names = ['rear collar', 'left collar', 'front left collar',
                               'front collar', 'front right collar', 'right collar',
                               'left strap', 'left upper dress', 'left upper dress',
                               'left torso', 'lower left dress',
                               'lower left dress', 'lower dress',
                               'lower right dress', 'lower right dress',
                               'right torso', 'right upper dress',
                               'right upper dress', 'right strap']
    elif category['name'] == 'long_sleeved_dress':
        updated_point_names = ['rear collar', 'left collar', 'front left collar',
                               'front collar', 'front right collar', 'right collar',
                               'left shoulder seam', 'the left sleeve', 'the left sleeve', 'the left sleeve',
                               'the left sleeve', 'the left sleeve', 'the left sleeve', 'the left sleeve',
                               'the left sleeve', 'the left sleeve', 'left upper dress',
                               'left upper dress', 'left torso',
                               'left lower dress', 'lower left dress',
                               'lower dress', 'lower right dress',
                               'right lower dress', 'right torso',
                               'right upper dress', 'right upper dress',
                               'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve',
                               'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve',
                               'right shoulder seam']
    elif category['name'] == 'short_sleeved_dress':
        updated_point_names = ['rear collar', 'left collar', 'front left collar',
                               'front collar', 'front right collar', 'right collar',
                               'left shoulder seam', 'the left sleeve', 'the left sleeve', 'the left sleeve',
                               'the left sleeve', 'the left sleeve', 'left upper dress',
                               'left upper dress', 'left torso',
                               'left lower dress', 'lower left dress',
                               'lower dress', 'lower right dress',
                               'right lower dress', 'right torso',
                               'right upper dress', 'right upper dress',
                               'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve',
                               'right shoulder seam']
    elif category['name'] == 'vest':
        updated_point_names = ['rear collar', 'left collar', 'front left collar',
                               'front collar', 'front right collar', 'right collar',
                               'the left shoulder', 'left upper torso', 'left lower torso',
                               'lower left shirt', 'lower shirt',
                               'lower right shirt', 'right lower torso',
                               'right upper torso', 'the right shoulder']
    elif category['name'] == 'vest_dress':
        updated_point_names = ['rear collar', 'left collar', 'front left collar',
                               'front collar', 'front right collar', 'right collar',
                               'the left shoulder', 'left upper dress', 'left upper dress',
                               'left torso', 'lower left dress',
                               'lower left dress', 'lower dress',
                               'right lower dress', 'right lower dress',
                               'right torso', 'right upper dress',
                               'right upper dress', 'the right shoulder']
    elif category['name'] == 'long_sleeved_shirt':
        updated_point_names = ['rear collar', 'left collar', 'front left collar',
                               'front collar', 'front right collar', 'right collar',
                               'left shoulder seam', 'the left sleeve', 'the left sleeve', 'the left sleeve',
                               'the left sleeve', 'the left sleeve', 'the left sleeve', 'the left sleeve',
                               'the left sleeve', 'the left sleeve', 'left upper torso',
                               'left lower torso', 'lower left shirt',
                               'lower shirt', 'lower right shirt',
                               'right lower torso', 'right upper torso',
                               'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve',
                               'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve',
                               'right shoulder seam']
    elif category['name'] == 'shorts':
        updated_point_names = ['upper left pants', 'upper pants', 'upper right pants',
                               'left pants', 'left left leg opening',
                               'right left leg opening', 'crotch', 'left right leg opening',
                               'right right leg opening', 'right pants']
    elif category['name'] == 'trousers':
        updated_point_names = ['upper left section of the pants', 'top portion of the pants', 'upper right section of the pants',
                               'left upper side of the pants', 'lower left section of the pants',
                               'left side of left leg seam', 'right side of left leg seam',
                               'lower left side seam', 'crotch', 'lower right side seam',
                               'left side of right leg seam', 'right side of right leg seam',
                               'right lower side of the pants', 'right upper side of the pants']
    elif category['name'] == 'short_sleeved_shirt':
        updated_point_names = ['back collar', 'left collar side', 'front left collar',
                               'front collar', 'front right collar', 'right collar side',
                               'left shoulder seam', 'the left sleeve', 'the left sleeve', 'the left sleeve',
                               'the left sleeve', 'the left sleeve', 'left upper torso',
                               'left lower torso', 'left bottom torso',
                               'bottom torso', 'right bottom torso',
                               'right lower torso', 'right upper torso',
                               'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve', 'the right sleeve',
                               'right shoulder seam']
    elif category['id'] == 40:
        # human_face from 300W
        updated_point_names = ['upper left cheekbone', 'mid left cheek',
                               'lower left cheek',
                               'upper left jawline', 'mid left jawline',
                               'lower left jawline',
                               'upper left jaw', 'lower left jaw',
                               'the chin',
                               'lower right jaw', 'upper right jaw',
                               'lower right side of low cheek', 'mid side of right low cheek',
                               'upper side of right low cheek',
                               'lower side of right high cheek', 'mid side of right high cheek',
                               'upper right side high cheek',
                               'left end of left eyebrow', 'center left eyebrow',
                               'midpoint of left eyebrow', 'midpoint of left eyebrow',
                               'right end of left eyebrow',
                               'left end of right eyebrow', 'center right eyebrow',
                               'midpoint of right eyebrow', 'midpoint of right eyebrow',
                               'right end of right eyebrow',
                               'top of the nose', 'mid nose', 'mid nose',
                               'lower nose',
                               'the left side of left nostril', 'the right side of left nostril',
                               'nasal septum',
                               'the left side of right nostril', 'the right side of right nostril',
                               'the left side of left eyeball',
                               'upper left side of left eyeball', 'upper right side of left eyeball',
                               'right side of left eyeball',
                               'lower right side of left eyeball', 'lower left side of left eyeball',
                               'the left side of right eyeball',
                               'upper left side of right eyeball', 'upper right side of right eyeball',
                               'the right side of right eyeball corner',
                               'the lower right side of right eyeball', 'the lower left side of right eyeball',
                               'left lip corner', 'upper left lip edge',
                               'upper side of high lip center', 'upper side of high lip center', 'upper side of high lip center',
                               'upper right side of the high lip', 'right lip',
                               'lower right side of low lip',
                               'lower side of the low lip', 'lower side of the low lip', 'lower side of the low lip',
                               'lower left side of the low lip',
                               'left lip corner',
                               'lower side of the high lip', 'lower side of the high lip', 'lower side of the high lip',
                               'right lip',
                               'upper side of the low lip', 'upper side of the low lip', 'upper side of the low lip']
    elif category['id'] == 18:
        updated_point_names = ['left point of left eyebrow', 'mid point of left eyebrow',
                               'right point of left eyebrow end', 'left point of right eyebrow',
                               'mid point of right eyebrow', 'right point of right eyebrow',
                               'left point of left eyeball', 'mid point of left eyeball', 'right point of left eyeball',
                               'left point of right eyeball', 'mid point of right eyeball',
                               'right point of right eyeball', 'left point of the nose', 'nasal bridge',
                               'right point of the nose', 'left lip corner', 'mouth center', 'right lip corner',
                               'the chin']
    elif category['name'] == 'hand':
        updated_point_names = ['wrist',
                               'thumb base', 'thumb lower segment', 'thumb middle segment',
                               'thumb tip', 'index finger base', 'index finger lower segment',
                               'index finger middle segment', 'index finger tip',
                               'middle finger base', 'middle finger lower segment',
                               'middle finger middle segment', 'middle finger tip',
                               'ring finger base', 'ring finger lower segment',
                               'ring finger middle segment', 'ring finger tip',
                               'pinky finger base', 'pinky finger lower segment',
                               'pinky finger middle segment', 'pinky finger tip']
    elif category['name'] == 'locust':
        updated_point_names = [
                                'cranium',  # head
                                'cervical region',  # neck
                                'central section',  # middle part
                                'lower section',  # lower part
                                'caudal appendage',  # tail
                                'extremity of the left antenna',  # tip of the left antenna
                                'origin of the left antenna',  # base of the left antenna
                                'left optic organ',  # left eye
                                'left forelimb',  # front left leg (1)
                                'left forelimb',  # front left leg (2)
                                'left forelimb',  # front left leg (3)
                                'left forelimb',  # front left leg (4)
                                'left middle limb',  # middle left leg (1)
                                'left middle limb',  # middle left leg (2)
                                'left middle limb',  # middle left leg (3)
                                'left middle limb',  # middle left leg (4)
                                'left hind limb',  # back left leg (1)
                                'left hind limb',  # back left leg (2)
                                'left hind limb',  # back left leg (3)
                                'left hind limb',  # back left leg (4)
                                'extremity of the right antenna',  # tip of the right antenna
                                'origin of the right antenna',  # base of the right antenna
                                'right optic organ',  # right eye
                                'right forelimb',  # front right leg (1)
                                'right forelimb',  # front right leg (2)
                                'right forelimb',  # front right leg (3)
                                'right forelimb',  # front right leg (4)
                                'right middle limb',  # middle right leg (1)
                                'right middle limb',  # middle right leg (2)
                                'right middle limb',  # middle right leg (3)
                                'right middle limb',  # middle right leg (4)
                                'right hind limb',  # back right leg (1)
                                'right hind limb',  # back right leg (2)
                                'right hind limb',  # back right leg (3)
                                'right hind limb'  # back right leg (4)
                            ]
    elif category['name'] == "fly":
        updated_point_names = ['cranium',  # head
                                'left optic organ',  # left eye
                                'right optic organ',  # right eye
                                'cervical region',  # neck
                                'chest',  # thorax
                                'belly',  # abdomen
                                'right forelimb',  # front right leg
                                'origin of the right forelimb',  # start point of the front right leg
                                'midsection of the right forelimb',  # middle point of the front right leg
                                'near the tip of the right forelimb',  # almost the end point of the front right leg
                                'tip of the right forelimb',  # end point of the front right leg
                                'origin of the right middle leg',  # start point of the middle right leg
                                'midsection of the right middle leg',  # middle point of the middle right leg
                                'near the tip of the right middle leg',  # almost the end point of the middle right leg
                                'tip of the right middle leg',  # end point of the middle right leg
                                'origin of the right hind limb',  # start point of the back right leg
                                'midsection of the right hind limb',  # middle point of the back right leg
                                'near the tip of the right hind limb',  # almost the end point of the back right leg
                                'tip of the right hind limb',  # end point of the back right leg
                                'origin of the left forelimb',  # start point of the front left leg
                                'midsection of the left forelimb',  # middle point of the front left leg
                                'near the tip of the left forelimb',  # almost the end point of the front left leg
                                'tip of the left forelimb',  # end point of the front left leg
                                'origin of the left middle leg',  # start point of the middle left leg
                                'midsection of the left middle leg',  # middle point of the middle left leg
                                'near the tip of the left middle leg',  # almost the end point of the middle left leg
                                'tip of the left middle leg',  # end point of the middle left leg
                                'origin of the left hind limb',  # start point of the back left leg
                                'midsection of the left hind limb',  # middle point of the back left leg
                                'near the tip of the left hind limb',  # almost the end point of the back left leg
                                'tip of the left hind limb',  # end point of the back left leg
                                'left wing appendage',  # left wing
                                'right wing appendage'  # right wing
                            ]
    else:
        print(f"{category['name']} was not changed. Exiting...")
        exit(-1)
        updated_point_names = category['keypoints']
        updated_point_names = [k.replace("_", " ") for k in updated_point_names]


    return updated_point_names


def translate_test(category):
    updated_point_names = []
    if category['name'] in ['antelope_body', 'beaver_body', 'bison_body', 'bobcat_body', 'cat_body', 'cheetah_body',
                            'cow_body', 'deer_body', 'dog_body', 'elephant_body', 'fox_body', 'giraffe_body',
                            'gorilla_body', 'hamster_body', 'hippo_body', 'horse_body', 'leopard_body', 'lion_body',
                            'otter_body', 'panda_body', 'panther_body', 'pig_body', 'polar_bear_body', 'rabbit_body',
                            'raccoon_body', 'rat_body', 'rhino_body', 'sheep_body', 'skunk_body', 'spider_monkey_body',
                            'squirrel_body', 'weasel_body', 'wolf_body', 'zebra_body']:
        updated_point_names = ['left eye', 'right eye', 'nose', 'neck', 'base of the tail', 'left shoulder',
                               'left elbow', 'left front paw', 'right shoulder', 'right elbow', 'right front paw',
                               'left hip', 'left knee', 'left rear paw', 'right hip', 'right knee', 'right rear paw']
    elif category['name'] in ["human_body", "person", "macaque"]:
        updated_point_names = ['nose', 'left eye', 'right eye', 'left ear', 'right ear', 'left shoulder',
                               'right shoulder', 'left elbow', 'right elbow', 'left wrist', 'right wrist',
                               'left hip', 'right hip', 'left knee', 'right knee', 'left ankle', 'right ankle']
    elif category['supercategory'] == 'bird':
        updated_point_names = ['back', 'beak', 'belly', 'chest', 'top of the head', 'forehead', 'left eye', 'left leg',
                               'left wing', 'back of the neck', 'right eye', 'right leg', 'right wing', 'tail', 'neck']
    elif category['supercategory'] == 'animal_face':
        updated_point_names = ['top left corner of the left eye', 'bottom right corner of the left eye',
                               'bottom left corner of the right eye', 'top right corner of the right eye',
                               'tip of the nose', 'left side of the mouth', 'right side of the mouth',
                               'upper side of the mouth', 'lower side of the mouth']
    elif category['name'] == 'sofa':
        updated_point_names = ['left rear leg', 'left front leg', 'left rear side of the seat',
                               'left front side of the seat', 'rear side of the left armrest',
                               'front side of the left armrest', 'top left corner of the backrest',
                               'right rear leg', 'right front leg', 'right rear side of the seat',
                               'right front side of the seat', 'rear side of the right armrest',
                               'front side of the right armrest', 'top right corner of the backrest']
    elif category['name'] == 'chair':
        updated_point_names = ['left front leg', 'right front leg', 'right rear leg',
                               'left rear leg', 'left front side of the seat',
                               'right front side of the seat', 'right rear side of the seat',
                               'left rear side of the seat', 'top left corner of the backrest',
                               'top right corner of the backrest']
    elif category['name'] == 'bed':
        updated_point_names = ['left rear leg', 'left front leg', 'left rear side of the mattress',
                               'left front side of the mattress', 'top left corner of the headboard',
                               'right rear leg', 'right front leg', 'right rear side of the mattress',
                               'right front side of the mattress', 'top right corner of the headboard']
    elif category['name'] == 'swivelchair':
        updated_point_names = ['wheel', 'wheel', 'wheel', 'wheel', 'wheel', 'center of the wheels',
                               'center of the seat', 'left front side of the seat',
                               'right front side of the seat', 'right rear side of the seat',
                               'left rear side of the seat', 'top left corner of the backrest',
                               'top right corner of the backrest']
    elif category['name'] == 'table':
        updated_point_names = ['left front corner of the top', 'left rear corner of the top',
                               'right front corner of the top', 'right rear corner of the top',
                               'left front leg', 'left rear leg', 'right front leg',
                               'right rear leg']
    elif category['supercategory'] == 'vehicle':
        # windshield is not present in the skeleton and should be ignored.
        updated_point_names = ['front right wheel', 'front left wheel', 'rear right wheel',
                               'rear left wheel', 'right headlight', 'left headlight', 'right taillight',
                               'left taillight', 'windshield', 'front right corner of the roof',
                               'front left corner of the roof', 'rear right corner of the roof',
                               'rear left corner of the roof']
    elif category['name'] == 'skirt':
        updated_point_names = ['top left corner of the skirt', 'top side of the skirt', 'top right corner of the skirt',
                               'left side of the skirt', 'bottom left corner of the skirt', 'bottom side of the skirt',
                               'bottom right corner of the skirt', 'right side of the skirt']
    elif category['name'] == 'short_sleeved_outwear':
        updated_point_names = ['back side of the collar', 'top left corner of the placket',
                               'front left side of the collar',
                               'left side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left side of the shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left upper body of the shirt',
                               'left lower body of the shirt', 'bottom left corner of the shirt',
                               'bottom left corner of the placket', 'bottom right corner of the shirt',
                               'right lower body of the shirt', 'right upper body of the shirt',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right side of the shoulder seam', 'top right corner of the collar',
                               'upper right corner of the placket', 'lower right corner of the placket',
                               'bottom right corner of the placket', 'upper left corner of the placket',
                               'lower left corner of the placket']
    elif category['name'] == 'long_sleeved_outwear':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                               'top left corner of the placket',
                               'front right side of the collar', 'right side of the collar',
                               'left side of the shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left upper body of the shirt',
                               'left lower body of the shirt', 'bottom left corner of the shirt',
                               'bottom left corner of the placket', 'bottom right corner of the shirt',
                               'right lower body of the shirt', 'right upper body of the shirt',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right side of the shoulder seam', 'top right corner of the placket',
                               'upper right corner of the placket', 'lower right corner of the placket',
                               'bottom right corner of the placket', 'upper left corner of the placket',
                               'lower left corner of the placket']
    elif category['name'] == 'sling':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                               'front side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left shoulder strap', 'left upper body of the shirt', 'left lower body of the shirt',
                               'bottom left corner of the shirt', 'bottom side of the shirt',
                               'bottom right corner of the shirt', 'lower right side of the shirt',
                               'upper right body of the shirt', 'right shoulder strap']

    elif category['name'] == 'sling_dress':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                               'front side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left strap', 'left upper body of the dress', 'left upper body of the dress',
                               'left side of the dress', 'lower left side of the dress',
                               'bottom left corner of the dress', 'bottom side of the dress',
                               'bottom right corner of the dress', 'lower right side of the dress',
                               'right side of the dress', 'right upper body of the dress',
                               'right upper body of the dress', 'right strap']
    elif category['name'] == 'long_sleeved_dress':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                               'front side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left side of the shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left upper body of the dress',
                               'left upper body of the dress', 'left side of the dress',
                               'left lower body of the dress', 'bottom left corner of the dress',
                               'bottom side of the dress', 'bottom right corner of the dress',
                               'right lower body of the dress', 'right side of the dress',
                               'right upper body of the dress', 'right upper body of the dress',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right side of the shoulder seam']
    elif category['name'] == 'short_sleeved_dress':
        updated_point_names = ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                               'front side of the collar', 'front right side of the collar', 'right side of the collar',
                               'left side of the shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left upper body of the dress',
                               'left upper body of the dress', 'left side of the dress',
                               'left lower body of the dress', 'bottom left corner of the dress',
                               'bottom side of the dress', 'bottom right corner of the dress',
                               'right lower body of the dress', 'right side of the dress',
                               'right upper body of the dress', 'right upper body of the dress',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right side of the shoulder seam']
    elif category['name'] == 'vest':
        updated_point_names = ['back of the collar', 'left collar side', 'front left collar side',
                               'front of the collar', 'front right collar side', 'right collar side',
                               'left shoulder', 'upper left body of the shirt', 'lower left body of the shirt',
                               'bottom left of the shirt', 'bottom of the shirt',
                               'bottom right of the shirt', 'lower right of the shirt',
                               'upper right body of the shirt', 'right shoulder']

    elif category['name'] == 'vest_dress':
        updated_point_names = ['back of the collar', 'left collar side', 'front left collar side',
                               'front of the collar', 'front right collar side', 'right collar side',
                               'left shoulder', 'upper left body of the dress', 'upper left body of the dress',
                               'left body of the dress', 'lower left body of the dress',
                               'bottom left of the dress', 'bottom of the dress',
                               'bottom right of the dress', 'lower right body of the dress',
                               'right body of the dress', 'upper right body of the dress',
                               'upper right body of the dress', 'right shoulder']

    elif category['name'] == 'long_sleeved_shirt':
        updated_point_names = ['back of the collar', 'left collar side', 'front left collar side',
                               'front of the collar', 'front right collar side', 'right collar side',
                               'left shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left upper body of the shirt',
                               'left lower body of the shirt', 'bottom left of the shirt',
                               'bottom of the shirt', 'bottom right of the shirt',
                               'right lower body of the shirt', 'right upper body of the shirt',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right shoulder seam']

    elif category['name'] == 'shorts':
        updated_point_names = ['top left of the pants', 'top of the pants', 'top right of the pants',
                               'left side of the pants', 'left side of the left leg opening',
                               'right side of the left leg opening', 'crotch', 'left side of the right leg opening',
                               'right side of the right leg opening', 'right side of the pants']

    elif category['name'] == 'trousers':
        updated_point_names = ['top left of the pants', 'top of the pants', 'top right of the pants',
                               'upper left of the pants', 'lower left of the pants',
                               'left side of the left leg opening', 'right side of the left leg opening',
                               'lower left of the pants', 'crotch', 'lower right of the pants',
                               'left side of the right leg opening', 'right side of the right leg opening',
                               'lower right of the pants', 'upper right of the pants']

    elif category['name'] == 'short_sleeved_shirt':
        updated_point_names = ['back of the collar', 'left collar side', 'front left collar side',
                               'front of the collar', 'front right collar side', 'right collar side',
                               'left shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve',
                               'left sleeve', 'left sleeve', 'left upper body of the shirt',
                               'left lower body of the shirt', 'bottom left of the shirt',
                               'bottom of the shirt', 'bottom right of the shirt',
                               'right lower body of the shirt', 'right upper body of the shirt',
                               'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                               'right shoulder seam']

    elif category['id'] == 40:
        updated_point_names = ['top of the upper left cheek', 'middle of the upper left cheek',
                               'bottom of the upper left cheek',
                               'top of the lower left cheek', 'middle of the lower left cheek',
                               'bottom of the lower left cheek',
                               'top of the left jaw', 'bottom of the left jaw',
                               'chin',
                               'bottom of the right jaw', 'top of the right jaw',
                               'bottom of the lower right cheek', 'middle of the lower right cheek',
                               'top of the lower right cheek',
                               'bottom of the upper right cheek', 'middle of the upper right cheek',
                               'top of the upper right cheek',
                               'left eyebrow side', 'middle of the left eyebrow',
                               'middle of the left eyebrow', 'middle of the left eyebrow',
                               'right eyebrow side',
                               'left side of the right eyebrow', 'middle of the right eyebrow',
                               'middle of the right eyebrow', 'middle of the right eyebrow',
                               'right side of the right eyebrow',
                               'top of the nose', 'middle of the nose', 'middle of the nose',
                               'bottom of the nose',
                               'left side of the left nostril', 'right side of the left nostril',
                               'middle of the nostrils',
                               'left side of the right nostril', 'right side of the right nostril',
                               'left side of the left eye',
                               'top left of the left eye', 'top right of the left eye',
                               'right side of the left eye',
                               'bottom right of the left eye', 'bottom left of the left eye',
                               'left side of the right eye',
                               'top left of the right eye', 'top right of the right eye',
                               'right side of the right eye',
                               'bottom right of the right eye', 'bottom left of the right eye',
                               'left side of the lips', 'top left of the upper lip',
                               'top of the upper lip', 'top of the upper lip', 'top of the upper lip',
                               'top right of the upper lip', 'right side of the lips',
                               'bottom right of the lower lip',
                               'bottom of the lower lip', 'bottom of the lower lip', 'bottom of the lower lip',
                               'bottom left of the lower lip',
                               'left side of the lips',
                               'bottom of the upper lip', 'bottom of the upper lip', 'bottom of the upper lip',
                               'right side of the lips',
                               'top of the lower lip', 'top of the lower lip', 'top of the lower lip']

    elif category['id'] == 18:
        updated_point_names = ['left side of the left eyebrow', 'middle of the left eyebrow',
                               'right side of the left eyebrow', 'left side of the right eyebrow',
                               'middle of the right eyebrow', 'right side of the right eyebrow',
                               'left side of the left eye', 'middle of the left eye', 'right side of the left eye',
                               'left side of the right eye', 'middle of the right eye',
                               'right side of the right eye', 'left side of the nose', 'middle of the nostrils',
                               'right side of the nose', 'left side of the lips', 'mouth', 'right side of the lips',
                               'chin']

    elif category['name'] == 'hand':
        updated_point_names = ['wrist',
                               'base of the thumb', 'lower thumb', 'middle thumb',
                               'top thumb', 'base of the index finger', 'lower index finger',
                               'middle index finger', 'top index finger',
                               'base of the middle finger', 'lower middle finger',
                               'middle middle finger', 'top middle finger',
                               'base of the ring finger', 'lower ring finger',
                               'middle ring finger', 'top ring finger',
                               'base of the pinky finger', 'lower pinky finger',
                               'middle pinky finger', 'top pinky finger']

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

    elif category['name'] == 'fly':
        updated_point_names = ['head', 'left eye', 'right eye', 'neck', 'thorax', 'abdomen', 'front right leg',
                               'starting point of the front right leg', 'middle of the front right leg',
                               'almost the end of the front right leg', 'end of the front right leg',
                               'starting point of the middle right leg', 'middle of the middle right leg',
                               'almost the end of the middle right leg', 'end of the middle right leg',
                               'starting point of the back right leg', 'middle of the back right leg',
                               'almost the end of the back right leg', 'end of the back right leg',
                               'starting point of the front left leg', 'middle of the front left leg',
                               'almost the end of the front left leg', 'end of the front left leg',
                               'starting point of the middle left leg', 'middle of the middle left leg',
                               'almost the end of the middle left leg', 'end of the middle left leg',
                               'starting point of the back left leg', 'middle of the back left leg',
                               'almost the end of the back left leg', 'end of the back left leg',
                               'left wing', 'right wing']
    else:
        print(f"{category['name']} was not changed. Exiting...")
        exit(-1)
        updated_point_names = category['keypoints']
        updated_point_names = [k.replace("_", " ") for k in updated_point_names]

    return updated_point_names

def typo_test(category):
    if category['name'] in ['antelope_body', 'beaver_body', 'bison_body', 'bobcat_body', 'cat_body', 'cheetah_body',
                            'cow_body', 'deer_body', 'dog_body', 'elephant_body', 'fox_body', 'giraffe_body',
                            'gorilla_body', 'hamster_body', 'hippo_body', 'horse_body', 'leopard_body', 'lion_body',
                            'otter_body', 'panda_body', 'panther_body', 'pig_body', 'polar_bear_body', 'rabbit_body',
                            'raccoon_body', 'rat_body', 'rhino_body', 'sheep_body', 'skunk_body', 'spider_monkey_body',
                            'squirrel_body', 'weasel_body', 'wolf_body', 'zebra_body']:
        updated_point_names = ['left eey', 'right eyee', 'nosse', 'necck', 'root of taill', 'left shoullder', 'left elbwo',
                               'left front paww', 'right shooulder', 'right ellbow', 'right front paaw', 'left hipp',
                               'left kneee', 'left back pawe', 'right hiip', 'right knnee', 'right back ppaw']
    elif category['name'] in ["human_body", "person", "macaque"]:
        updated_point_names = ['nosee', 'leeft eye', 'right eyye', 'leftt ear', 'right earr', 'left shooulder',
                               'righht shoulder', 'left elbbow', 'right elboow', 'left wwrist', 'right wrsit',
                               'left hipp', 'right heip', 'left knnee', 'right nee', 'left ankel', 'right aknle']
    elif category['supercategory'] == 'bird':
        updated_point_names = ['bakc', 'beakk', 'bellyy', 'breasst', 'crownn', 'forehed', 'left eey', 'left legg',
                               'left wingg', 'nappe', 'right eyee', 'right leeg', 'right winng', 'taill', 'throatt']

    elif category['supercategory'] == 'animal_face':
        updated_point_names = ['top left side of the left eey', 'bottom right side of the lft eye',
                               'bottom lfet side of the right eye', 'top righ side of the right eye',
                               'noose tip', 'left sidee of the lip', 'right side of the lipp', 'top side of the llip',
                               'botom side of the lip']
    elif category['name'] == 'sofa':
        updated_point_names = ['left and bakc leg', 'left and front leeg', 'left and back side of the sit',
                               'left and front side of the seet', 'back side of the left armrst',
                               'frnt side of the left armrest', 'top letf side of the backrest',
                               'right and beck leg', 'right and froont leg', 'right and back side of the sseat',
                               'right and front side of the seaat', 'back side of the right armmrest',
                               'front side of the right armresst', 'top right side of the bcakrest']
    elif category['name'] == 'chair':
        updated_point_names = ['left and frront leg', 'rite and front leg', 'rigt and back leg',
                               'left and back legg', 'left and front side of the saet',
                               'right and fornt side of the seat', 'right and back sdie of the seat',
                               'left and back side of the seaat', 'top left side of the bakseat',
                               'top right side of the backseat']
    elif category['name'] == 'bed':
        updated_point_names = ['left and bakc leg', 'left and fronnt leg', 'left and back side of the matress',
                               'left and front side of the mattres', 'top left side of the headbord',
                               'right and bacc leg', 'right and frunt leg', 'right and back side of the mattreess',
                               'right and front side of the mattrress', 'top right side of the hedboard']
    elif category['name'] == 'swivelchair':
        updated_point_names = ['whel', 'weel', 'wehel', 'whele', 'whil', 'centr of the wheels',
                               'cnter of the seat', 'left and frnt side of the seat',
                               'rght and front side of the seat', 'right and back side of the seet',
                               'left and back siide of the seat', 'top left side of the back rst',
                               'toop right side of the backrest']
    elif category['name'] == 'table':
        updated_point_names = ['left and fronnt side of the top', 'left and bck side of the top',
                               'right and front side off the top', 'rite and back side of the top',
                               'left and frontt leg', 'left and bakk leg', 'right and front lleg',
                               'right and back legg']
    elif category['supercategory'] == 'vehicle':
        # windshield is not present in the skeleton and should be ignored.
        updated_point_names = ['front and right wheeel', 'front and left wheell', 'reer and right wheel',
                               'rear and left wwheel', 'right headligh', 'left headligt', 'right tailight',
                               'left tailliht', 'windshild', 'front and right sidde of the top',
                               'front and left side of the topp', 'raer and right side of the top',
                               'rrear and left side of the top']
    elif category['name'] == 'skirt':
        updated_point_names = ['top left side of the skrit', 'top side of the skrt', 'top rigth side of the skirt',
                               'left side of the sikrt', 'botom left side of the skirt', 'bttom side of the skirt',
                               'bottm right side of the skirt', 'right side of the skrt']
    elif category['name'] == 'short_sleeved_outwear':
        updated_point_names = ['back side of the collr', 'top left side of the plackt', 'front left side of the colar',
                               'left side of the cllar', 'front right side of the collaar', 'right side of the coollar',
                               'left side of the shoulder seem', 'left sleve', 'left sleeeve', 'left sleevve',
                               'left slleeve', 'left sleev', 'left and uper body of the shirt',
                               'left and lowr body of the shirt', 'bottom left side of the shrt',
                               'bottm left side of the shirt placket', 'bottom right side of the shert',
                               'right and lowr body of the shirt', 'right and upper boody of the shirt',
                               'right sleevee', 'right ssleeve', 'righht sleeve', 'rigght sleeve', 'right sleave',
                               'right side of the sholder seam', 'top right side of the colllar',
                               'uper right side of the shirt placket', 'lower right side of the shirt plackeet',
                               'bottom right side of the shirt plackett', 'upper left side of the shirt plackket',
                               'lower left side of the shirrt placket']
    elif category['name'] == 'long_sleeved_outwear':
        updated_point_names = ['back side of the collaar', 'left side of the colar', 'front left side ofthe collar',
                               'top left side of the placket', 'front right sdie of the collar', 'right sid of the collar',
                               'left side of the shulder seam', 'left slieeve', 'left slevee', 'left sleve',
                               'left slleeve', 'left ssleeve', 'left sleevee', 'letf sleeve', 'let sleeve', 'lft sleeve',
                               'left and upper bodyy of the shirt', 'left and lower boddy of the shirt',
                               'bottoom left side of the shirt', 'bottem left side of the shirt placket',
                               'bottum right side of the shirt', 'right and lowr body of the shirt',
                               'right and uppeer body of the shirt', 'right ssleeve', 'right sleeive', 'right sleve',
                               'riight sleeve', 'right sleev', 'rigth sleeve', 'right slleeve', 'rigght sleeve',
                               'right sleevve', 'right side of the shouldr seam', 'top right side of the plaket',
                               'upper right side of the shert placket', 'lower right side of the shrit placket',
                               'battom right side of the shirt placket', 'upperr left side of the shirt placket',
                               'loweer left side of the shirt placket']
    elif category['name'] == 'sling':
        updated_point_names = ['back side of thee collar', 'left side oof the collar', 'frant left side of the collar',
                               'frotn side of the collar', 'front right side of the collr', 'right side of the cllar',
                               'left shouldr strap', 'upper left body of the shart', 'lowar left body of the shirt',
                               'bottom left sider of the shirt', 'buttom side of the shirt',
                               'bottom right side uf the shirt', 'lowerl right side of the shirt',
                               'upper right side of the sihrt', 'right shouldeer strap']

    elif category['name'] == 'sling_dress':
        updated_point_names = ['bck side of the collar', 'lefft side of the collar', 'front left side of the cullar',
                               'frunt side of the collar', 'frant right side of the collar', 'raght side of the collar',
                               'left straap', 'upper left body of the dres', 'upper left body of the dreess',
                               'left body of the dresss', 'lower left side of the drress',
                               'battom left side of the dress', 'bottem side of the dress',
                               'bettom right side of the dress', 'lowir right side of the dress',
                               'right bady of the dress', 'apper right body of the dress',
                               'uppir right body of the dress', 'reght strap']
    elif category['name'] == 'long_sleeved_dress':
        updated_point_names = ['backc side of the collar', 'left f side of the collar', 'front left side of the coller',
                               'front side fo the collar', 'frontt right side of the collar', 'riight side of the collar',
                               'left side of the soulder seam', 'left sleve', 'left sIeeve', 'left ssleeve',
                               'left sleeveee', 'left sleevve', 'left sleevee', 'left g sleeve',
                               'left slevve', 'left slevee', 'left nd upper body of the dress',
                               'left andd upper body of the dress', 'left bodey of the dress',
                               'left and lower bodiy of the dress', 'bottom left side of the dres',
                               'bettom side of the dress', 'bottom right side of the drss',
                               'right and loower body of the dress', 'right budy of the dress',
                               'right and upperr body of the dress', 'right and upper budy of the dress',
                               'right slleeve', 'rigt sleeve', 'right k sleeve', 'rigt sleeve', 'right sleeev',
                               'right sliv', 'righht sleeve', 'right sleve', 'right sleeveee',
                               'right side of the shoalder seam']
    elif category['name'] == 'short_sleeved_dress':
        updated_point_names = ['back side the collar', 'left side of the ccollar', 'front left side of the collaar',
                               'front side of thee collar', 'front righte side of the collar', 'rght side of the collar',
                               'left side of the shouldeer seam', 'left ssleeve', 'left slleeve', 'left sleeeve',
                               'left sleevve', 'left sleevee', 'left and uupper body of the dress',
                               'left and upper body of the dreess', 'left body of the dresss',
                               'left and loower body of the dress', 'bottoom left side of the dress',
                               'bottom side of the ddress', 'bottom right side of tthe dress',
                               'right and lowar body of the dress', 'right boedy of the dress',
                               'right and upper body of the dreass', 'right and upper bodi of the dress',
                               'right sleieve', 'rigt sleeve', 'rright sleeve', 'righet sleeve', 'right c sleeve',
                               'right side of the shoulder seeam']
    elif category['name'] == 'vest':
        updated_point_names = ['back sidee of the collar', 'lefft side of the collar', 'front left siide of the collar',
                               'front side of the colllar', 'front right side of th collar', 'right side of the collr',
                               'left shouldar', 'upper left body of the shiert', 'lower left body of the shirtt',
                               'bottom left side of the shirrt', 'bottim side of the shirt',
                               'bittom right side of the shirt', 'loawer right side of the shirt',
                               'uppar right side of the shirt', 'right shouldere']
    elif category['name'] == 'vest_dress':
        updated_point_names = ['baack side of the collar', 'left saide of the collar', 'front left side uf the collar',
                               'front side of the collaer', 'front right side of the collare', 'rieght side of the collar',
                               'left shouelder', 'upper left body of the dresss', 'uppere left body of the dress',
                               'left body of the drass', 'lower left body of the dreass',
                               'bottome left side of the dress', 'bottoam side of the dress',
                               'boattom right side of the dress', 'lowere right side of the dress',
                               'right side of the deress', 'upper right side of the derss',
                               'uppr right side of the dress', 'righ shoulder']

    elif category['name'] == 'long_sleeved_shirt':
        updated_point_names = ['back side of tha collar', 'left siede of the collar', 'front left side of the coallar',
                               'front side of the colloar', 'front right sidee of the collar', 'rigght side of the collar',
                               'lfet side of the shoulder seam', 'lft sleeve', 'left sleeve', 'left sleve',
                               'left sleeev', 'left sleev', 'left slleeve', 'left sleave',
                               'left s leeve', 'left slee ve', 'left and upper body of the shiirt',
                               'left and low er body of the shirt', 'bottm left side of the shirt',
                               'bottom side of the shirte', 'bottom right side of the shiert',
                               'rig ht and lower body of the shirt', 'right and upp-r body of the shirt',
                               'rigth sleeve', 'right sleeve', 'rgiht sleeve', 'rght sleeve', 'right sleav',
                               'right slive', 'rright sleeve', 'rightt sleeve', 'righ t sleeve',
                               'right side of the shuolder seam']

    elif category['name'] == 'shorts':
        updated_point_names = ['top left side of the pnts', 'top side of the pnats', 'top right side of the panst',
                               'left side of the ppants', 'left side of the left leg openig',
                               'right side of the left leg oppening', 'cruttch', 'left side of the right leeg opening',
                               'right side of the right leg oppening', 'right side of the pantss']
    elif category['name'] == 'trousers':
        updated_point_names = ['top leeft side of the pants', 'top side of the pannts', 'top right side of the ppants',
                               'upper left sidde of the pants', 'lower left side of the patns',
                               'left side of the left leg opeening', 'right side of the left leg openning',
                               'lower left side of the pant s', 'crutchh', 'lowerr right side of the pants',
                               'left side of the right leg openingg', 'right side of the right leg oppening',
                               'lower right side of the pantts', 'upper right side of the pantss']
    elif category['name'] == 'short_sleeved_shirt':
        updated_point_names = ['bakc side of the collar', 'left siide of the collar', 'front left side of the colllar',
                               'front side of the collaar', 'front right side of the ccollar', 'rigt side of the collar',
                               'left side of the shoulder seeam', 'left sleeave', 'left slleeve', 'left sleevee',
                               'left sleevve', 'left ssleeve', 'left and uppeer body of the shirt',
                               'leftt and lower body of the shirt', 'bottom left side of the shirte',
                               'bottom side of the shiret', 'bottom right side of the shirtt',
                               'right and lowr body of the shirt', 'right and uppr body of the shirt',
                               'rght sleeve', 'right sleevve', 'rightt sleeve', 'right sleevee', 'right sleeeve',
                               'right side of the shouldar seam']
    elif category['id'] == 40:
        # human_face from 300W
        updated_point_names = ['top side of the upper left cheeck', 'middle side of the upper left cheec',
                               'bottom side of the upper left cheak',
                               'top side of the lower left cheeek', 'middle side of the lower left chieek',
                               'bottom side of the lower left chheek',
                               'top side of the left jaaw', 'bottom side of the left jjaw',
                               'chiin',
                               'bottom side of the right jaww', 'top side of the right jaaw',
                               'bottom side of the lower righte cheek', 'middle side of the lower rigt cheek',
                               'top side of the lowe right cheek',
                               'bottom side of the upper right chik', 'middle side of the upper right cheeek',
                               'top side of the upper right cheekk',
                               'left side of the left eeybrow', 'middle side of the left eyebroww',
                               'middle side of the left eyebbrow', 'middle side of the left eyeebrow',
                               'right side of the left eyyebrow',
                               'left side of the right eyebroow', 'middle side of the right eyebrowe',
                               'middle side of the right eeyebrow', 'middle side of the right eeybrow',
                               'right side of the right eiyebrow',
                               'top side of the noose', 'middle side of the nosse', 'middle side of the nosee',
                               'bottom side of the nnose',
                               'left side of the left nostrill', 'right side of the left nosstril',
                               'middle of the nosttrils',
                               'left side of the right nnostril', 'right side of the right noostril',
                               'left side of the left eyee',
                               'top left side of the left eeye', 'top right side of the left eyye',
                               'right side of the left eeye',
                               'bottom right side of the left eye', 'bottom left side of the left ey',
                               'left side of the right eeye',
                               'top left side of the riht eye', 'top right sidde of the right eye',
                               'right side of the right eyee',
                               'bottom right side of the rright eye', 'bottm left side of the right eye',
                               'left side of the lipps', 'top left side of the upper liip',
                               'top side of the upper llip', 'top side of the upper liep', 'top side of the uper lip',
                               'topp right side of the upper lip', 'right side of th lips',
                               'bottoam right side of the bottom lip',
                               'boattom side of the lower lip', 'bottom side of the loweer lip', 'bottom side off the lower lip',
                               'bottom left side of the lower lipp',
                               'left side of the lisp',
                               'bottom side of the apper lip', 'bottom sidde of the upper lip', 'bbottom side of the upper lip',
                               'rgiht side of the lips',
                               'top side of the lowere lip', 'top sied of the lower lip', 'top side oof the lower lip'
                               ]
    elif category['id'] == 18:
        updated_point_names = ['left side of the left eyebroow', 'middle side of the left eyyebrow',
                               'right side of the left eyeebrow', 'left side of the right eeyebrow',
                               'midle side of the right eyebrow', 'right side of the right eyebreow',
                               'left side of the lefft eye', 'middle side of the left eyee', 'right side of the leftt eye',
                               'left side of the rigt eye', 'mieddle side of the right eye',
                               'raght side of the right eye', 'left side of the noose', 'middle of the noastrils',
                               'right side of the noase', 'left side of the leeps', 'moouth', 'rigght side of the lips',
                               'chin']
    elif category['name'] == 'hand':
        updated_point_names = ['wwrist',
                               'basse of the thumb', 'lower part of the thummb', 'middle part of the thuumb',
                               'top part of the tthumb', 'base of the index ffinger', 'lower part of the indeex finger',
                               'middle part of the iindex finger',  'top part of the inndex finger',
                               'base of the middlle finger', 'lower part of the midlle finger',
                               'middle prt of the middle finger', 'top part of the middl finger',
                               'base of the ringg finger', 'lower part of the riing finger',
                               'middle part of the rring finger', 'top partt of the ring finger',
                               'base of the pinkey finger', 'lower part of the pinkiy finger',
                               'middle part of the pincky finger', 'top part of the ppinky finger'
                               ]
    elif category['name'] == 'locust':
        updated_point_names = ['headd', 'neckk', 'midle part', 'lowr part', 'taail',
                               'tipp of the left antenna', 'basse of the left antenna', 'left eyee',
                               'front left legg', 'frnot left leg', 'front lefft leg', 'front left leeg',
                               'mieddle left leg', 'middl left leg', 'mddle left leg', 'middle lleft leg',
                               'bck left leg', 'back leeft leg', 'bakc left leg', 'bacck left leg',
                               'tip of the right antena', 'base of the right anteenna', 'right eeye',
                               'frontt right leg', 'front righht leg', 'front riight leg', 'front reight leg',
                               'mmiddle right leg', 'midddle right leg', 'middel right leg', 'midel right leg',
                               'back rright leg', 'back raight leg', 'back right lleg', 'back righht leg']

    elif category['name'] == 'fly':
        updated_point_names = ['heead', 'lefft eye', 'rightt eye', 'necck', 'thoraxx', 'abbdomen', 'front right leeg',
                               'strat point of the front right leg', 'mieddle point of the front right leg',
                               'almst the end point of the front right leg', 'end piont of the front right leg',
                               'satrt point of the middle right leg', 'middel point of the middle right leg',
                               'allmost the end point of the middle right leg', 'end poinnt of the middle right leg',
                               'startt point of the back right leg', 'midle point of the back right leg',
                               'almost the end point of the backk right leg', 'endd point of the back right leg',
                               'starrt point of the front left leg', 'middle pooint of the front left leg',
                               'almost the end poiint of the front left leg', 'end poinnt of the front left leg',
                               'start pointt of the middle left leg', 'mmiddle point of the middle left leg',
                               'aalmost the end point of the middle left leg', 'ennd point of the middle left leg',
                               'start point of the baack left leg', 'middl point of the back left leg',
                               'almostt the end point of the back left leg', 'endd point of the back left leg',
                               'left wiing', 'right winng']

    else:
        print(f"{category['name']} was not changed. Exiting...")
        exit(-1)

        updated_point_names = category['keypoints']
        updated_point_names = [k.replace("_", " ") for k in updated_point_names]
    return updated_point_names


def get_custom_graph_from_llm(img_metas):
    texts = list(img_metas[0]['query_point_descriptions'])
    edges = None
    if texts == ['top left side of the left eye', 'bottom right side of the left eye',
                 'bottom left side of the right eye', 'top right side of the right eye',
                 'nose tip', 'left side of the lip', 'right side of the lip',
                 'top side of the lip', 'bottom side of the lip']:
        edges = [[0, 1], [2, 3], [0, 4], [3, 4], [1, 4], [2, 4], [5, 6], [5, 7], [6, 7], [5, 8], [6, 8]]
    elif texts == ['left eye', 'right eye', 'nose', 'neck', 'root of tail', 'left shoulder', 'left elbow',
                   'left front paw', 'right shoulder', 'right elbow', 'right front paw', 'left hip', 'left knee',
                   'left back paw', 'right hip', 'right knee', 'right back paw']:
        edges = [[0, 2], [1, 2], [2, 3], [3, 5], [3, 8], [5, 6], [6, 7], [8, 9], [9, 10],
                 [3, 4], [4, 11], [4, 14], [11, 12], [12, 13], [14, 15], [15, 16]]
    elif texts == ['back', 'beak', 'belly', 'breast', 'crown', 'forehead', 'left eye', 'left leg', 'left wing',
                   'nape', 'right eye', 'right leg', 'right wing', 'tail', 'throat']:
        edges = [[0, 9], [9, 4], [4, 5], [5, 6], [5, 10], [6, 3], [10, 3], [3, 14], [14, 1], [3, 2], [2, 7], [2, 11],
                 [0, 13], [0, 8], [0, 12]]
    elif texts == ['wheel', 'wheel', 'wheel', 'wheel', 'wheel', 'center of the wheels', 'center of the seat',
                   'left and front side of the seat', 'right and front side of the seat',
                   'right and back side of the seat', 'left and back side of the seat',
                   'top left side of the backrest', 'top right side of the backrest']:
        edges = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 6], [6, 7], [6, 8], [6, 9], [6, 10], [7, 8], [9, 10],
                 [10, 11], [7, 11], [8, 12], [9, 12], [11, 12]]
    elif texts == ['left and back leg', 'left and front leg', 'left and back side of the mattress',
                   'left and front side of the mattress', 'top left side of the headboard', 'right and back leg',
                   'right and front leg', 'right and back side of the mattress', 'right and front side of the mattress',
                   'top right side of the headboard']:
        edges = [[0, 2], [1, 3], [2, 3], [2, 4], [3, 4], [5, 7], [6, 8], [7, 8], [7, 9], [8, 9], [4, 9]]
    elif texts == ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                   'top left side of the placket', 'front right side of the collar', 'right side of the collar',
                   'left side of the shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve',
                   'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve',
                   'left and upper body of the shirt', 'left and lower body of the shirt',
                   'bottom left side of the shirt', 'bottom left side of the shirt placket',
                   'bottom right side of the shirt', 'right and lower body of the shirt',
                   'right and upper body of the shirt', 'right sleeve', 'right sleeve', 'right sleeve',
                   'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                   'right side of the shoulder seam', 'top right side of the placket',
                   'upper right side of the shirt placket', 'lower right side of the shirt placket',
                   'bottom right side of the shirt placket', 'upper left side of the shirt placket',
                   'lower left side of the shirt placket']:
        edges = [[0, 1], [1, 2], [2, 3], [2, 4], [4, 5], [1, 6], [5, 33], [6, 16], [33, 22], [16, 17], [17, 18],
                 [18, 19], [19, 35], [22, 21], [21, 20], [20, 34], [3, 37], [37, 36], [36, 35], [37, 30], [30, 31],
                 [31, 32], [32, 34], [3, 29], [29, 28], [28, 27], [27, 26], [26, 25], [25, 24], [24, 23], [23, 22],
                 [16, 15], [15, 14], [14, 13], [13, 12], [12, 11], [11, 10], [10, 9], [9, 8], [8, 7], [7, 6]]
    elif texts == ['back side of the collar', 'left side of the collar', 'front left side of the collar',
                   'front side of the collar', 'front right side of the collar', 'right side of the collar',
                   'left side of the shoulder seam', 'left sleeve', 'left sleeve', 'left sleeve', 'left sleeve',
                   'left sleeve', 'left and upper body of the dress', 'left and upper body of the dress',
                   'left body of the dress', 'left and lower body of the dress', 'bottom left side of the dress',
                   'bottom side of the dress', 'bottom right side of the dress', 'right and lower body of the dress',
                   'right body of the dress', 'right and upper body of the dress', 'right and upper body of the dress',
                   'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve', 'right sleeve',
                   'right side of the shoulder seam']:
        edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [1, 6], [5, 28], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11],
                 [2, 12], [3, 13], [12, 14], [14, 15], [15, 16], [16, 17], [17, 18], [18, 19], [19, 20], [20, 21],
                 [21, 22], [4, 22], [22, 23], [23, 24], [24, 25], [25, 26], [26, 27], [27, 28]]

    else:
        print(f"Custom graph not found for {img_metas[0]['query_point_descriptions']}. Exiting...")
        exit(-1)
    return edges