import os
import json

mp78_annotations_dir = 'data/mp78_annotations_settingB'
mp100_annotations_dir = 'data/mp100/annotations'

# iterate over all json files in mp78_annotations_dir:
for mp78_annotation_file in [f for f in os.listdir(mp78_annotations_dir) if f.endswith('.json')]:
    # read json file with annotations:
    with open(os.path.join(mp78_annotations_dir, mp78_annotation_file), 'r') as file:
        mp78_annotations_json = json.load(file)

    # split string using '_' as separator:
    # file_name_parts = os.path.basename(mp78_annotation_file).split('_')
    # mp100_annotation_file = os.path.join(mp100_annotations_dir, "mp100_" + '_'.join(file_name_parts[2:]) + '.json')
    mp100_annotation_file = os.path.join(mp100_annotations_dir, 'mp100_all.json')

    # read json file with annotations:
    with open(mp100_annotation_file, 'r') as file:
        mp100_annotations_json = json.load(file)

    # make a copy of the annotation file:
    fixed_annotations_json = mp78_annotations_json.copy()
    for category in fixed_annotations_json['categories']:
        # find the category in mp100_annotations_json:
        mp100_category = next((c for c in mp100_annotations_json['categories'] if c['id'] == category['id']), None)
        if mp100_category is None:
            print(f"Category with id {category['id']} not found in mp100 annotations.")
            exit(-1)
        category['skeleton'] = mp100_category['skeleton']

    # write fixed annotations to file:
    with open(os.path.join(mp78_annotations_dir, 'fixed_' + mp78_annotation_file), 'w') as file:
        json.dump(fixed_annotations_json, file, indent=2)
        print(f"Fixed annotations written to {'fixed_' + mp78_annotation_file}")
