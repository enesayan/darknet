from __future__ import print_function
from os import listdir, getcwd, remove

labels = ['ball', 'goal', 'robot']
# label_numbers = ['n04254680', 'n03820318', 'n02710201']
# label_dict = dict(zip(labels, label_numbers))
# label_number_dict = dict(zip(label_numbers, labels))

if __name__ == "__main__":
    pwd = getcwd()
    for label in labels:
        label_dir = 'annotations/%s' % label
        img_dir = 'images/%s' % label
        label_files = listdir(label_dir)
        img_files = listdir(img_dir)
        print('-- %s --' % label)
        print('Original #annotations: %s' % len(label_files))
        print('Original #imgs: %s' % len(img_files))
        # Remove redundant label files
        label_dels = [x for x in label_files
                      if not(x.split('.xml')[0] + '.JPEG' in img_files or
                             x.split('.xml')[0] + '.jpg' in img_files)]
        print('After #annotations: %s' % (len(label_files) - len(label_dels)))
        for label_file in label_dels:
            label_path = '%s/%s/%s' % (pwd, label_dir, label_file)
            print('\t Deleting file: %s' % label_path)
            remove(label_path)

        # Remove redundant image files
        img_dels = [x for x in img_files
                    if not(x.split('.jpg')[0] + '.xml' in label_files or
                           x.split('.JPEG')[0] + '.xml' in label_files)]
        print('After #imgs: %s' % (len(img_files) - len(img_dels)))
        for img_file in img_dels:
            img_path = '%s/%s/%s' % (pwd, img_dir, img_file)
            print('\t Deleting file: %s' % img_path)
            remove(img_path)
        print('Done!')
