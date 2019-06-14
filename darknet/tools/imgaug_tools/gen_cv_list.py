import os

def gen_cv_list(img_path):
    imgs_f = open(img_path, 'r')
    imgs = imgs_f.readlines()

    cv_0 = open('../../data/cv_list/cv_0.txt', 'w')
    cv_1 = open('../../data/cv_list/cv_1.txt', 'w')
    cv_2 = open('../../data/cv_list/cv_2.txt', 'w')
    cv_3 = open('../../data/cv_list/cv_3.txt', 'w')
    cv_4 = open('../../data/cv_list/cv_4.txt', 'w')

    count = 0
    for i in imgs:
        if count / 50 < 1:
            cv_0.write(i)
        elif count / 50 < 2:
            cv_1.write(i)
        elif count / 50 < 3:
            cv_2.write(i)
        elif count / 50 < 4:
            cv_3.write(i)
        else:
            cv_4.write(i)
        count += 1

def gen_data_aug_cv_list(cv_0, cv_1, cv_2, cv_3, cv_4, img_path):
    imgs_f = open(img_path, 'r')
    imgs = imgs_f.readlines()

    cv_0 = open(cv_0, 'r')
    cv_1 = open(cv_1, 'r')
    cv_2 = open(cv_2, 'r')
    cv_3 = open(cv_3, 'r')
    cv_4 = open(cv_4, 'r')

    cv_0 = cv_0.readlines()
    cv_1 = cv_1.readlines()
    cv_2 = cv_2.readlines()
    cv_3 = cv_3.readlines()
    cv_4 = cv_4.readlines()

    tf_0 = open('../../data/cv_list/data_aug_cv_0.txt', 'w')
    tf_1 = open('../../data/cv_list/data_aug_cv_1.txt', 'w')
    tf_2 = open('../../data/cv_list/data_aug_cv_2.txt', 'w')
    tf_3 = open('../../data/cv_list/data_aug_cv_3.txt', 'w')
    tf_4 = open('../../data/cv_list/data_aug_cv_4.txt', 'w')

    for i in imgs:
        img_name = i.strip().split(' ')[0].split('/')[-1:][0].split('_')[-1:][0]

        for j in cv_0:
            name = j.strip().split(' ')[0].split('/')[-1:][0]
            if img_name == name:
                tf_0.write(i)
                break
        for j in cv_1:
            name = j.strip().split(' ')[0].split('/')[-1:][0]
            if img_name == name:
                tf_1.write(i)
                break
        for j in cv_2:
            name = j.strip().split(' ')[0].split('/')[-1:][0]
            if img_name == name:
                tf_2.write(i)
                break
        for j in cv_3:
            name = j.strip().split(' ')[0].split('/')[-1:][0]
            if img_name == name:
                tf_3.write(i)
                break
        for j in cv_4:
            name = j.strip().split(' ')[0].split('/')[-1:][0]
            if img_name == name:
                tf_4.write(i)
                break


if __name__ == '__main__':
    img_path = '../../data/original_list/img_label_shuffle.txt'
    gen_cv_list(img_path)

    # cv_0 = '../../data/cv_list/cv_0.txt'
    # cv_1 = '../../data/cv_list/cv_1.txt'
    # cv_2 = '../../data/cv_list/cv_2.txt'
    # cv_3 = '../../data/cv_list/cv_3.txt'
    # cv_4 = '../../data/cv_list/cv_4.txt'
    # img_path = '../../data/data_augment/all_data_aug_list.txt'
    # gen_data_aug_cv_list(cv_0, cv_1, cv_2, cv_3, cv_4, img_path)
