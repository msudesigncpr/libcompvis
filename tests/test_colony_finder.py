from libcolonyfind.colony_finder import ColonyFinder
import cv2

def test_colony_finder():
    raw_image_path='C:\\Users\\John Fike\\OneDrive\\Documents\\Visual Studio 2022\\cap\\libcolonyfind\\4-5-images'
    csv_out_path='output\cfu-csv'

    cf = ColonyFinder(raw_image_path, csv_out_path)
    cf.run_full_proc() # process images, create annotated images

    images = cf.get_annot_images()
    for file_name, image in images.items():
        cv2.imwrite('output\\annotated-images\\' + str(file_name) + ".jpg", images[file_name])
        print(type(images[file_name]))
        # print(index)


if __name__ == "__main__":
    test_colony_finder()